# 对已有模块试错的试验场函数
import utils, re

map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_1_256.png"
scene_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-scen/Berlin_1_256.map.scen"

dir_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png"

def scene_reader(scene_path=scene_path):
    '''
    读入标准scene文件，返回起点和终点数组

    Args:
        scene_path (str, optional): scene文件的路径. 默认值在launch.py中.

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
            starts.append(start)
            goals.append(goal)
    return starts, goals

# 检查rescale后起点和终点的位置是不是空心的


map = utils.map_load(map_path)
starts, goals = scene_reader(scene_path)

for i in range(len(starts)):
    start = starts[i]
    goal = goals[i]
    if map[start[1]][start[0]]==False: print("起点在墙里")
    if map[goal[1]][goal[0]]==False: print("终点在墙里")

