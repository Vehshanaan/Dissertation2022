from launch import LaunchDescription

from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="sites",
            namespace="sites",
            executable="site",
            name="node1",
        ),
        Node(
            package="sites",
            namespace="sites",
            executable="site",
            name="node2",
        )
    ])