from heapq import heappop, heappush
from math import inf
import time as t


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


def cut_path(path, plan_dict):
    '''
    根据传入的计划和自己路径的冲突部分，将发生冲突的部分及以后的路径全部剪掉

    Args:
        path (list): 路径
        plan_dict (dict): 原生计划字典
    '''
    for plan in list(plan_dict.values()):
        min_length = min(len(path), len(plan))  # 获取最小长度
        # 获得同位置元素相同的位置标号
        indices = [i for i in range(min_length) if path[i] == plan[i]]
        if indices:
            index = indices[0]
            if index-1 >= 0:
                path = path[:index-1]
            else:
                path = []
    return path


def init_algo(current_pos, path, plan_no_id):
    # 返回：起点，修剪后的path，时间

    if path and not plan_no_id: # 自己有计划但还没收到别人计划的场合：直接继续
        start = path[-1]
        path_for_return = path
        cost = len(path)-1
        return start, path_for_return, cost
    
    elif path and plan_no_id: # 两个都不空的场合
        start = current_pos  # 初始化起点
        path_for_return = []  # 初始化用于返回的清洁路径
        # 逐个检查收到的计划和自己的计划，如有冲突则剪掉

        min_length = min(len(path), len(plan_no_id))  # 获得自己计划和别人计划中的最小长度
        cost = 0  # 初始化时间值
        for i in range(min_length):
            # 检查是否有碰撞，如果有就停止
            my_pos = path[i]
            others_pos = plan_no_id[i]
            # 如果没有碰撞，更新路径和起点
            if my_pos not in others_pos:
                start = my_pos
                path_for_return.append(my_pos)
                cost += 1
            else: break
        # 如果滤遍了计划，还是没有碰：返回完整的计划和时间
        return start, path_for_return, cost
    else: # path为空的场合
        start = current_pos
        path_for_return = []
        cost = 0
        return start, path_for_return, cost


def find_path(time_limit, map, path, others_positions, current_pos, goal, plan_dict={}, first_ever=False):
    '''
    寻路算法

    Args:
        time_limit(float): 本次算法所可以使用的时间长度
        map (list[list]): 地图：二维数组，[[行]], 其中True代表可通行，False代表障碍物
        path(list(tuple)): 计划。当前节点有的计划。其中部分还没执行呢
        others_positions(dict): 此时刻别人的位置。解决计划中不含当前位置的问题，主要是消除swap碰撞用
        current_pos(tuple): 我现在在哪里
        goal(tuple): 终点位置
        plan_dict(dict): 原生格式的计划字典
        first_ever(bool): 进行计划的节点是否已经phase in
    Returns:
        生成的计划 (list[tuple]): 生成的计划， [(横坐标，纵坐标)], 越往前越是下一步该执行的计划。此计划不包含起始点（即输入的start）
    '''
    start_time = t.time()
    # 以时间片分割的计划
    plan_no_id = list(plan_dict.values())
    plan_no_id = transpose_list(plan_no_id)

    # 根据自己的计划和收到的计划，切割路径，返回算法起点和对应的时间值
    start, path_remain, time = init_algo(current_pos, path, plan_no_id)

    # 初始化寻路算法需要的工具
    path_for_return = path_remain  # 寻路算法生成的结果
    queue = [(heuristic(start, goal), time, start, path_remain)]
    visited = set([])
    time_remain = time_limit - (t.time()-start_time)  # 留给后面的时间
    start_time = t.time()  # 后面开始

    # 直到超时或遍历完以前，都继续
    while t.time()-start_time < time_remain*0.8 and queue:
        _, time, current, path = heappop(queue)
        path_for_return = path

        if current_pos == goal:  # 如果达到终点：结束
            return path

        current_others_plan = []
        if plan_no_id and time < len(plan_no_id):  # 根据时间提取当前时间点其他节点的计划
            current_others_plan = plan_no_id[time]
        # 获得不上墙也不和别人碰撞的邻居点
        neighbors = get_neighbors(current, map, current_others_plan)

        # 如果是入网以来第一次筹谋，则第一步必须是起点
        if not path and first_ever:
            neighbors = [start]

        # 去除swap碰撞类型
        if time != 0:  # 非第一步的swap去除
            neighbors = remove_swap_collision_positions(
                current, neighbors, time, plan_dict)
        else:  # 第一步的swap去除
            neighbors = remove_swap_collision_positions_first(
                current, neighbors, time, plan_dict, others_positions)

        for neighbor in neighbors:
            new_time = time+1
            if tuple(list(neighbor)+[new_time]) not in visited:
                heappush(queue, (new_time+heuristic(neighbor, goal),
                         new_time, neighbor, path+[neighbor]))
                visited.add(tuple(list(neighbor)+[new_time]))

    # 返回生成的路径
    return path_for_return


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


def remove_swap_collision_positions(current, neighbors_with_swaps, cost, plan_dict):
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