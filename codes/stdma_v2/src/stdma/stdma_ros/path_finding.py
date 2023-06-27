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


def find_path(map, max_steps, start=(0,0), goal=(3,3), plan  = []):
    '''
    寻路算法

    Args:
        map (list[list]): 地图：二维数组，[[行]], 其中True代表可通行，False代表障碍物
        max_steps (int): 生成计划的最大长度上限
        start (tuple, optional): 起始位置坐标. Defaults to (0,0).
        goal (tuple, optional): 终点位置坐标. Defaults to (3,3).
        plan (list[(x,y)], optional): 计划保存变量, [[计划]] . Defaults to [].

    Returns:
        生成的计划 (list[tuple]): 生成的计划， [(横坐标，纵坐标)], 越往前越是下一步该执行的计划。此计划不包含起始点（即输入的start）
    '''
    start = tuple(start)
    goal = tuple(goal)

    # 处理一下输入的计划，变成以时间步划分的计划
    plan = plan.copy()
    plan = transpose_list(plan) # 转换完成


    # 使用优先级队列来保存待探索的节点，优先级由估计的路径长度决定
    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set([start])


    while queue:
        _, cost, current, path = heappop(queue)

        current_others_plan = []
        
        if len(path) >= max_steps:
            return path

        if current == goal:
            return path
        
        if plan and cost < len(plan): # 根据步数提取当前时间点的其他计划
            current_others_plan = plan[cost]


        neighbors = get_neighbors(current, map, current_others_plan)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = cost + 1
                heappush(queue, (new_cost + heuristic(neighbor, goal), new_cost, neighbor, path + [neighbor]))
                visited.add(neighbor)

        heappush(queue, (_+1, cost+1, current, path+[current])) # 有这行才能有留在原地的选项。不然每一步必须离开原地，影响终点不可达时留在原地的能力
        
    # 如果可探索点用完还没能到达终点：就这样吧
    if path:
        return path

    return []

def get_neighbors(pos, map, plan=[]):
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
        if is_valid(new_pos, map) and new_pos not in plan:
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
    start = (1,1)
    for i in range(20):
        path = find_path(map,20,start = start, goal = (10,10), plan = generated_path)
        path = path#[:i]
        generated_path.append(path)


    for i in range(len(generated_path[0])):
        pos = set()
        for j in range(len(generated_path)):
            if generated_path[j][i] in pos and generated_path[j][i]!=start:
                print("碰撞"+str(generated_path[j][i]))
                print(generated_path[j])
                print("发生在%d,%d"%(i,j))
            else:
                pos.add(generated_path[j][i])

    for _ in generated_path:
        print(_)



        
if __name__ == "__main__":
    main()