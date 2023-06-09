# 地图节点
'''
流程：
    1. 初始化：从地图图片读入物理地图数据
    2. 保持服务畅通
        - 服务1： agent站点向地图发送，用来更新自己的位置
             - 输入： 坐标x，y 就从0开始用数组下标格式吧，不要折腾了
             - 输出：成功与否
        - 服务2： 向站点发送地图数据
             - 输入：无
             - 输出：真地图，但是打成一维，开头附上宽高数据，方便恢复。
'''


from PIL import Image
import numpy as np

map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/map_builder/map1.png"

def map_reader(map_path):
    '''
    将地图图片读取为二维数组的函数

    Args:
        map_path (string): 地图图片的路径，编写此函数时用的是绝对路径。不推荐相对路径，因为ros2功能包里的src路径不太适合放图片吧 

    Returns:
        list: 二维数组，其中地图图片中白色的地方是True，黑色像素的地方是False
    '''
    with Image.open(map_path) as img:
       width, height = img.size
       pixels = img.load()
       bool_array = [[False for _ in range(width)] for _ in range(height)]
       for i in range(height):
           for j in range(width):
               if pixels[j, i] == (255, 255, 255):
                   bool_array[i][j] = True
       return bool_array

def map_condenser(map_list_2d):    
    '''
    将二维的数组压缩为一维的函数，压缩后在开头附上宽高数据，以便接收端恢复

    Args:
        map_list_2d (list[list[]]): 用来保存地图数据的二维数组 

    Returns:
        list: 被压缩为一维的数组，且开头附有宽高信息
    '''
    width = len(map_list_2d[0])
    height = len(map_list_2d)

    flattened = [_ for row in map_list_2d for _ in row]

    flattened.insert(0,width)
    flattened.insert(1,height)

    return flattened

def map_uncondenser(map_list_1d):
    '''
    将输入的一维数组恢复为二维数组的函数，输入的一维数组第一位是原数组宽，第二位是原数组高

    Args:
        map_list_1d (list): 输入的一维数组第一位是原数组宽，第二位是原数组高

    Returns:
        list[list[]]: 恢复的二维数组
    '''
    width = map_list_1d[0]
    height = map_list_1d[1]

    del map_list_1d[:2]

    map_list_2d = [map_list_1d[i:i+width] for i in range(0,len(map_list_1d),width)]

    return map_list_2d

map_list = map_reader(map_path)

flattened_map = map_condenser(map_list)

resumed_map = map_uncondenser(flattened_map)


print(map_list==resumed_map)

