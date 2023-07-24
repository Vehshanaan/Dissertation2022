from heapq import heappop, heappush
import math
import time
import os
import cv2
import numpy as np
import random



def remove_black_border(img):
    # 去除图片的黑色边框
    # 获取图像的高度和宽度
    height, width = img.shape

    # 设置边框阈值，这里假设边框为纯黑色
    border_threshold = 50  # 调整阈值以适应实际情况

    # 从上到下扫描，去除顶部的黑色边框
    top = 0
    for y in range(height):
        if np.mean(img[y, :]) > border_threshold:
            top = y
            break

    # 从下到上扫描，去除底部的黑色边框
    bottom = height - 1
    for y in range(height - 1, -1, -1):
        if np.mean(img[y, :]) > border_threshold:
            bottom = y
            break

    # 从左到右扫描，去除左侧的黑色边框
    left = 0
    for x in range(width):
        if np.mean(img[:, x]) > border_threshold:
            left = x
            break

    # 从右到左扫描，去除右侧的黑色边框
    right = width - 1
    for x in range(width - 1, -1, -1):
        if np.mean(img[:, x]) > border_threshold:
            right = x
            break

    # 裁剪图像，去除黑色边框
    img = img[top:bottom, left:right]

    return img


def map_load(map_path, size):
    '''
    读取地图的函数

    Args:
        map_path (str): 地图文件的绝对路径

    Returns:
        map ([[T/F]]): 代表地图的二维列表，其中True代表可通过，False代表障碍物
    '''
    img = cv2.imread(map_path, 0)

    img = remove_black_border(img)

    img = cv2.resize(img, size)  # , interpolation=cv2.INTER_AREA)

    _, img = cv2.threshold(
        img, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化
    
    map = (img != 0).tolist()

    return map

scene_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/my_own_benchmarks/"

def scene_generate(map_path, map_size, scene_path = scene_path):
    '''
    情景档生成器

    Args:
        map_path (str): 地图的绝对路径
        map_size (tuple): (宽, 高)
        scene_path (str, optional): 情景档的保存文件夹. Defaults to scene_path.
    '''



    map_name = os.path.basename(map_path)

    scene_path = scene_path +\
        map_name+str(time.strftime("%h%d%H%M"))+".scen"


    # 读取地图
    map = map_load(map_path, map_size)

    # 生成包含地图中所有外侧位置的列表
    # 除四角以外的四个边
    top_row = [(0, j) for j in range(1, len(map[0])-1)]
    bottom_row = [(len(map)-1, j) for j in range(1, len(map[0])-1)]
    left_col = [(i, 0) for i in range(1, len(map)-1)]
    right_col = [(i, len(map[0])-1) for i in range(1, len(map)-1)]

    # 外侧位置的列表，位置本身是元组
    outer_boundary = top_row+bottom_row+left_col+right_col

    width = map_size[0]
    height = map_size[1]
    starts = []
    goals = []
    optimals = []
    while outer_boundary:  # 当还有点的时候
        start = random.choice(outer_boundary)
        outer_boundary.remove(start)  # 提取过的起点删除掉

        start = (start[1],start[0])
        # 计算对应的终点
        goal = (width-1-start[0], height-1-start[1])

        optimal = find_path(map,start,goal)

        starts.append(start)
        goals.append(goal)
        optimals.append(optimal)

    # 将生成的起点终点塞进标准格式的scene文件中
    with open(scene_path,"w") as scene:
        scene.write("version 1\n")
        for i in range(len(starts)):
            line = "1" + "\t"+map_name+"\t"+str(map_size[0])+"\t"+str(map_size[1])+"\t"+str(starts[i][0])+"\t"+str(starts[i][1])+"\t"+str(goals[i][0])+"\t"+str(goals[i][1])+"\t"+str(optimals[i])
            scene.write(line+"\n")

    print("done!")


def scene_reader(scene_path, min_dist=-1):
    '''
    读入标准scene文件，返回起点和终点数组

    Args:
        scene_path (str, optional): scene文件的路径. 默认值在launch.py中.

        min_dist (int): 起点和终点之间的最小距离，小于这个距离的将被滤除

    Returns:

        starts [(x,y)]: 起点的坐标

        goals [(x,y)]: 终点的坐标
    '''
    starts = []
    goals = []
    with open(scene_path, "r") as scene:
        for line in scene:
            words = line.strip().split(" ")
            if len(words) == 2:
                continue  # 过滤掉开头的version空格1
            words = words[0].strip().split("\t")
            # 第5，6个元素是起点横纵坐标
            start = (int(words[4]), int(words[5]))
            # 第7，8个元素是终点横纵坐标
            goal = (int(words[6]), int(words[7]))
            # 最后一个元素是最优距离
            optimal_dist = float(words[-1])
            if optimal_dist < min_dist:
                continue  # 如果最优距离小于阈值：跳过，不读入这组起终点
            starts.append(start)
            goals.append(goal)
    return starts, goals



def find_path(map, start=(0,0), goal=(3,3)):

    start = tuple(start)
    goal = tuple(goal)

    # 使用优先级队列来保存待探索的节点，优先级由估计的路径长度决定
    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set([start])

    path = []

    while queue:
        _, cost, current, path = heappop(queue)
                
        if current == goal: return len(path)

        neighbors = get_neighbors(current, map)

    
        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = cost + 1
                heappush(queue, (new_cost + heuristic(neighbor, goal), new_cost, neighbor, path + [neighbor]))
                visited.add(neighbor)

    return -1 # 没道儿啊        
  

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

        if is_valid(new_pos, map): # 如果不在地图障碍物中：
            neighbors.append(new_pos)

    return neighbors

def is_valid(pos, map): # 记得xy倒回去！我的其他代码格式里可能全反了，我刚发现。

    x = pos[0]
    y = pos[1]

    col_max = len(map)
    row_max = len(map[0])

    if 0 <= y < col_max and 0 <= x < row_max:
        if map[y][x]:
            return True

    return False

def heuristic(pos, goal):
    # 使用曼哈顿距离作为启发式估计
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


if __name__ == "__main__":

    map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/randoms/mapf-png/warehouse-10-20-10-2-1.png"
    map_size = (162, 61)  # 162,64
    scene_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/my_own_benchmarks/"


    scene_generate(map_path,map_size,scene_path)

    #main()