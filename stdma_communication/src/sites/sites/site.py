import rclpy

from rclpy.node import Node

from interfaces.msg import Slot

import time

# 给stdma通信层的信道topic的名字
name_for_stdma_channel = "channel"

# 定义帧长度
frame_length = 5  # 1个frame = 5 slots, slot编号为1~5


class Site(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("站点启动！此节点的名字是%s" % self.get_name())

        # 话题发布者部分：
        self.publisher_ = self.create_publisher(
            Slot, name_for_stdma_channel, 10)

        # 话题接收者部分
        self.received_msg = Slot()
        self.subscriber_ = self.create_subscription(
            Slot, name_for_stdma_channel, self.subscriber_callback, 10)

        # 导入帧长度
        self.frame_length = frame_length

        # 关于信道信息的记录

        network_inited = self.is_network_inited(5)

        # 如果网络没有初始化：
        if not network_inited:
            # 发送网络中的第一条信息
            pass
        else:
            # 记录信息
            pass



    def is_network_inited(self, timeout):
        """
        检测stdma信道中是否有成员。超过时间限制还没听见人说话则认定为false

        Args:
            timeout : 超时时长（秒），超过此时长还是啥也没听见则返回False

        Returns:
            bool: 有没有成员
        """

        result = rclpy.spin_once(self, timeout_sec=timeout)

        return result

    # 从stdma通信层信道topic接收到信息时运行的回调函数

    def subscriber_callback(self, msg):
        self.received_msg = msg
        self.get_logger().info("msg received: slot %d/%d from site %d." %
                               (self.received_msg.slot_no, self.received_msg.slot_total, self.received_msg.sender_no))


def main(args=None):

    rclpy.init(args=args)

    site = Site("NodeNameHere")

    site.join_network()

    rclpy.spin(site)

    rclpy.shutdown()
