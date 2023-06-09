import rclpy

from rclpy.node import Node

class MyNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("此节点的名字是：%s" % self.get_name())

def main(args=None):
    rclpy.init(args=args)
    MyOOPNode = MyNode("Name_Node_Here")
    rclpy.spin(MyOOPNode)
    rclpy.shutdown()