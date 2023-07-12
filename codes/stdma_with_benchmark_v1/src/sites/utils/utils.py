import time
import random
import os
import json
from PIL import Image
import cv2
map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_0_256.png"
save_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/generated_scenes"


def map_load(map_path=map_path, size=(-1, -1)):
    '''
    读入地图并在地图外围加上五圈，加入的五圈均为可通行的通道

    Args:
        map_path (str): 地图文件的路径
        size ((宽，高))): 要把打开的地图缩放到什么程度

    Returns:
        bigger_map ([list]): 地图的二维数组，True代表可通行，False代表不可通行
    '''
    '''

    with Image.open(map_path) as img:

        if size == (-1, -1):
            pass
        else:
            img = img.resize(size)  # 一律重新调整大小

        width, height = img.size
        pixels = img.load()

    '''
    img = cv2.imread(map_path,0)
    if size!=(-1,-1):img = cv2.resize(img,size)
    _,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 大津二值化
    height,width=img.shape
    origin_map = [[True for _ in range(width)] for _ in range(height)]
    for i in range(height): # 纵坐标
        for j in range(width): # 横坐标
            if img[i, j] == 0:  # 如果不是代表通路的浅灰色：不通。 # 调用索引是先纵坐标后横坐标
                origin_map[i][j] = False
    # 将地图扩大五圈
    bigger_map = [[True for _ in range(width+10)]
                  for _ in range(height+10)]
    for i in range(len(origin_map)):
        for j in range(len(origin_map[0])):
            bigger_map[i+5][j+5] = origin_map[i][j]
    # 将地图外侧五圈改为白色可通过
    return bigger_map


def start_goal_generator(node_num, map_path=map_path, size=(-1, -1)):
    '''
    读取地图并返回若干随机初始出生点的函数

    Args:
        node_num (int): 节点数目
        map_path (str): 地图图片的绝对路径
        size ((宽，高))): 要把打开的地图缩放到什么程度

    Returns:
        starts ([list]): 起点的位置

        goals ([list]): 终点的位置 
    '''
    map = map_load(map_path, size)

    # 生成地图外围一圈除四角位置的坐标的列表：
    map_width = len(map[0])
    map_height = len(map)

    outer_boundary = []  # 外围坐标

    # 将外围点一个个填进外围坐标列表里去
    # 左右两侧的外围点
    for i in range(map_height):
        outer_boundary.append([i, 0])
        outer_boundary.append([i, map_height-1])

    # 上下两侧的外围点
    for i in range(map_width):
        outer_boundary.append([0, i])
        outer_boundary.append([map_width-1, i])

    # 随机种子
    random.seed(int(time.time()))

    # 随机选取若干个点
    starts = random.sample(outer_boundary, node_num)

    '''
    cols_mirror = list(range(map_width))[::-1]  # 横坐标镜像
    rows_mirror = list(range(map_height))[::-1]  # 纵坐标镜像

    goals1 = []

    for start in starts:
        goal = [rows_mirror[start[0]], cols_mirror[start[1]]]
        goals1.append(goal)
    '''
    # 用起点生成终点：将起点的坐标镜像。

    goals = []

    sum = [map_height-1, map_width-1]

    for start in starts:
        goal = [sum[0]-start[0], sum[1]-start[1]]
        goals.append(goal)

    return starts, goals


def scene_generator(node_number, save_path, map_path=map_path, size=(-1, -1)):
    '''
    生成情景的函数（主要生成指定数量的起点和终点），并把生成的情景保存成json文件

    Args:
        node_number (int): 节点数目
        save_path (str): 生成的情景文件的保存文件夹，不含最后那个/ 
        map_path (str): 地图文件的路径
        size ((宽，高))): 要把打开的地图缩放到什么程度
    '''
    starts, goals = start_goal_generator(node_number, map_path, size)

    file_name = os.path.basename(
        map_path) + str(node_number) + "nodes" + str(time.strftime("%H%M")+".scene")

    file_path = save_path + "/" + file_name

    data = {
        "node_number": node_number,
        "map_path": map_path,
        "map_size": size,
        "starts": starts,
        "goals": goals
    }

    with open(file_path, "w")as file:
        json.dump(data, file)

    print(file_path)

def scene_reader(scene_path):
    '''
    从文件加载情景档的函数

    Args:
        scene_path (str): 情景文件的路径

    Returns:
        node_number (int): 节点的数目  

        map_path (str): 地图的路径  

        starts ([list]): 起点位置的列表  

        goals ([list]): 终点位置的列表
    '''
    with open(scene_path, "r") as file:
        data = json.load(file)

    node_number = data["node_number"]
    map_path = data["map_path"]
    map_size = data["map_size"]
    starts = data["starts"]
    goals = data["goals"]

    return node_number, map_path, map_size, starts, goals


# 生成情景档的命令：
# scene_generator(10,save_path,map_path)


# 寻找最优路径的函数
from gettext import find
from heapq import heappop, heappush
from operator import ge


def get_neighbors(pos, map):
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



        if is_valid(new_pos, map):
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

def find_path_optimal(map, start=(0,0), goal=(3,3),):
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



    # 使用优先级队列来保存待探索的节点，优先级由估计的路径长度决定
    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set([start])


    while queue:
        _, cost, current, path = heappop(queue)

        
        if current == goal:
            return path

        '''
        if current == goal:
            if len(path)<max_steps:
                for ii in range(max_steps-len(path)):
                    path.append(current)
            return path # 保证即使已经达到终点，计划仍然是那么长
        '''


        neighbors = get_neighbors(current, map)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = cost + 1
                heappush(queue, (new_cost + heuristic(neighbor, goal), new_cost, neighbor, path + [neighbor]))
                visited.add(neighbor)

        # 每一步必须离开原地
        
    # 如果可探索点用完还没能到达终点：就这样吧
    if path:
        return path
    else: return[]

if __name__ == "__main__":
    for i in [60,90,]:
        scene_generator(i, save_path, map_path, (50,50))
