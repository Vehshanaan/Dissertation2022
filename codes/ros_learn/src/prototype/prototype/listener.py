import rclpy

from rclpy.node import Node

# 导入话题消息类型
from std_msgs.msg import String


class MySubscriber(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("话题订阅者节点成功启动")

        self.receivedMsg = ""  # 存储收到的信息

        self.listen = self.create_subscription(
            String, "huati", self.callback4listener, 10)  # 决定订阅什么话题，信息什么格式，收到后干啥（执行callback）

    def callback4listener(self, msg):  # callback函数
        self.receivedMsg = msg.data
        self.get_logger().info("收到了如下讯息：%s" % self.receivedMsg)


def main(args=None):

    rclpy.init(args=args)
    talker = MySubscriber("Subscriber_Name_Here")

    rclpy.spin(talker)
    rclpy.shutdown()
