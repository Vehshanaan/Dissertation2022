import rclpy

from rclpy.node import Node

def main(args=None):

    rclpy.init()
    NodeInstance = Node("node_name")
    NodeInstance.get_logger().info("这是此节点启动时产生的一行日志输出")
    rclpy.spin(NodeInstance)
    rclpy.shutdown()
