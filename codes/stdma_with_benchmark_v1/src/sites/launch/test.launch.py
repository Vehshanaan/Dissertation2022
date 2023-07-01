from turtle import screensize
import numpy as np

# 情景的路径
scene_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/mapf-scen-even/scen-even/Berlin_1_256-even-1.scen"


def generate_launch_description():
    # 这就相当于main，这里面的print也会执行的
    pass


def load_scene(scene_path):
    '''
    从情景文件中读入各项信息

    Args:
        scene_path (str): 情景文件的绝对路径

    Returns:
        map_name (str): 地图的文件名

        map_size (tuple): 地图的宽高

        bucket_number (int): 情景中的哪一组

        starts ([tuple]): 起点们 [(起点1),(起点2)，。。。]

        goals ([tuple]): 终点们 [(终点1),(终点2)，。。。]

        optimal_dist ([int]): 最优距离们。 

        - 最优长度假设为对角线代价的sqrt（2）
        - 最优长度假设节点不能cut corners through walls.
    '''
    # 忽略第一行（version信息），将每一行加载为一个元组
    scene_data = np.genfromtxt(
        scene_path, delimiter='\t', dtype=None, encoding='utf-8', skip_header=1)
    map_name = scene_data[0][1]
    map_size = (scene_data[0][2], scene_data[0][3])

    # 将数据按bucket顺序排列，并去除地图名称和地图宽高
    ordered_scene_data = []
    for item in scene_data:
        # 滤除地图名称，地图宽，地图高
        # 剩余的数据：[bucket, 起始x，起始y，终止x，终止y，最优距离]
        ordered_scene_data.append(
            [item[0], item[4], item[5], item[6], item[7], item[8]])

    buckets = set([item[0] for item in ordered_scene_data])  # 桶的编号组

    bucket_number = input(
        "此情景文件中包含%d个在同一地图中的问题集，要选择哪一个？（编号从0开始）" % len(buckets))

    bucket_number = int(bucket_number)

    filtered_scene_data = []

    # 滤出属于同一bucket组的数据
    for _ in ordered_scene_data:
        if _[0] == bucket_number:
            filtered_scene_data.append(_)

    starts = [] # 起点
    goals = [] # 终点
    optimal_dist = [] # 最优距离

    for _ in filtered_scene_data:
        starts.append((_[1], _[2]))
        goals.append((_[3], _[4]))
        optimal_dist.append(_[5])

    if len(starts)!=len(set(starts)):
        print("起点有重复")
    if len(goals)!=len(set(goals)):
        print("终点有重复")

    return map_name, map_size, bucket_number, starts, goals, optimal_dist

def main():
    load_scene(scene_path=scene_path)


if __name__ == "__main__":
    main()
