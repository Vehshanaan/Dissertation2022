import rclpy

from rclpy.node import Node

from interfaces.msg import Slot

from interfaces.srv import ApplyForSending


# 给stdma通信层的信道topic的名字
name_for_stdma_channel = "STDMA_Channel"


class Site(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("站点启动！此节点的名字是%s" % self.get_name())

        # 话题接收者部分
        self.received_msg = Slot()
        self.subscriber_ = self.create_subscription(
            Slot, name_for_stdma_channel, self.subscriber_callback, 10)
        
        # 一些参数和标志位

        # 已加入网络？
        self.joined_ = False 
        

    # 从stdma通信层信道topic接收到信息时运行的回调函数
    def subscriber_callback(self, msg):
        self.received_msg = msg
        self.get_logger().info("msg received: slot %d/%d from site %d." %
                               (self.received_msg.slot_no, self.received_msg.slot_total, self.received_msg.sender_no))

        # 保存收到的信道信息
        self.frame_length_ = msg.slot_total
        self.current_slot_ = msg.slot_no
        if not hasattr(self,"occupied_"):
            self.occupied_ = [-1]*self.frame_length_

        self.occupied_[self.current_slot_-1] = msg.occupied

    
        

def main(args=None):

    rclpy.init(args=args)

    site = Site("NodeNameHere")

    site.join_network()

    rclpy.spin(site)

    rclpy.shutdown()
