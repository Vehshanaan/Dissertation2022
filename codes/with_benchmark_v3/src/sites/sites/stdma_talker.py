
from zoneinfo import available_timezones
from blinker import receiver_connected

from rclpy.logging import LoggingSeverity
import sys  # 为了导入同目录的工具箱
import os
import random
import time
from numpy import outer
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Bool, Int32MultiArray

# 导入工具箱
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
if current_dir:
    import utils
    import path_finder


class StdmaTalker(Node):

    def __init__(self):
        self.node_id = os.getpid()  # 此方法返回的是一个int
        random.seed(self.node_id)  # 从可用slot中随机挑选slot的时候会用到这个
        super().__init__("stdma_talker_%d" % self.node_id)

        # 尽可能少显示控制台日志信息。设置级别以下的东西不会被打印出来 例程见https://github.com/ros2/rclpy/blob/humble/rclpy/test/test_logging.py
        # 可以在继承此节点的节点类初始化函数中修改此等级，使其发送全部消息
        self.get_logger().set_level(LoggingSeverity.WARN)

        self.frame = 0  # 帧计数
        self.slot = -1  # 当前所处的slot，每次end_slot_callback中会修改这个

        # 从外部初始化帧长度
        num_slots = 10
        self.declare_parameter("num_slots", num_slots)
        self.num_slots = self.get_parameter(
            "num_slots").get_parameter_value().integer_value

        # 状态机状态
        self.state = "listen"
        self.my_slot = -2  # 自己的slot编号
        self.slot_allocations = [None]*self.num_slots  # 槽位分配记录列表
        self.inbox = []

        # 从外部初始化地图大小
        self.declare_parameter("map_size", [1, 1])
        map_size = self.get_parameter(
            "map_size").get_parameter_value().integer_array_value
        self.map_size = tuple(list(map_size))

        # 初始化地图
        self.declare_parameter("map_path", "_")
        map_path = self.get_parameter(
            "map_path").get_parameter_value().string_value
        self.map = utils.map_load(map_path, self.map_size)

        # 初始化起点
        start = (-1, -1)
        self.declare_parameter("start", start)
        self.start = self.get_parameter(
            "start").get_parameter_value().integer_array_value
        self.start = tuple(self.start.tolist())

        # 初始化终点
        goal = (-1, -1)
        self.declare_parameter("goal", goal)
        self.goal = self.get_parameter(
            "goal").get_parameter_value().integer_array_value
        self.goal = tuple(self.goal.tolist())

        # 是否已经成功进入地图？
        self.jumped_in = False

        # 初始化自身位置
        self.position = self.start

        # 信道分配的话题
        self.control_sub = self.create_subscription(
            Int32, 'stdma/control', self.control_callback, 10)
        self.control_pub = self.create_publisher(Int32, 'stdma/control', 10)

        # 传输自身计划的话题
        self.message_pub = self.create_publisher(
            Int32MultiArray, "stdma/message", 10)
        self.message_sub = self.create_subscription(
            Int32MultiArray, "stdma/message", self.message_callback, 10)

        # 时钟
        self.timer_sub = self.create_subscription(
            Bool, "stdma/timer", self.timer_callback, 10)

        # 用于测算半槽时长的时间戳
        self.time_stamp = -1

        # 半槽长度保存变量
        self.half_slot_length = -1

        # 寻路机
        self.path_finder = path_finder.PathFinder(
            self.map, self.num_slots, self.start, self.goal)

    def slot_length_update(self, time):
        '''
        每半槽调用一次，更新半槽时长

        Args:
            time (float): time.time()
        '''
        if self.time_stamp == -1:  # 如果时间戳未初始化过：初始化时间戳
            self.time_stamp = time
        else:
            diff = time-self.time_stamp  # 计算时间差
            if self.half_slot_length == -1:  # 如果时间差还没被初始化过：初始化
                self.half_slot_length = diff
            else:
                self.half_slot_length = self.half_slot_length*0.9+diff*0.1  # 使用滑动平均值方法记录时间差
            self.time_stamp = time  # 更新时间戳

    def control_callback(self, msg):
        '''
        用来分享信道占用情况(槽位使用权)的STDMA话题
        '''
        self.inbox.append(msg)

    def message_callback(self, msg):
        '''
        传输计划的stdma话题, 传输时机根据信道分配而决定
        '''
        node_id, data = utils.plan_decompressor(msg.data)
        if node_id == self.node_id:
            return  # 如果是自己发的：跳过，不保存接收到的信息
        else:
            '''
            # 如果计划不够长：用计划最后一位补齐长度
            if len(data) < self.num_slots:
                data += [data[-1]]*(self.num_slots-len(data))
                self.get_logger().fatal("补长后的计划："+str(data))
            self.inbox_plan[node_id] = data  # 保存到计划存储变量里
            '''
            self.path_finder.receive_plan(node_id, data)  # 保存收到的计划
            

        # self.get_logger().warn("收到的计划："+str(self.path_finder.others_plans)+"\n实际我的计划："+str(self.path_finder.published_plan))


    def get_messages(self):
        '''
        将self.inbox中的信息逐个弹出，构成新的列表并返回新列表
        '''
        received_messages = []
        num_messages = len(self.inbox)
        for ii in range(num_messages):
            received_messages.append(self.inbox.pop(0))
        return received_messages

    def timer_callback(self, msg):

        self.slot_length_update(time.time())  # 更新半槽时间记录

        if msg.data:
            # 上升沿，是slot的开始或结束
            self.end_slot_callback()
        else:
            # 下降沿，是slot的中间
            self.mid_slot_callback()

    def mid_slot_callback(self):
        if self.slot >= 0:  # 防止刚初始化的节点掺和进这里头
            if self.slot == self.my_slot:
                msg = Int32()
                msg.data = self.node_id
                self.control_pub.publish(msg)  # 发送信道占有信息

                '''
                # 如果有计划且计划不空且状态为in:   
                if hasattr(self, "plan") and self.plan and self.state == "in":
                    msg = Int32MultiArray()
                    msg.data = utils.plan_compressor(
                        self.node_id, self.plan[:self.num_slots])
                    self.message_pub.publish(msg)
                '''

                # 该裁剪计划了
                if self.state == "in":
                    self.plan = self.path_finder.cut_plan(2*self.num_slots)
                    if self.plan:
                        self.jumped_in = True
                        #self.get_logger().fatal("我切下来的计划：%s" % str(self.plan))
                    else:
                        self.get_logger().fatal("啥也没切下来")

                # 若有计划: 发送计划
                if hasattr(self, "plan") and self.plan and self.state == "in":
                    msg = Int32MultiArray()
                    msg.data = utils.plan_compressor(self.node_id, self.plan)
                    self.message_pub.publish(msg)

                self.state = "check"  # 每次发送完都检查我这一槽是不是只有我说话，来更新自己对槽的占有状态

    def end_slot_callback(self):

        if self.slot == -1:
            # 初次进入此函数
            self.slot = 0  # 从-1变回0

        else:
            received_message = self.get_messages()  # 清空收到的信道控制信息并转存
            num_messages = len(received_message)  # 检查在过去槽里一共收到几条信息

            # 如果啥也没收到：槽空
            if num_messages == 0:
                self.slot_allocations[self.slot] = None  # 登记本槽为空
            # 如果本槽内只收到一条信息：槽有主人了
            elif num_messages == 1:
                msg = received_message[0]  # 就一条
                sender = msg.data
                self.slot_allocations[self.slot] = sender  # 登记槽归谁
                if sender == self.node_id:  # 如果是我发的：
                    self.state = "in"  # 说明我成功搞到一个槽，我入网了
            elif num_messages > 1:  # 如果槽内收到多条信息:大撞车
                colliding_ids = [m.data for m in received_message]  # 撞车的哥几个都是谁
                self.slot_allocations[self.slot] = None  # 由于发生了撞车，没人拥有此槽
                if self.node_id in colliding_ids:  # 如果哥们自己也撞了：
                    self.state = "listen"  # 回到听的状态
                    self.my_slot = -2
            if self.state == "check":
                # 如果自己已经入网，发过消息，但此时没有接收到自己的消息，也没有发生碰撞：肯定是传丢了
                self.state = "listen"
                self.my_slot = -2  # 重听吧

            # 更新槽和帧的编号
            self.slot += 1
            if self.slot == self.num_slots:  # 如果听过一整帧
                self.slot = 0
                self.frame += 1
                if self.state == "listen":  # 如果听过一整帧之后，我是待加入状态：找一个眼儿
                    available_slots = [ii for ii in range(
                        self.num_slots) if self.slot_allocations[ii] == None]
                    if available_slots:  # 没有可供选择的自由槽位的话，就算了，啥也不干
                        self.state = "enter"
                        self.my_slot = random.sample(available_slots, 1)[0]
                        self.get_logger().info('Will try to enter at slot %d' % self.my_slot)
                    else:
                        self.my_slot = -2

            # 每次槽结束：寻路机时间+1, 还有一大堆别的处理
            self.path_finder.slot_end()

            # 更新自身位置
            if hasattr(self, "plan") and self.plan:
                self.position = self.plan.pop(0)
                if self.position == self.goal:
                    self.destroy_node()  # 如果已经到达终点：消灭自己

            # 如果是初次：先初始化寻路器的堆
            if self.slot == self.my_slot and self.state == "in" and not self.jumped_in:
                self.path_finder.init()
            # 谋
            time_left = self.half_slot_length - \
                (time.time()-self.time_stamp)  # 剩余时间
            self.path_finder.connive(time_left)


def main(args=None):

    rclpy.init(args=args)

    stdma_talker = StdmaTalker()

    rclpy.spin(stdma_talker)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    stdma_talker.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
