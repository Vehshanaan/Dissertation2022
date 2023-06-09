import rclpy

from rclpy.node import Node

from std_msgs.msg import String  # 1. 导入要使用的消息类型


class MyPublisher(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("这是此节点被启动时自动发送的一条信息，此节点的名字为%s。" % self.get_name())

        # 2. 声明并创建发布者
        # 信息格式，话题名称，QoS_profile 详见http://docs.ros.org/en/humble/Concepts/About-Quality-of-Service-Settings.html
        self.talk = self.create_publisher(String, "huati", 10)

        # 创建一个用于定时复读的timer，每当时间到的时候，timer就会调用callback的函数
        # 创建timer周期
        self.timer_period = 2  # 每两秒触发一下timer
        self.timer = self.create_timer(self.timer_period, self.callback4timer)

        self.counter = 0  # 一会发送消息要用的本地计数器

    # 写一个给timer用的回调函数
    def callback4timer(self):  # 写self代表是类的成员函数
        msg = String()  # 实例化String对象
        msg.data = "这是第%d条信息。" % self.counter
        self.talk.publish(msg)  # 发布msg
        self.get_logger().info("刚刚发布了一条信息：\" 这是第%d条信息。\' " % self.counter)

        self.counter += 1  # 自增计数器


def main(args=None):
    rclpy.init(args=args)
    talker = MyPublisher("Publisher_Name_Here")

    rclpy.spin(talker)

    rclpy.shutdown()
