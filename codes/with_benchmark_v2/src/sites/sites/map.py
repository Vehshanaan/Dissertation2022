import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Bool, Int32MultiArray
import pygame  # 地图绘制用
import json  # 结果保存用
import time  # 日志文件命名时间戳用

# 导入工具箱（和map位于同一文件夹）：
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
import utils  # 导入工具箱

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 实验结果日志文件夹路径
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/"


def find_keys_with_same_value(dictionary):
    '''
    返回字典中拥有相同值的键的列表，这个是用来检查地图中位置冲突用的。

    Args:
        dictionary : 被论断的字典

    Returns:
        list: [[具有相同值1的键的列表], [具有相同值2的键的列表]， 。。。]
    '''
    value_to_keys = {}

    # 遍历字典，将值作为键，将键作为值存储在value_to_keys字典中
    for key, value in dictionary.items():
        value = tuple(value)
        if value not in value_to_keys:
            value_to_keys[value] = []
        value_to_keys[value].append(key)

    # 找到具有相同值的键
    keys_with_same_value = [
        keys for keys in value_to_keys.values() if len(keys) > 1]

    return keys_with_same_value


def id_to_color(code):
    '''
    根据输入的编号生成唯一对应RGB颜色

    Args:
        code (int): 节点编号

    Returns:
        color (r,g,b): 三通道值
    '''
    number = int(code)
    r = (number * 127) % 256  # 每个通道的取值范围是0-255
    g = (number * 83) % 256
    b = (number * 43) % 256
    return (r, g, b)


class Map(Node):
    def __init__(self):
        super().__init__("Map")
        self.inbox_plan = {}  # 记录各节点的计划
        self.message_sub = self.create_subscription(
            Int32MultiArray, "stdma/message", self.message_callback, 100)  # 接受节点发送的计划的话题
        self.node_positions = {}  # 记录节点的位置

        # 从外界初始化地图文件路径（读取地图要用）
        self.declare_parameter("map_path", "_")
        map_path = self.get_parameter(
            "map_path").get_parameter_value().string_value
        self.map_path = map_path

        # 从外界初始化场景文件路径 （写结果保存日志文件用，为了以后自己不蒙圈）
        self.declare_parameter("scene_path", "_")
        scene_path = self.get_parameter(
            "scene_path").get_parameter_value().string_value
        self.scene_path = scene_path

        # 读取地图
        map = utils.map_load(self.map_path)
        self.map = map
        self.height = len(map)
        self.width = len(map[0])

        # 从外部初始化帧长度（写结果保持日志文件用，为了以后自己不蒙圈）
        self.declare_parameter("num_slots", 10)
        num_slots = self.get_parameter(
            "num_slots").get_parameter_value().integer_value
        self.num_slots = num_slots

        # 日志路径的生成
        dir_path = log_path+str(os.path.basename(map_path))+"/"
        if not os.path.exists(dir_path):  # 为每个地图创建一个子文件夹保存其对应日志结果文件
            os.makedirs(dir_path)
        self.log_path = dir_path+"FrameLen" + \
            str(self.num_slots)+str(time.strftime("%h%d%H%M")) + \
            ".log"  # 日期格式：月（英文缩写）日时分

        # 自适应调节地图格子大小
        grid_size = 20
        while grid_size*self.height > 1300 or grid_size*self.width > 1300:
            grid_size = grid_size-1
        
        self.grid_size = grid_size

        self.position_history = {}  # 记录节点位置的历史，日志里用
        self.time = 0  # 时间戳，给节点位置历史分时间用

        self.timer_sub = self.create_subscription(
            Bool, "stdma/timer", self.timer_callback, 10)

        self.node_with_plans = set([])

        self.map_init()  # 初始化可视化地图窗口

    def map_init(self):
        '''
        初始化地图窗口
        '''
        pygame.init()
        pygame.display.set_caption("Map")
        self.window = pygame.display.set_mode(
            (self.width*self.grid_size, self.height*self.grid_size))
        self.map_reset()  # 初始化窗口内的内容
        pygame.display.flip()  # 刷新一下显示

    def map_reset(self):
        '''
        将地图抹白，然后画上障碍物
        '''
        # 恢复到全白
        self.window.fill(WHITE)
        # 绘制障碍物
        for row in range(self.height):
            for col in range(self.width):
                cell_color = BLACK if self.map[row][col] == False else WHITE
                pygame.draw.rect(
                    self.window,
                    cell_color,
                    (col * self.grid_size, row * self.grid_size,
                     self.grid_size, self.grid_size),
                )
    def message_callback(self, msg):
        '''
        接收到节点计划的处理
        '''
        node_id, data = utils.plan_decompressor(msg.data)

        self.inbox_plan[node_id] = data  # 保存收到的计划 字典保证了这东西一人只有一个

    def position_update(self):
        '''
        用计划更新位置。此函数会弹出所有计划的第一位
        '''
        if self.inbox_plan:
            for key in list(self.inbox_plan.keys()):
                if self.inbox_plan[key]:  # 如果计划不空：
                    self.node_positions[key] = self.inbox_plan[key].pop(
                        0)  # 用计划的头一位更新位置

    def history_update(self):
        '''
        将当前节点-位置 数据对保存到历史记录变量中
        '''
        frame = []
        for key in list(self.node_positions.keys()):
            node_pos = [key, self.node_positions[key]]  # [node_id, [位置]]
            frame.append(node_pos)  # 加入当前帧
        self.position_history[self.time] = frame  # 将当前帧保存到历史记录中

    def log_write(self):
        '''
        将文件写入日志实验结果保存文件
        '''
        with open(self.log_path, "w") as log:
            data = {
                "scene_path": self.scene_path,
                "map_path": self.map_path,
                "history": self.position_history
            }
            json.dump(data, log)

    def map_update(self):
        # 先还原成纯白
        self.map_reset()

        # 根据收到的计划画出计划
        for key, value in self.inbox_plan.items():
            node_id = key
            plans = value
            color = id_to_color(node_id)

            size = self.grid_size/2.5
            # 将计划中所有格填上代表色
            for i in range(len(plans)):
                x, y = plans[i]
                x = x*self.grid_size+self.grid_size//2
                y = y*self.grid_size+self.grid_size//2

                # 为了看清楚swap的情形，先不画出计划线
                pygame.draw.circle(self.window, color, (x, y), size)

                # 每画一格尺寸缩小一点点
                size = size*0.95
                if size < 1:
                    size = 1

        # 根据self.node_position绘制节点当前位置
        for key, value in self.node_positions.items():
            node_id = key  # 提取节点名称
            x, y = value  # 提取横纵坐标

            # 画节点占用的位置的底色
            pygame.draw.rect(
                self.window,
                id_to_color(node_id),
                (x*self.grid_size, y*self.grid_size, self.grid_size, self.grid_size)
            )

            center_x = x*self.grid_size+self.grid_size//2
            center_y = y*self.grid_size+self.grid_size//2
            number_text = self.font.render(str(node_id), True, GREEN)
            text_rect = number_text.get_rect(center=(center_x, center_y))
            self.window.blit(number_text, text_rect)

        # 根据字典value唯一性判断是否有碰撞
        collisions = find_keys_with_same_value(
            self.node_positions)  # [[具有相同位置的节点的id]]
        if collisions:

            # 将发生碰撞的位置画成红色，里面填上碰撞的是谁
            for collision in collisions:
                collision_pos = self.node_positions[collision[0]]
                # 格子涂红
                pygame.draw.rect(
                    self.window,
                    RED,
                    (collision_pos[0]*self.grid_size, collision_pos[1]
                     * self.grid_size, self.grid_size, self.grid_size)
                )
                # 里面写上撞车的是谁
                center_x = collision_pos[0]*self.grid_size+self.grid_size//2
                center_y = collision_pos[1]*self.grid_size+self.grid_size//2
                number_text = self.font.render(
                    collision.__str__(), True, GREEN)
                text_rect = number_text.get_rect(center=(center_x, center_y))
                # self.get_logger().warning("在（%d, %d）处，%s之间发生碰撞"%(collision_pos[0],collision_pos[1],collision.__str__()))
                self.window.blit(number_text, text_rect)

        pygame.display.flip()  # 刷新画面

    def timer_callback(self, msg):
        if msg.data:  # 如果是上升沿：槽的开始/结束
            self.time += 1
            self.position_update()  # 用收到的槽的计划更新节点位置
            self.history_update()  # 更新历史记录
            self.log_write()  # 写入日志文档
            self.map_update()  # 更新地图


def main(args = None):

    rclpy.init()

    map = Map()

    rclpy.spin(map)

    map.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()