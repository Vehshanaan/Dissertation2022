from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

# 不能用os当场获取的路径，因为这玩意儿编译其实就是一个搬运，搬到别的文件路径下运行。所以要把路径写死
import sys
parent_dir = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/stdma_with_benchmark_v1/src/sites"
sys.path.append(parent_dir)

from utils.utils import scene_reader



scene_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/generated_scenes/Berlin_0_256.png10nodes1688462793.0501769"

def generate_launch_description():
    package_name = "sites"

    # 定义启动描述符
    ld = LaunchDescription()

    # 读取情境
    node_number, map_path, map_size, starts, goals = scene_reader(scene_path=scene_path)

    # 启动地图节点
    activate_map = Node(
        package = package_name,
        executable="map",
        parameters=[{"map_path":map_path, "map_size":map_size}],
    )
    ld.add_action(activate_map)

    # 启动信道可视化节点
    activate_channel = Node(
        package=package_name,
        executable="channel_visualiser",
        parameters=[{"num_slots":node_number}]
    )
    ld.add_action(activate_channel)

    # 启动若干给定起始位置和终点的节点
    for i in range(len(starts)):
        start = starts[i]
        goal = goals[i]
        activate_site = Node(
            package=package_name,
            executable="site",
            parameters=[{"num_slots":node_number, "start":start, "goal":goal, "map_path":map_path, "map_size":map_size}]
        )
        ld.add_action(activate_site)

    # 启动timer

    activate_timer=Node(
        package=package_name,
        executable="timer"
    )
    ld.add_action(activate_timer)


    return ld

def main():

    # 加载情景设置档
    node_number, map_path, map_size,  starts, goals = scene_reader(scene_path=scene_path)

    print(node_number)


    package_name = "sites"

    # 定义Launch描述符

if __name__ == "__main__":
    main()

