import cv2
import re
import os
import numpy as np
map_path1 = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_1_256.png"
map_path2 = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/randoms/mapf-png/maze_1_32.png"


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
    img = cv2.imread(map_path,0)

    img = remove_black_border(img) # 调试长廊时暂时消掉，回来记得补回来！

    img = cv2.resize(img, size)#, interpolation=cv2.INTER_AREA)

    _,img = cv2.threshold(img,1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 二值化 

    map = (img!=0).tolist()

    return map

def id_to_color(code):
    '''
    根据输入的编号生成唯一对应RGB颜色

    Args:
        code (int): 节点编号

    Returns:
        color (r,g,b): 三通道值
    '''
    number = int(code)
    r = (number * 127) % 256  # 每个通道的取值范围是0-255
    g = (number * 83) % 256
    b = (number * 43) % 256
    return (r, g, b)

def plan_compressor(node_id, plan2d) -> list:
    '''
    将[[x1,y1],[x2,y2],...]格式的二维数组压缩成一维的函数

    Args:
        node_id: 发送者编号
        plan (list[list]): [[x1,y1],[x2,y2],...]格式的二维数组

    Returns:
        result: 格式为[node_id,x1,y1,x2,y2,...]的一维数组
    '''
    if not plan2d:  # 如果输入为空列表
        return [node_id]  # 返回无计划的列表
    else:
        plan1d = [node_id]
        for _ in plan2d:
            plan1d.append(_[0])
            plan1d.append(_[1])


    return plan1d


def plan_decompressor(plan1d):
    '''
    将格式为[节点id, x1,y1,x2,y2...]格式的数组还原为 发送者id，[[x1,y1],[x2,y2],...] 的两个输出

    Args:
        plan1d (list): [节点id,x1,y1,x2,y2...]格式的一维数组

    Returns:
        node_id: 发送者id

        plan2d: [[x1,y1],[x2,y2],...]格式的二维数组
    '''
    if not plan1d:
        return -1, [[]]  # 如果输入为空，返回空, id写-1
    else:
        plan2d = []
        node_id = plan1d.pop(0)
        for i in range(0, len(plan1d), 2):
            plan2d.append((plan1d[i], plan1d[i+1]))
    return node_id, plan2d


if __name__ == "__main__":
    map = map_load(map_path)
    print(len(map))
