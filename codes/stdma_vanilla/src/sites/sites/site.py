import rclpy

from rclpy.node import Node

from interfaces.msg import Slot

from interfaces.srv import ApplyForSending, MapSending, MapLocationUpdate

import random

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
from pathfinding_test import find_path  # 导入临时瞎写的寻路包。此处的寻路是用A*实现的。


# 给stdma通信层的信道topic的名字
name_for_stdma_channel = "STDMA_Channel"

# 初始化地图信息的服务名称
name_for_map_init_service = "MapSender"

# 向地图更新自己位置的服务名称
name_for_map_location_update = "MapLocationUpdater"

# 如果节点没有加入网络，它的槽位就是这个值：
not_joined = -100


def map_uncondenser(map_list_1d):
    '''
    将输入的一维数组恢复为二维数组的函数，输入的一维数组第一位是原数组宽，第二位是原数组高

    Args:
        map_list_1d (list): 输入的一维数组第一位是原数组宽，第二位是原数组高

    Returns:
        list[list[]]: 恢复的二维数组
    '''
    width = map_list_1d[0]
    height = map_list_1d[1]

    del map_list_1d[:2]

    map_list_2d = [map_list_1d[i:i+width]
                   for i in range(0, len(map_list_1d), width)]

    return map_list_2d


class Site(Node):
    def __init__(self, name):
        super().__init__(name)

        # 话题接收者部分
        self.received_stdma_msg_ = Slot()
        self.stdma_receiver_client_ = self.create_subscription(
            Slot, name_for_stdma_channel, self.stdma_subscriber_callback, 10)

        # 向信道申请位置部分
        self.client_apply_slot_ = self.create_client(
            ApplyForSending, "ApplyForSending")

        # 站点的编号
        self.site_no = int(self.get_name()[-1])

        # 此节点占有的slot槽位编号是
        self.slot_no_ = not_joined  # not_joined = -100 代表还未加入网络

        # 地图的物理信息
        self.map_ = None

        # 初始化时接收地图信息的客户端
        self.map_init_client_ = self.create_client(
            MapSending, name_for_map_init_service)

        # 移动时向地图发送信息的客户端
        self.map_move_client_ = self.create_client(
            MapLocationUpdate, name_for_map_location_update)

        # 站点在地图中的物理位置
        # 左上为（0，0），x横y纵
        self.declare_parameter("start_x", 1)
        self.declare_parameter("start_y", 1)

        # 站点的目标位置
        self.declare_parameter("target_x", 2)
        self.declare_parameter("target_y", 2)

        self.get_logger().info("站点，启动！此节点的名字是%s, 初始坐标为(x = %d, y = %d)" %
                               (self.get_name(), self.get_local_location()[0], self.get_local_location()[1]))

        # 初始化地图信息
        self.load_map_()

        # 站点的移动计划
        self.plan_ =  [self.get_local_location()]+ find_path(
            self.map_, self.get_local_location(), self.get_target_location())

        

        # 加入网络
        self.join_network()

    def load_map_(self):
        '''
        应在节点初始化阶段调用，从地图节点中读取地图物理信息的函数
        '''
        while not self.map_init_client_.wait_for_service(1):
            self.get_logger().info("地图节点还妹开呢。")
        request = MapSending.Request()
        request.applicant = self.site_no
        future = self.map_init_client_.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.map_ = map_uncondenser(future.result().map_data)
        self.get_logger().info("名为%s的节点地图加载成功。" % self.get_name())

    def set_local_location(self, x, y):
        '''
        更新以参数形式保存在本地的自身位置数据。也就是self.x,self.y

        Args:
            x (int): 横坐标
            y (int): 纵坐标
        '''
        x_new = rclpy.parameter.Parameter(
            "start_x",
            rclpy.Parameter.Type.INTEGER,
            x
        )

        y_new = rclpy.parameter.Parameter(
            "start_y",
            rclpy.Parameter.Type.INTEGER,
            y
        )

        all_new_params = [x_new, y_new]

        self.set_parameters(all_new_params)

    def get_local_location(self):
        '''
        获得本地保存的自身位置

        Returns:
            [x,y]:[横坐标，纵坐标]
        '''
        x = self.get_parameter("start_x").get_parameter_value().integer_value
        y = self.get_parameter("start_y").get_parameter_value().integer_value

        return [x, y]

    def get_target_location(self):
        '''
        获得本地保存的目标位置
        '''
        x = self.get_parameter("target_x").get_parameter_value().integer_value
        y = self.get_parameter("target_y").get_parameter_value().integer_value

        return [x, y]

    def apply_for_sending(self, data):
        '''
        在获得位置后向信道发送消息用的函数

        Args:
            data (string): 此信息的类型要想更改记得改srv里的数据类型现在暂时是字符串
        '''
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


    def stdma_subscriber_callback(self, msg):
        '''
        从stdma通信层信道topic接收到信息时运行的回调函数
        '''
        self.received_stdma_msg_ = msg
        # self.get_logger().info("msg received: slot %d/%d from site %d." %
        #                       (self.received_msg.slot_no, self.received_msg.slot_total, self.received_msg.sender_no))

        # 保存收到的信道信息
        self.frame_length_ = msg.slot_total
        self.current_slot_ = msg.slot_no
        if not hasattr(self, "occupied_"):
            self.occupied_ = [-1]*self.frame_length_

        self.occupied_[self.current_slot_-1] = msg.occupied

        # 取计划中的第一个格子。
        if self.plan_:  # 如果计划不为空：向计划中的下一个点移动
            next_pos = self.plan_[0]
            next_x = next_pos[0]
            next_y = next_pos[1]

            self.move_to(next_x, next_y)
            # 已到达的目标点的删除是在move的完成回调中进行。
        else: self.get_logger().info("%s的计划为空。"%self.get_name())


        # 当轮到自己说话的时候，说话。
        if not hasattr(self, "slot_no_"):
            return
        if (self.current_slot_ == self.slot_no_ - 1) or (self.slot_no_ == 1 and self.current_slot_ == self.frame_length_):
            # 轮到自己了，说话。
            self.apply_for_sending("我是"+str(self.get_name()))

    def apply_for_slot(self, slot_desired):
        '''
        用来申请加入网络
        Args:
            slot_desired (int): 申请的位置编号，slot的编号从1开始

        Returns:
            _type_: _description_
        '''

        # 当信道还不在线的时候，打印一个不在线
        while not self.client_apply_slot_.wait_for_service(1):
            self.get_logger().warn("信道还没开，信道还没开")

        # 构造请求的内容
        request = ApplyForSending.Request()
        request.applicant = self.site_no
        request.apply_slot = slot_desired

        # 发送请求
        future = self.client_apply_slot_.call_async(request)
        rclpy.spin_until_future_complete(self, future)  # 等待服务完成

        # 返回申请结果
        if future.result() is not None and future.result().result:
            return True
        else:
            return False

    def join_network(self):
        '''
        应在节点初始化函数里调用。用来加入网络的函数。
        '''

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
                    self.slot_no_ = apply_for  # 保存自己的槽位
                    self.move_to(self.get_local_location()[
                                 0], self.get_local_location()[1])  # 初始化自身起始位置
                    return success
                else:
                    # 随机换一个自己可以用的槽位
                    candidates = [
                        i+1 for i in range(len(self.occupied_)) if self.occupied_[i] == False]
                    apply_for = random.choice(candidates)

    def move_to(self, x, y):
        '''
        将自己的目标位置发送给地图，申请移动。如果地图端判断无物理碰撞，服务会返回true，此时更新本地位置记录。

        Args:
            x (int16): 横坐标
            y (int16): 纵坐标
        '''
        request = MapLocationUpdate.Request()
        request.applicant = self.site_no
        request.x = x
        request.y = y
        self.map_move_client_.call_async(
            request).add_done_callback(self.move_finish_callback)

    def move_finish_callback(self, future):
        result = future.result()
        if result.success:
            # 如果成功移动：删除计划中的第一个点
            if self.plan_: del self.plan_[0]
            else: self.get_logger().info("%s已经没有下一步计划了！"%self.get_name())
            self.get_logger().info("%s成功移动，当前位置为%d,%d" %
                                   (self.get_name(), self.get_local_location()[0], self.get_local_location()[1]))

        else:
            # 不然：啥也不干
            self.get_logger().info("%s移动失败，目标位置为%d,%d" %
                                   (self.get_name(), self.get_local_location()[0], self.get_local_location()[1]))


def main(args=None):

    rclpy.init(args=args)

    site = Site("node1")

    rclpy.spin(site)

    rclpy.shutdown()
