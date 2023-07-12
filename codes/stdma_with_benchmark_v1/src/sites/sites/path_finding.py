from gettext import find
from heapq import heappop, heappush
from operator import ge


def transpose_list(input_list):
    '''
    将输入的二维列表中的成员列表的每个相同位置的元素放进一个列表最后打包成一个新二维列表的函数
    '''
    if not input_list: return None
    num_rows = len(input_list)
    num_cols = max(len(row) for row in input_list)

    transposed_list = [[] for _ in range(num_cols)]
    for row in input_list:
        for col_index, element in enumerate(row):
            transposed_list[col_index].append(element)

    return transposed_list


def find_path(map, max_steps, self_id = -1, start=(0,0), goal=(3,3), plan_dict = {}):
    '''
    寻路算法

    Args:
        map (list[list]): 地图：二维数组，[[行]], 其中True代表可通行，False代表障碍物
        max_steps (int): 生成计划的最大长度上限
        start (tuple, optional): 起始位置坐标. Defaults to (0,0).
        goal (tuple, optional): 终点位置坐标. Defaults to (3,3).
        plan ({node_id: [(x,y),...]}, optional): 计划保存变量, {node_id: [(x,y),...]} . Defaults to {}.

    Returns:
        生成的计划 (list[tuple]): 生成的计划， [(横坐标，纵坐标)], 越往前越是下一步该执行的计划。此计划不包含起始点（即输入的start）
    '''
    start = tuple(start)
    goal = tuple(goal)

    if start == goal: return [goal]*max_steps # 如果到了终点：就呆在终点！

    # 处理一下输入的计划，变成以时间步划分的计划
    plan_no_id = list(plan_dict.values()).copy()
    plan_no_id = transpose_list(plan_no_id) # 转换完成



    # 使用优先级队列来保存待探索的节点，优先级由估计的路径长度决定
    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set([start])

    path = []

    while queue:
        _, cost, current, path = heappop(queue)
        

        
        if current ==goal: return path[:max_steps]
            

        current_others_plan = []
        if plan_no_id and cost < len(plan_no_id): # 根据步数提取当前时间点的其他计划
            current_others_plan = plan_no_id[cost]




        neighbors_ = get_neighbors(current, map, current_others_plan)



        # TODO:写一个函数从neighbours里去除swap，注意位置数据都是元组（x,y）格式
        # 如果邻居点（可用备选计划点）中有别人现在正在用的点（current计划的前一页），且这个人下一步想到我现在的位置（current）：neighbours弃掉。
        # 注意出界的问题
        neighbors = []
        # 先生成当前计划和上一步计划
        # 当前步计划
        next_steps = {}
        current_positions = {}
        if plan_dict:
            for node_id, plan in plan_dict.items():
                # 先提取当前步计划
                if cost<len(plan): # 如果计划有那么长：
                    pos = plan[cost]
                    next_steps[node_id] = tuple(pos)
                # 再提取之前步计划
                if cost-1>=0 and cost-1<len(plan):
                    pos = plan[cost-1]
                    current_positions[node_id] = tuple(pos)


        for neighbor in neighbors_: 
            add = True
            if next_steps:
                for node_id, pos in next_steps.items():
                    if pos == current:
                        if current_positions:
                            if current_positions[node_id] == neighbor:

                                add = False
            if add: neighbors.append(neighbor)
        


        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = cost + 1
                heappush(queue, (new_cost + heuristic(neighbor, goal), new_cost, neighbor, path + [neighbor]))
                visited.add(neighbor)

        
    # 如果可探索点用完还没能到达终点：就这样吧
    if path:
        print("this")
        return path[:max_steps]

    else:
        return [start]*max_steps # 如果产生的路径是空的：呆在原地    

def remove_swap_collision_postions(neighbors, cost, plan, ): pass

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
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向
    neighbors = []



    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if is_valid(new_pos, map) and new_pos not in current_plan: # 如果不在地图障碍物且不在别人的下一步计划中：
            neighbors.append(new_pos)

    return neighbors

def is_valid(pos, map): # 记得xy倒回去！我的其他代码格式里可能全反了，我刚发现。

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
    start = (1,1)
    for i in range(20):
        path = find_path(map,20,start = start, goal = (10,10), plan = generated_path)
        path = path#[:i]
        generated_path.append(path)

    #generated_path = [[(0,0),(0,1)],[(1,1),(0,1)]]

    
    for i in range(len(generated_path[0])):
        pos = set()
        for j in range(len(generated_path)):
            if generated_path[j][i] in pos and generated_path[j][i]!=start:
                print("碰撞"+str(generated_path[j][i]))

                #print(generated_path[j])
                print("发生在下面数组中的%d,%d"%(i,j))
            else:
                pos.add(generated_path[j][i])
    

    for _ in generated_path:
        print(_)



        
if __name__ == "__main__":
    map = [[True,True,True],
           [False,True,False],
           [False,True,True],
           [True,True,True]]
    plan = {1:[(0,1),(1,1),(2,1),(3,1),(3,0)]}
    path = find_path(map,10,-1,(3,0),(0,2),plan_dict = plan)
    print(path) # 应为：31 21 22

    neighbours = get_neighbors((2,0),map,[(0,1)])
    #print(neighbours)

