import rclpy

from rclpy.node import Node

from interfaces.msg import Slot

from interfaces.srv import ApplyForSending

import random


# 给stdma通信层的信道topic的名字
name_for_stdma_channel = "STDMA_Channel"

not_joined = -100


class Site(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("站点启动！此节点的名字是%s" % self.get_name())

        # 话题接收者部分
        self.received_msg = Slot()
        self.subscriber_ = self.create_subscription(
            Slot, name_for_stdma_channel, self.subscriber_callback, 10)

        # 向信道申请位置部分
        self.client_apply_slot_ = self.create_client(
            ApplyForSending, "ApplyForSending")

        # 一些参数和标志位

        # 此节点的槽位编号是
        self.slot_no_ = not_joined  # not_joined = -100 代表还未加入网络

    # 在获得位置后向信道发送消息用的函数
    def apply_for_sending(self,data):
        # 当信道还不在线的时候，打印一个不在线
        while not self.client_apply_slot_.wait_for_service(1):
            self.get_logger().warn("信道还没开，信道还没开")

        # 构造请求的内容
        request = ApplyForSending.Request()
        request.applicant = int(self.get_name()[-1])
        request.apply_slot = self.slot_no_
        request.data = data

        # 发送请求
        self.client_apply_slot_.call_async(request)



    # 从stdma通信层信道topic接收到信息时运行的回调函数
    def subscriber_callback(self, msg):
        self.received_msg = msg
        #self.get_logger().info("msg received: slot %d/%d from site %d." %
        #                       (self.received_msg.slot_no, self.received_msg.slot_total, self.received_msg.sender_no))

        # 保存收到的信道信息
        self.frame_length_ = msg.slot_total
        self.current_slot_ = msg.slot_no
        if not hasattr(self, "occupied_"):
            self.occupied_ = [-1]*self.frame_length_

        self.occupied_[self.current_slot_-1] = msg.occupied

        # 当轮到自己说话的时候，说话。
        if not hasattr(self, "slot_no_"):
            return
        if (self.current_slot_ == self.slot_no_ - 1) or (self.slot_no_ == 1 and self.current_slot_ == self.frame_length_):
            # 轮到自己了，说话。
            self.apply_for_sending("我是"+str(self.get_name()))


    # 用来申请加入网络
    def apply_for_slot(self, slot_desired):

        # 当信道还不在线的时候，打印一个不在线
        while not self.client_apply_slot_.wait_for_service(1):
            self.get_logger().warn("信道还没开，信道还没开")

        # 构造请求的内容

        request = ApplyForSending.Request()
        request.applicant = int(self.get_name()[-1])
        request.apply_slot = slot_desired

        # 发送请求
        future = self.client_apply_slot_.call_async(request)
        rclpy.spin_until_future_complete(self, future)  # 等待服务完成

        # 返回申请结果
        if future.result() is not None and future.result().result:
            return True
        else:
            return False

    # 应在main里调用。在spin以前。 加入网络的函数。
    def join_network(self):

        # 先检查自己是否已经加入网络，若已加入则直接return
        if self.slot_no_ != not_joined:
            return

        # 先听一帧。
        while 1:

            # 一直听
            rclpy.spin_once(self)

            # 如果还没听够一帧：再听。
            if not hasattr(self, "occupied_"):
                continue
            if -1 in self.occupied_:
                continue

            # 如果已经听够一帧，结束听的阶段
            break

        # 随机找一个自己可以用的槽位
        candidates = [
            i+1 for i in range(len(self.occupied_)) if self.occupied_[i] == False]
        apply_for = random.choice(candidates)

        # 申请此槽位
        # 等到该自己说话的时候
        while not hasattr(self, "current_slot_"):
            rclpy.spin_once(self)
        # 只要还没加入，就一直试着加入
        while self.slot_no_ == not_joined:

            rclpy.spin_once(self)  # 听一下信道

            # 等待轮到自己
            if (self.current_slot_ == apply_for - 1) or (apply_for == 1 and self.current_slot_ == self.frame_length_):
                # 申请槽位
                success = self.apply_for_slot(apply_for)
                if success:
                    self.slot_no_ = apply_for
                    return success
                else:
                    # 随机换一个自己可以用的槽位
                    candidates = [
                        i+1 for i in range(len(self.occupied_)) if self.occupied_[i] == False]
                    apply_for = random.choice(candidates)


def main(args=None):

    rclpy.init(args=args)

    site = Site("node1")

    site.join_network()

    rclpy.spin(site)

    rclpy.shutdown()
