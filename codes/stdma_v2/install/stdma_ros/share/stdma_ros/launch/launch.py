# 测试多个信道同时运行时是否会出问题的启动脚本
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    package_name = "stdma_ros"

    # 定义Launch描述符
    ld = LaunchDescription()

    activate_timer = Node(
        package=package_name,
        executable="timer",
    )
    ld.add_action(activate_timer)
    for _ in range(10):
        action = Node(
            package=package_name,
            executable="talker",
        )
        ld.add_action(action)
    return ld
