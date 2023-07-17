# from launch import LaunchDescription

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

# 注意，地图和场景都在这里设置，**记得设置成成对的！！！，没法设计代码级别的防呆匹配！自己记得用好，不要犯傻**
map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_1_256.png"
scene_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-scen/Berlin_1_256.map.scen"


def generate_launch_description():

    package_name = "sites"

    # 启动描述符
    ld = LaunchDescription()

    # 启动地图
    map = Node(
        package=package_name,
        executable="map",
        parameters=[
            {
                "map_path": map_path,  # 地图文件绝对路径
                "scene_path": scene_path,  # 场景文件绝对路径
                "num_slots": 10,  # 信道帧长度
            }
        ]
    )
    ld.add_action(map)

    # 启动信道可视化
    channel_visualiser = Node(
        package=package_name,
        executable="channel_visualiser",
        parameters=[
            {
                "num_slots": 10,  # 信道帧长度
                "map_path": map_path,  # 地图路径，实际上对于可视化节点用不到, 写上只是为了防止读图空路径报错
            }
        ]
    )

    ld.add_action(channel_visualiser)

    # 启动节点
    # 为各个节点读取起点和终点
    starts, goals = scene_reader(scene_path)

    # 启动节点
    node_amount = 15
    for i in range(node_amount):
        print("起点-终点对："+str(starts[i])+" - "+str(goals[i]))
        site = Node(
            package=package_name,
            executable="talker",
            parameters=[
                {
                    "num_slots": 10,  # 信道帧长度
                    "map_path": map_path,  # 地图路径
                    "start": starts[i],  # 起点位置
                    "goal":goals[i],  # 终点位置
                }
            ]
        )

        ld.add_action(site)

    # 启动timer
    timer = Node(
        package=package_name,
        executable="timer"
    )
    ld.add_action(timer)

    return ld


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


def main():
    starts, goals = scene_reader()



if __name__ == "__main__":
    main()
