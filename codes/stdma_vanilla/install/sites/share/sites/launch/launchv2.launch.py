import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        yaml_content = yaml.safe_load(file)
        return yaml_content


def generate_launch_description():

    package_name = "sites"
    yaml_file_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/stdma_vanilla/src/sites/launch/coordinates.yaml"  # 替换为你的YAML文件路径

    yaml_params = read_yaml_file(yaml_file_path)

    # 定义launch描述符
    ld = LaunchDescription()

    # 启动地图
    activate_map = Node(
        package=package_name,
        executable="map",
        name="map",
    )

    # 启动地图可视化
    activate_map_visualiser = Node(
        package=package_name,
        executable="map_visualiser",
        name="map_visualiser",
    )

    # 启动信道
    activate_channel = Node(
        package=package_name,
        executable="channel",
        name="channel",
    )

    # 启动信道可视化
    activate_channel_visualiser = Node(
        package=package_name,
        executable="visualiser",
        name="channel_visualiser",
    )

    ld.add_action(activate_map)
    ld.add_action(activate_map_visualiser)
    ld.add_action(activate_channel)
    ld.add_action(activate_channel_visualiser)

    # 启动站点
    for node_name, params in yaml_params.items():
        # 获取文件中设定的横纵坐标
        start_x = params["start_x"]
        start_y = params["start_y"]
        target_x = params["target_x"]
        target_y = params["target_y"]

        # 创建节点
        activate_sites = Node(
            package=package_name,
            executable="site",
            name=node_name,
            parameters=[{"start_x": start_x, "start_y": start_y,
                         "target_x": target_x, "target_y": target_y}],
        )

        ld.add_action(activate_sites)

    return ld
