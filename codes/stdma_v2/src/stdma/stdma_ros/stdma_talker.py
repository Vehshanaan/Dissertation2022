# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
stdma通讯节点的代码，这个只管通讯
'''

from PIL import Image  # 读取地图用的
from std_msgs.msg import Int32, Bool, Int32MultiArray
from rclpy.node import Node
import rclpy
from numpy import outer
import random
import os
from rclpy.logging import LoggingSeverity

import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
from path_finding import find_path  # 导入寻路的函数


# 地图的绝对文件路径
map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/map_builder/map2.png"


def map_reader(map_path = map_path) -> list[list]:
    '''
    将地图图片读取为二维数组的函数

    Args:
        map_path (string): 地图图片的路径，编写此函数时用的是绝对路径。不推荐相对路径，因为ros2功能包里的src路径不太适合放图片吧 

    Returns:
        list: 二维数组，其中地图图片中白色的地方是True，黑色像素的地方是False
    '''
    with Image.open(map_path) as img:
        width, height = img.size
        pixels = img.load()
        bool_array = [[False for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if pixels[j, i] == (255, 255, 255):  # 如果像素为全白：
                    bool_array[i][j] = True
        return bool_array


def spawn_pos_generate(pid, map) -> list:
    '''
    返回一个位于地图边界外一圈不包含四角的起始位置。

    Args:

        pid (int): os.getpid()

        map (list): 详见地图加载函数。


    Returns:
        list: [横坐标，纵坐标]，注意其中的值可能为负。初始寻路的时候需要注意。
    '''

    # 生成地图外围一圈除四角位置的坐标的列表：
    map_width = len(map[0])
    map_height = len(map)

    outer_boundary = []  # 外围坐标

    # 将外围点一个个填进外围坐标列表里去
    for col in range(map_width):
        outer_boundary.append([col, -1])
        outer_boundary.append([col, map_height])
    for row in range(map_height):
        outer_boundary.append([-1, row])
        outer_boundary.append([map_width, row])

    # 用进程id选取一个唯一的外围点
    index = pid % len(outer_boundary)

    return outer_boundary[index]


def plan_compressor(plan2d) -> list:
    '''
    将[节点id,[x1,y1],[x2,y2],...]格式的二维数组压缩成一维的函数

    Args:
        plan (list[list]): [[x1,y1],[x2,y2],...]格式的二维数组

    Returns:
        result: 格式为[x1,y1,x2,y2,...]的一维数组
    '''
    if not plan2d:  # 如果输入为空列表
        return []  # 返回空列表
    else:
        plan1d = []
        for _ in plan2d:
            plan1d.append(_[0])
            plan1d.append(_[1])

    return plan1d


def plan_decompressor(plan1d) -> list[list]:
    '''
    将格式为[节点id,x1,y1,x2,y2...]格式的数组还原为[[x1,y1],[x2,y2],...]

    Args:
        plan1d (list): [x1,y1,x2,y2...]格式的一维数组

    Returns:
        plan2d: [[x1,y1],[x2,y2],...]格式的二维数组
    '''
    if not plan1d:
        return [[]]  # 如果输入为空，返回空
    else:
        plan2d = []
        for i in range(0, len(plan1d), 2):
            plan2d.append((plan1d[i], plan1d[i+1]))
    return plan2d


class StdmaTalker(Node):

    def __init__(self):
        self.node_id = os.getpid()  # 返回一个int, 是操作系统分配的每个进程唯一的标识符
        random.seed(self.node_id)

        super().__init__('stdma_talker_%d' % self.node_id)

        # 尽可能少显示控制台日志信息。设置级别以下的东西不会被打印出来 例程见https://github.com/ros2/rclpy/blob/humble/rclpy/test/test_logging.py
        # 可以在继承此节点的节点类初始化函数中修改此等级，使其发送全部消息
        self.get_logger().set_level(LoggingSeverity.WARN)

        self.frame = 0  # 帧计数
        self.slot = -1  # 当前所处的slot。站点初始化时这是-1，此变量的修改详见self.end_slot_callback
        self.num_slots = 10  # 帧长度
        self.state = 'listen'
        self.my_slot = -2
        self.slot_allocations = [None]*self.num_slots  # 初始化槽位分配情况保存列表
        self.inbox = []
        self.inbox_plan = []  # 储存别人发过来的计划

        # 初始化关于地图和移动的一些东西
        self.move_pub = self.create_publisher(
            Int32MultiArray, "stdma/move", 10)
        self.map = map_reader(map_path=map_path)  # 加载地图
        self.position = spawn_pos_generate(
            self.node_id, self.map)  # 根据进程pid获得一个唯一的起始位置。[横坐标，纵坐标]
        
        # 告诉地图自己的初始化位置
        init_pos_msg = Int32MultiArray()
        init_pos_msg.data = self.position + [self.node_id]
        self.move_pub.publish(init_pos_msg)

        self.target = [0,0]#[len(self.map[0])//2, len(self.map)//2]  # 将地图中心点设为目标位置

        # 信道管理的话题
        self.control_sub = self.create_subscription(
            Int32,
            'stdma/control',
            self.control_callback,
            10)
        self.control_pub = self.create_publisher(Int32, 'stdma/control', 10)

        # 实际传输信息的话题
        self.message_pub = self.create_publisher(
            Int32MultiArray, "stdma/message", 10)

        self.message_sub = self.create_subscription(
            Int32MultiArray, "stdma/message", self.message_callback, 10)


        self.timer_sub = self.create_subscription(
            Bool,
            'stdma/timer',
            self.timer_callback,
            10)

    def control_callback(self, msg):
        '''
        用来分享信道占用情况（槽位使用权）的STDMA话题
        '''
        self.inbox.append(msg)

    def message_callback(self, msg):
        '''
        真正传输信息的STDMA话题
        '''
        data = plan_decompressor(msg.data)

        if hasattr(self, "plan") and data == self.plan:
            return  # 如果是自己发的：跳过
        else:
            self.inbox_plan.append(data)  # 加入收到的计划中
        '''        
        if hasattr(self,"plan"):
            if data == self.plan:
                self.get_logger().warning("收到自己的了")
        '''

    def get_messages(self):
        '''
        将self.inbox中的信息逐个弹出，构成新的列表并返回此列表

        Returns:
            received_messages (list) : inbox的全部内容。调用此函数会清空inbox
        '''
        received_messages = []
        num_messages = len(self.inbox)
        for ii in range(num_messages):
            received_messages.append(self.inbox.pop(0))
        return received_messages

    def timer_callback(self, msg):  # 收到时钟信号时的callback分流
        if msg.data:
            # rising edge - start/end of slot 上升沿标志着slot的结束
            self.end_slot_callback()
        else:
            # falling edge - middle of slot
            self.mid_slot_callback()

    def end_slot_callback(self):
        '''
        收到时钟信号且为上升沿，slot结束时自动调用的callback
        记录当前槽位和帧数
        更新信道使用情况
        选择自己的槽位编号
        - 根据自己的计划移动一格
        - 将收到的所有计划删除一位（已被执行）
        - 如果下一slot是自己的：筹谋
        - 这样实现了实际上的在前半槽筹谋。因为前半槽的开始实际上也是end标注的（end就是start嘛。）
        - 移动和清除一格计划是同时就进行的，唯一迷惑的地方就在于筹谋和这俩的先后顺序。
        '''
        if self.slot == -1:
            # first ever run - need to wait for end of first slot
            self.slot = 0
            self.get_logger().info('Start of slot 0 frame 0')
        else:
            self.get_logger().info('End of slot %d frame %d' % (self.slot, self.frame))
            # end of slot - check received messages
            received_messages = self.get_messages()
            num_messages = len(received_messages)

            # 如果此slot内没收到任何东西：槽为空
            if num_messages == 0:
                self.get_logger().info('Slot %d looks empty' % self.slot)
                self.slot_allocations[self.slot] = None  # 登记本槽为空

            # 如果本slot内仅收到一条消息: 槽已有主
            elif num_messages == 1:
                msg = received_messages[0]
                sender = msg.data
                self.get_logger().info('Slot %d allocated to %d' % (self.slot, sender))
                self.slot_allocations[self.slot] = sender  # 登记槽位分配情况
                if sender == self.node_id:  # 如果此时发现发送者就自己一个：
                    # my own message - means successfully in channel
                    self.state = 'in'  # 自己已经成功拿下一个槽
                    self.get_logger().info('Secured my own slot')  # 说出来高兴一下

            # 如果本槽内收到多条消息：碰撞
            elif num_messages > 1:
                # more than one message in a slot - collision
                colliding_ids = [
                    m.data for m in received_messages]  # 撞车的哥几个都是谁
                self.get_logger().warning('Collision between %s' % colliding_ids.__str__())
                self.slot_allocations[self.slot] = None  # 本槽归0，清空所有权
                # 如果哥们自己也撞了：接着听吧, 没宣称成功
                if self.node_id in colliding_ids:
                    self.get_logger().warning('%s lost slot due to collision' % self.get_name())
                    self.state = 'listen'  # 注意，站点初始化时状态就是listen
                    self.my_slot = -2
                    if self.state == "in":
                        self.get_logger().warning(
                            "\n\n\nCollision between secured and joining! NEVER SHOULD HAPEN! \n\n\n")
            if self.state == 'check':
                # successful join would have changed state to 'in'
                # collision would have changed to 'listen'
                # so this must mean lost data 到这就是有问题，恢复成'listen'状态吧
                self.state = 'listen'
                self.my_slot = -2
            # update for next slot 更新当前槽位编号，到下一个槽位编号。
            self.slot += 1
            if self.slot == self.num_slots:  # 超限归零
                self.slot = 0
                self.frame += 1
                if self.state == 'listen':
                    # 运行到此处代表已经听完完整的一帧并确定好分配情况，接下来的几行代码随机选空槽
                    # have listened to a whole frame - time to try and get in
                    self.state = 'enter'
                    available_slots = [ii for ii in range(
                        self.num_slots) if self.slot_allocations[ii] == None]
                    if available_slots:
                        self.my_slot = random.sample(available_slots, 1)[0]
                        self.get_logger().info('Will try to enter at slot %d' % self.my_slot)
                    else:
                        self.get_logger().info("No avaliable slots in the channel.")
            if self.slot == self.my_slot:
                self.get_logger().info('Slot allocations: %s' %
                                       self.slot_allocations.__str__())

            self.get_logger().info('State: "%s" my slot: %d' % (self.state, self.my_slot))

            # TODO: 执行一次移动
            if hasattr(self, "plan") and self.plan:  # 如果有计划且计划不为空：
                next_pos = list(self.plan.pop(0))  # 取自己计划中的第一个
                self.position = next_pos
                msg = Int32MultiArray()
                msg.data = next_pos + [self.node_id]
                self.move_pub.publish(msg)

            else: # 如果没有计划：只宣布自己现在的位置, 即原地不动
                msg = Int32MultiArray()
                msg.data = self.position + [self.node_id]
                self.move_pub.publish(msg)
                

            # 在筹谋前：每个槽结束把执行过的计划删除
            if self.inbox_plan:
                i = len(self.inbox_plan)-1
                while i >= 0:
                    if self.inbox_plan[i]:
                        self.inbox_plan[i].pop(0)  # 清除一个
                    else:
                        del self.inbox_plan[i]  # 如果已经为空，消灭此计划。
                    i -= 1
                self.get_logger().info(self.inbox_plan.__str__())

            # TODO: 如果下一槽位是自己的且自己已经加入网络：筹谋。
            if self.state == "in":
                if self.slot == self.my_slot:
                    self.plan = find_path(
                        map=self.map, max_steps=self.num_slots, start=self.position, goal=self.target)

    def mid_slot_callback(self):
        '''
        收到时钟信号且为下降沿，槽中被调用的函数
        说话是在这个时机进行的。
        计划的发送是在这个时机进行的
        '''
        if self.slot >= 0:  # 如果当前槽计数值>=0 这是防止刚初始化的站点掺和进流程里头的判断
            self.get_logger().info('Middle of slot %d frame %d' % (self.slot, self.frame))
            if self.slot == self.my_slot:  # 如果觉得该自己说话：说话
                msg = Int32()
                msg.data = self.node_id
                self.control_pub.publish(msg)
                self.state = 'check'
                self.get_logger().info('Sent my control message')

                # TODO: 发送计划
                if hasattr(self, "plan") and self.plan:  # 如果有计划且计划不为空：广播计划
                    msg = Int32MultiArray()
                    msg.data = plan_compressor(self.plan)
                    self.message_pub.publish(msg)

    def rubbish():
        '''
        草稿过程中产生的废物函数。这是垃圾填埋场。
        '''
        received_messages = self.get_messages()
        previous_slot = (self.slot-1) % self.num_slots
        if len(received_messages) == 1:
            msg = received_messages[0]
            sender = re.search('stdma_talker_[0-9]+', msg.data).group()
            self.slot_allocations[previous_slot] = sender
            self.get_logger().info('Slot %d belongs to %s, got %s' %
                                   (previous_slot, sender, msg.data))
            if sender == self.node_name:
                # means I've got my own slot
                self.state = 'in'
                self.get_logger().info('Got own message back - successful entry')
        elif len(received_messages) == 0:
            self.get_logger().info('Slot %d empty' % previous_slot)
            self.slot_allocations[self.slot] = None
        else:
            self.get_logger().info('Slot %d collision' % previous_slot)
            for msg in received_messages:
                self.get_logger().info('Got message %s' % msg.data)
        if self.state == 'check':
            # means my message didn't get through
            self.state = 'listen'
            self.get_logger().info('Collision - back to listening')
        if self.state != 'listen' and self.slot == self.my_slot:
            # time to send a message
            msg = String()
            msg.data = 'Hello from %s : frame %d slot %d' % (
                self.node_name, self.frame, self.slot)
            self.publisher_.publish(msg)
            if self.state == 'enter':
                self.state == 'check'
            self.get_logger().info('Sent: "%s" mode : "%s"' % (msg.data, self.state))
        self.slot += 1
        if self.slot == self.num_slots:
            self.slot = 0
            self.frame += 1
            if self.state == 'listen':
                # have now listened to a whole slot - time to try and get in
                self.state = 'enter'
                self.get_logger().info('Listened for whole frame - ready to enter')
                available_slots = [ii for ii in range(
                    self.num_slots) if self.slot_allocations[ii] is None]
                if available_slots:
                    self.my_slot = available_slots[0]
        self.get_logger().info('State %s my slot %d allocs %s' %
                               (self.state, self.my_slot, self.slot_allocations.__str__()))


def main(args=None):
    rclpy.init(args=args)

    stdma_talker = StdmaTalker()

    rclpy.spin(stdma_talker)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    stdma_talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
