import rclpy

from rclpy.node import Node

from prototype_interfaces.msg import Prototype


class customMsgNode(Node):
    def __init__(self, name):
        # 初始化部分
        super().__init__(name)
        self.get_logger().info("这是此节点被启动时自动发送的一条信息，此节点的名字为%s。" % self.get_name())

        # 话题发送者部分
        self.publisher_ = self.create_publisher(Prototype, 'huati', 10)
        self.timer_period = 2
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.i = 0

        # 话题接受者部分
        self.receivedMsg = Prototype()
        self.subscriber_ = self.create_subscription(
            Prototype, 'huati', self.subscriber_callback, 10)

    def subscriber_callback(self, msg):
        self.receivedMsg = msg
        self.get_logger().info("收到了如下信息：%s" % self.receivedMsg.content.data)

    def timer_callback(self):
        msg = Prototype()
        msg.content.data = str(self.i)
        self.publisher_.publish(msg)
        self.get_logger().info("发送了以下信息：%s" % msg.content.data)
        self.i += 1


def main(args=None):
    rclpy.init()

    customMsgTestNode = customMsgNode("NameNodeHere")

    rclpy.spin(customMsgTestNode)

    rclpy.shutdown()
