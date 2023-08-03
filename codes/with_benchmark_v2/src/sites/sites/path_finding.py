from heapq import heappop, heappush
from math import inf

from numpy import require


def transpose_list(input_list):
    '''
    将输入的二维列表中的成员列表的每个相同位置的元素放进一个列表最后打包成一个新二维列表的函数
    '''
    if not input_list:
        return None
    num_rows = len(input_list)
    num_cols = max(len(row) for row in input_list)

    transposed_list = [[] for _ in range(num_cols)]
    for row in input_list:
        for col_index, element in enumerate(row):
            transposed_list[col_index].append(element)

    return transposed_list


def find_path(map, required_length, horizon, others_positions, start=(0, 0), goal=(3, 3), plan_dict={}, first_ever=False):
    '''
    寻路算法

    Args:
        map (list[list]): 地图：二维数组，[[行]], 其中True代表可通行，False代表障碍物
        required_length (int): 所需计划的长度
        horizon (int): 生成计划的最大时间维长度 这个和timer的单个帧长度直接相关，60对应0.5，不要随便改
        others_positions (dict): 筹谋时刻的其他节点的位置
        start (tuple, optional): 起始位置坐标. Defaults to (0,0).
        goal (tuple, optional): 终点位置坐标. Defaults to (3,3).
        plan ({node_id: [(x,y),...]}, optional): 计划保存变量, {node_id: [(x,y),...]} . Defaults to {}.
        first_ever (bool): 是否是加入网络之后第一次筹谋？如果是的话，第一步必须是起点
    Returns:
        生成的计划 (list[tuple]): 生成的计划， [(横坐标，纵坐标)], 越往前越是下一步该执行的计划。此计划不包含起始点（即输入的start）
    '''
    start = tuple(start)
    goal = tuple(goal)

    if start == goal:
        return [goal]  # 到了终点其实就不该进入这个函数了，除非是出生就在终点不然不会触发这一行的

    # 处理一下输入的计划，变成以时间步划分的计划
    plan_no_id = list(plan_dict.values())
    plan_no_id = transpose_list(plan_no_id)  # 转换完成

    # 使用优先级队列来保存待探索的节点，优先级由估计的路径长度决定
    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set([])  # 已扩展过的点。已扩展过的点后面不会再重复扩了

    paths = []  # 保存所有生成的长度达标的路径，如果一直没有能到终点的路径，就从这里面挑一个

    while queue:
        _, cost, current, path = heappop(queue)

        if len(path) == horizon:
            paths.append(path)  # 如果获得了想要的长度的路径：保存
        if len(path) > horizon:
            continue  # 长度到了就不要继续了，这样实现finite horizon。这后面的这个数值就是horizon的长度
        if current == goal and cost <= required_length:
            return path  # 节点到达终点后会直接self.destroy_node(), 不用管那么多了

        current_others_plan = []
        if plan_no_id and cost < len(plan_no_id):  # 根据步数提取当前时间点的其他计划
            current_others_plan = plan_no_id[cost]

        # 获得不上墙也不和别人碰的邻居点
        neighbors = get_neighbors(current, map, current_others_plan)

        # 如果是入网以来第一次筹谋，则第一步必须是起点
        if first_ever and cost == 0:
            neighbors = [start]

        # 去除swap碰撞类型
        if cost != 0:  # 对于非第一步的swap去除
            neighbors = remove_swap_collision_postions(
                current, neighbors, cost, plan_dict)
        else:  # 对于第一步的swap去除
            neighbors = remove_swap_collision_positions_first(
                current, neighbors, cost, plan_dict, others_positions)

        for neighbor in neighbors:
            new_cost = cost + 1
            if tuple(list(neighbor)+[new_cost]) not in visited:  # 不可重复扩展的是三维空间的点，不是二维
                heappush(queue, (new_cost + heuristic(neighbor, goal),
                         new_cost, neighbor, path + [neighbor]))
                visited.add(tuple(list(neighbor)+[new_cost]))

    # 如果可探索点用完还没能到达终点：从生成的路径里找一个离终点最近的
    if paths:
        # 找一个最后的点离终点最近的 这个是用horizon长度的计划的最后一位判断的
        min_dist = inf  # 最短距离
        label = -1  # 是谁
        for i in range(len(paths)):
            final_pos = paths[i][-1]
            dist = abs(final_pos[0]-goal[0])+abs(final_pos[1]-goal[1])
            if dist < min_dist:
                min_dist = dist
                label = i
        path = paths[label]

        # 长度如果不够：补齐
        if path and len(path) < required_length:
            path = path+[path[-1]]*(required_length-len(path))

        return path[:required_length]  # 返回的时候就截一下

    else:
        return None  # 如果没能找到计划：返回None 这其实是不应该的，这意味着场地的空间放不下节点了。


def remove_swap_collision_positions_first(current, neighbors_with_swaps, cost, plan_dict, others_positions):
    neighbors = []
    next_steps = {}
    if plan_dict:
        for node_id, plan in plan_dict.items():
            if cost < len(plan):
                pos = plan[cost]
                next_steps[node_id] = pos
    for neighbor in neighbors_with_swaps:
        add = True
        if next_steps:
            for node_id, pos in next_steps.items():
                if pos == current:
                    if others_positions:
                        if others_positions[node_id] == neighbor:
                            add = False
        if add:
            neighbors.append(neighbor)
    return neighbors


def remove_swap_collision_postions(current, neighbors_with_swaps, cost, plan_dict):
    neighbors = []
    # 先生成当前计划和上一步计划
    # 当前步计划
    next_steps = {}
    # 所有节点当前的位置（其实就是上一步计划）
    current_positions = {}
    if plan_dict:
        for node_id, plan in plan_dict.items():
            # 先提取当前步计划
            if cost < len(plan):  # 如果计划有那么长：
                pos = plan[cost]
                next_steps[node_id] = pos  # tuple(pos)
            # 再提取之前步计划
            if cost-1 >= 0 and cost-1 < len(plan):
                pos = plan[cost-1]
                current_positions[node_id] = pos  # tuple(pos)

    for neighbor in neighbors_with_swaps:
        add = True
        if next_steps:
            for node_id, pos in next_steps.items():
                if pos == current:  # 如果有人的下一步是到我现在的位置
                    if current_positions:
                        # 如果此人的当前位置等于我下一步想去的位置
                        if current_positions[node_id] == neighbor:
                            add = False  # 这就是swap了，不行
        if add:
            neighbors.append(neighbor)

    return neighbors


def get_neighbors(pos, map, current_plan=[]):
    '''
    获得一个点周围可用的点

    Args:
        pos (tuple): 当前位置
        map (list[list]): 地图
        plan (list[tuple]): 下一步的计划，是主函数根据时间点从计划总保存变量中切割出来的一片。

    Returns:
        _type_: _description_
    '''
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向和原地。
    neighbors = []

    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if is_valid(new_pos, map) and new_pos not in current_plan:  # 如果不在地图障碍物且不在别人的下一步计划中：
            neighbors.append(new_pos)

    return neighbors


def is_valid(pos, map):

    x = pos[0]
    y = pos[1]

    col_max = len(map)
    row_max = len(map[0])

    if 0 <= x < row_max and 0 <= y < col_max:
        if map[y][x]:
            return True

    return False


def heuristic(pos, goal):
    # 使用曼哈顿距离作为启发式估计
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


# 地图的绝对文件路径
map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/map_builder/map2.png"


def main():

    # 创建一个示例地图
    map = [[True]*20]*20

    max_steps = 10  # 限制路径最大长度为5

    # 测试程序是否产生碰撞
    generated_path = []
    start = (1, 1)
    for i in range(20):
        path = find_path(map, 20, start=start, goal=(
            10, 10), plan=generated_path)
        path = path  # [:i]
        generated_path.append(path)

    # generated_path = [[(0,0),(0,1)],[(1,1),(0,1)]]

    for i in range(len(generated_path[0])):
        pos = set()
        for j in range(len(generated_path)):
            if generated_path[j][i] in pos and generated_path[j][i] != start:
                print("碰撞"+str(generated_path[j][i]))

                # print(generated_path[j])
                print("发生在下面数组中的%d,%d" % (i, j))
            else:
                pos.add(generated_path[j][i])

    for _ in generated_path:
        print(_)


if __name__ == "__main__":
    pass
