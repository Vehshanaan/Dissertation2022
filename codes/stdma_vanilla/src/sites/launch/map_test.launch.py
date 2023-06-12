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
    package_name = 'sites'  # 替换为你的包名
    yaml_file_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/stdma_vanilla/src/sites/launch/coordinates.yaml"  # 替换为你的YAML文件路径

    yaml_params = read_yaml_file(yaml_file_path)

    # 定义launch描述符
    ld = LaunchDescription()

    node_action = Node(
        package=package_name,
        executable="map",
        name="map_node",
    )

    ld.add_action(node_action)

    for node_name, params in yaml_params.items():
        # 获取横纵坐标参数
        x = params['x']
        y = params['y']

        # 创建一个节点启动动作
        node_action = Node(
            package=package_name,
            executable='test_site',  # 替换为你的节点可执行文件
            name=node_name,
            parameters=[{'x': x, 'y': y}]
        )

        # 将节点启动动作添加到launch描述符中
        ld.add_action(node_action)

    return ld
