import time
import random
import os
import json
from PIL import Image
map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_0_256.png"
save_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/generated_scenes"

def map_load(map_path=map_path):
    '''
    读入地图并在地图外围加上五圈，加入的五圈均为可通行的通道

    Args:
        map_path (str): 地图文件的路径

    Returns:
        bigger_map ([list]): 地图的二维数组，True代表可通行，False代表不可通行
    '''

    with Image.open(map_path) as img:

        width, height = img.size
        pixels = img.load()

        origin_map = [[True for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if pixels[j, i][0:3] != (229, 229, 229):  # 如果不是代表通路的浅灰色：不通。
                    origin_map[i][j] = False

        # 将地图扩大五圈
        bigger_map = [[True for _ in range(width+10)]
                      for _ in range(height+10)]
        for i in range(len(origin_map)):
            for j in range(len(origin_map[0])):
                bigger_map[i+5][j+5] = origin_map[i][j]

        return bigger_map


def start_goal_generator(node_num, map_path=map_path):
    '''
    读取地图并返回若干随机初始出生点的函数

    Args:
        node_num (int): 节点数目
        map_path (str): 地图图片的绝对路径

    Returns:
        starts ([list]): 起点的位置

        goals ([list]): 终点的位置 
    '''
    map = map_load(map_path)

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

    sum = [map_height-1,map_width-1]

    for start in starts:
        goal = [sum[0]-start[0],sum[1]-start[1]]
        goals.append(goal)


    return starts, goals

def scene_generator(node_number, save_path, map_path = map_path):
    starts,goals = start_goal_generator(node_number,map_path)

    file_name = os.path.basename(map_path) + str(node_number)+ "nodes" + str(time.time())

    file_path = save_path + "/" + file_name

    data = {
        "node_number":node_number,
        "map_path":map_path,
        "starts":starts,
        "goals":goals
    }

    with open(file_path,"w")as file:
        json.dump(data,file)


    with open(file_path,"r") as file:
        data = json.load(file)
    
    node_number_check  =  data["node_number"]
    map_path_check = data["map_path"]
    starts_check = data["starts"]
    goals_check = data["goals"]

    print(node_number==node_number_check)
    print(map_path == map_path_check)
    print(starts == starts_check)
    print(goals == goals_check)

scene_generator(10,save_path,map_path)



