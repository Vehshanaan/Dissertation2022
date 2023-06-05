import rclpy

from rclpy.node import Node

from interfaces.msg import Slot

from interfaces.srv import ApplyForSending


class Channel(Node):
    '''
    用作信道的节点
    '''

    def __init__(self, name):
        super().__init__(name)

        # 初始化一系列参数

        # 一帧中含有多少个槽
        self.frame_length_ = 5

        # 当前播放的是帧中的哪个槽。此值正常为1~frame_length
        self.current_slot_ = 1

        # slot的被占用情况：
        self.occupation_ = [-1]*self.frame_length_  # 初始化均为-1（未被占用）

        # 当前帧要发送的信息
        self.msg_for_this_slot_ = Slot()

        # 申请使用当前槽的节点数，用作冲撞判断
        self.applicant_amount_for_current_slot_ = 0

        # 从节点接收数据的功能初始化（初始化服务器站点）

        # 是否可以广播下一个slot了
        self.next_slot_ready_ = False

        # 向节点广播数据的功能初始化（初始化话题发送端站点）
        self.publisher_ = self.create_publisher(Slot, "STDMA_Channel", 10)

        # 初始化槽位申请服务器
        self.apply_for_slot_server_ = self.create_service(
            ApplyForSending, "ApplyForSending", self.apply_sending_callback)

        # 检查下一slot是否可以广播的时间间隔
        self.check_slot_ready_period_ = 1  # 默认1秒。快点好，好啊。

        # 定时广播下一槽信息
        self.timer_ = self.create_timer(
            self.check_slot_ready_period_, self.broadcast)

        self.get_logger().info("信道已打开。此信道中一帧有%d个槽" % self.frame_length_)

    def apply_sending_callback(self, request, response):
        '''
        节点申请在某一槽发送数据的服务函数

        Returns:
            bool : 成功了吗
        '''
        if self.occupation_[request.apply_slot-1] != request.applicant:
            self.get_logger().info("收到来自节点%d的申请：申请slot %d" %
                                   (request.applicant, request.apply_slot))
        else:
            self.get_logger().info("收到来自节点%d的数据：在slot %d 发送 %s " %
                                   (request.applicant, request.apply_slot, request.data))

        # 每次收到申请，增加一个申请人计数器
        self.applicant_amount_for_current_slot_ += 1

        # 卡在这里了。spin_once如果没有接到东西的话会无限地等下去

        # 看看半秒内有没有接到新的服务请求
        # rclpy.spin_once(self, timeout_sec=0.5)

        if self.applicant_amount_for_current_slot_ != 1:  # 如果有多个申请者要在下一槽发信息
            # 告诉申请者发生了冲撞
            response.result = False
            # 直接返回，结束函数
            return response

        else:
            response.result = True  # 不然就是申请成功了

        # 记录申请者信息和要发送的数据

         # 记录此槽归谁
        self.occupation_[request.apply_slot-1] = request.applicant

        # 记录要发送的信息
        pass

        self.next_slot_ready_ = True  # 准备好发送下一槽的信息，可以发送了

        return response

    def broadcast(self):
        '''
        向信道话题中发送消息的回调函数。此函数是timer的回调函数，每隔一段时间就检查一下是不是该发下一条了。
        '''
        if (not self.next_slot_ready_) and (self.occupation_[self.current_slot_-1] != -1):
            self.next_slot_ready_ = False
            print("还没收到该收到的此节点信息")
            return  # 如果还没准备好发送：不发送，直接返回

        # 初始化要广播的信息
        msg = Slot()
        msg.slot_no = self.current_slot_
        msg.slot_total = self.frame_length_
        msg.sender_no = self.occupation_[self.current_slot_-1]

        # 根据occupation记录判断信息中被占用标志位的值
        if self.occupation_[self.current_slot_-1] != -1:
            msg.occupied = True
        else:
            msg.occupied = False

        # 发送信息
        self.publisher_.publish(msg)
        self.get_logger().info("%d/%d,此槽的被占用情况是%s" % (self.current_slot_,
                                                      self.frame_length_, self.occupation_[self.current_slot_-1]))

        self.next_slot_ready_ = False  # 每次发送后重置就绪标示符
        self.applicant_amount_for_current_slot_ = 0  # 重置申请人数目
        self.current_slot_ += 1  # 往后捯一个槽
        if self.current_slot_ > self.frame_length_:
            self.current_slot_ = 1


def main(args=None):

    rclpy.init(args=args)

    ChannelInst = Channel("ChannelNameHere")

    rclpy.spin(ChannelInst)

    rclpy.shutdown()
