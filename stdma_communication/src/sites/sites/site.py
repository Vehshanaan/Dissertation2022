import rclpy

from rclpy.node import Node


class Site(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("站点启动！此节点的名字是%s" % self.get_name())



        if (self.get_name() == "node1"):
            pass
            # 如果是一号节点，那kick start一下，直接让他进入网络，发消息，不然网络里啥也没有，没法开始


def main(args=None):

    rclpy.init()

    site = Site("NodeNameHere")

    rclpy.spin(site)

    rclpy.shutdown()
