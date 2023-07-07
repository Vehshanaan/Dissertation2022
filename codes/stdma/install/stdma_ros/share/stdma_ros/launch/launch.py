from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = "stdma_ros"

    ld = LaunchDescription()

    activate_timer = Node(
        package=package_name,
        executable="timer"
    )

    ld.add_action(activate_timer)

    for i in range(100):
        activate_site = Node(
            package=package_name,
            executable="talker",
            arguments=['--ros-args', '--log-level', 'FATAL']
        )
        ld.add_action(activate_site)
    
    return ld
