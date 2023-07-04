import rclpy
import sys
import os
from rclpy.node import Node
from std_msgs.msg import Int32, Bool, Int32MultiArray
import pygame


import sys, os
parent_dir = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/stdma_with_benchmark_v1/src/sites"
sys.path.append(parent_dir)
# 看来即使被复制走，节点仍然位于同一文件夹下
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import stdma_talker
from utils.utils import map_load

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# 未初始化情况下的默认地图路径
map_path_default = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_0_256.png"

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
    keys_with_same_value = [keys for keys in value_to_keys.values() if len(keys) > 1]
    
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

        # 从外界初始化地图路径
        self.declare_parameter("map_path",map_path_default)

        map_path = self.get_parameter("map_path").get_parameter_value().string_value

        # 从外界初始化打开地图的大小
        self.declare_parameter("map_size",(-1,-1))
        self.map_size = tuple(self.get_parameter("map_size").get_parameter_value().integer_array_value)


        # 读取地图
        map = map_load(map_path,self.map_size)

        self.map = map # 录入地图

        self.height = len(map)
        self.width = len(map[0])

        # 自适应调整GRIDSIZE
        # 定义网格大小
        grid_size = 20
        while grid_size*self.height >1300 or grid_size*self.width>1300:
            grid_size-=1

        self.grid_size = grid_size

        self.inbox_plan = {} # 记录各节点计划
        self.node_positions = {} # 记录节点占有位置。 键值对为：节点编号：[坐标x,y]

        # 初始化可视化地图窗口
        self.map_init()

        # 写数字时用的字体
        pygame.font.init()
        
        self.font = pygame.font.Font(None, int(self.grid_size * 0.5))

        self.timer_sub = self.create_subscription(
            Bool,
            'stdma/timer',
            self.timer_callback,
            10)

        # 订阅节点发出的的移动信号
        self.move_sub = self.create_subscription(
            Int32MultiArray, "stdma/move", self.move_callback, 100)

        # 订阅节点发出的自身计划
        self.message_sub = self.create_subscription(Int32MultiArray, "stdma/message", self.message_callback, 1000)

    def map_reset(self):
        '''
        把地图恢复到只有网格线和障碍物，注意此函数内不包含flip
        '''
        self.window.fill(WHITE)

        # 绘制障碍物
        for row in range(self.height):
            for col in range(self.width):
                cell_color = BLACK if self.map[row][col]==False else WHITE
                pygame.draw.rect(
                    self.window,
                    cell_color,
                    (col * self.grid_size, row * self.grid_size, self.grid_size, self.grid_size),
                )

        # 绘制外侧安全区
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or row == self.height-1 or col == 0 or col == self.width-1:
                    pygame.draw.rect(
                        self.window,
                        GREEN,
                        (col*self.grid_size, row*self.grid_size, self.grid_size, self.grid_size),
                    )

        '''
        # 绘制网格线
        for row in range(self.height):
            pygame.draw.line(
                self.window,
                BLACK,
                (0, row * self.grid_size),
                (self.width*self.grid_size, row * self.grid_size)
            )
        for col in range(self.width):
            pygame.draw.line(
                self.window,
                BLACK,
                (col * self.grid_size, 0),
                (col * self.grid_size, self.height*self.grid_size)
            )
        '''

    def map_init(self):
        '''
        初始化地图可视化窗口
        '''
        pygame.init()
        pygame.display.set_caption('Map')
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.window = pygame.display.set_mode((self.width*self.grid_size,self.height*self.grid_size))
        self.map_reset()
        pygame.display.flip() # 显示地图可视化窗口

    def timer_callback(self,msg):
        if msg.data:
            # 上升沿：槽的开始或结束

            # 每个槽结束把执行过的计划删除
            if self.inbox_plan:
                for key, value in self.inbox_plan.items():
                    if not value: # 如果计划为空：删除计划
                        del self.inbox_plan[key]
                        continue
                    value.pop(0) # 弹掉计划的头一个
                    if not value: # 如果删完计划为空:删除计划键值对
                        del self.inbox_plan[key]
                        continue
        else:
            # 下降沿：槽的中间：更新地图。之所以不在槽的结束处更新是为了防止一边移动一边更新的情况
            self.map_update()

    def message_callback(self,msg):
        '''
        真正传输信息的STDMA话题
        '''
        node_id, data = stdma_talker.plan_decompressor(msg.data)

        self.inbox_plan[node_id] = data  # 加入收到的计划中

    def move_callback(self, msg):
        '''
        根据发来的移动信息记录节点位置
        '''
        data = msg.data
        node_id = data[2]
        # 发来的无边框地图坐标横纵各+1 = 有边框地图坐标
        x = data[0] # 横坐标
        y = data[1] # 纵坐标

        self.node_positions[str(node_id)] = [x,y] # 保存节点对应位置


        
    def map_update(self):
        
        # 先把地图回复全白带格子和障碍物
        self.map_reset()

        # 根据收到的计划画出计划
        for key,value in self.inbox_plan.items():
            node_id = key
            plans = value
            color = id_to_color(node_id)

            size = self.grid_size/2
            # 将计划中所有格填上代表色
            for i in range(len(plans)):
                x,y = plans[i]
                x = x*self.grid_size+self.grid_size//2
                y = y*self.grid_size+self.grid_size//2

                pygame.draw.circle(self.window,color,(x,y),size)

                # 每画一格尺寸缩小一点点
                size = size*0.97
                
        # 根据self.node_position绘制节点当前位置
        for key,value in self.node_positions.items():
            node_id= key # 提取节点名称
            x, y = value # 提取横纵坐标

            # 画节点占用的位置的底色
            pygame.draw.rect(
                self.window,
                id_to_color(node_id),
                (x*self.grid_size,y*self.grid_size,self.grid_size,self.grid_size)
            )
            
            center_x = x*self.grid_size+self.grid_size//2
            center_y = y*self.grid_size+self.grid_size//2
            number_text = self.font.render(str(node_id), True, GREEN)
            text_rect = number_text.get_rect(center=(center_x, center_y))
            self.window.blit(number_text,text_rect)
            #pygame.display.flip()


        # 根据字典value唯一性判断是否有碰撞
        collisions = find_keys_with_same_value(self.node_positions) # [[具有相同位置的节点的id]]
        if collisions:

            # 将发生碰撞的位置画成红色，里面填上碰撞的是谁
            for collision in collisions:
                collision_pos = self.node_positions[collision[0]]
                # 格子涂红
                pygame.draw.rect(
                    self.window,
                    RED,
                    (collision_pos[0]*self.grid_size,collision_pos[1]*self.grid_size,self.grid_size,self.grid_size)
                )
                # 里面写上撞车的是谁
                center_x = collision_pos[0]*self.grid_size+self.grid_size//2
                center_y = collision_pos[1]*self.grid_size+self.grid_size//2
                number_text = self.font.render(collision.__str__(),True,GREEN)
                text_rect = number_text.get_rect(center=(center_x,center_y))
                self.get_logger().warning("在（%d, %d）处，%s之间发生碰撞"%(collision_pos[0],collision_pos[1],collision.__str__()))
                self.window.blit(number_text, text_rect)


        '''
        # 重新绘制网格线,因为绘制格子内内容把线盖掉了
        for row in range(self.height):
            pygame.draw.line(
                self.window,
                BLACK,
                (0, row * self.grid_size),
                (self.width*self.grid_size, row * self.grid_size)
            )
        for col in range(self.width):
            pygame.draw.line(
                self.window,
                BLACK,
                (col * self.grid_size, 0),
                (col * self.grid_size, self.height*self.grid_size)
            )
        '''
        # 更新绘制结果
        pygame.display.flip()

def main(args = None):
    rclpy.init()

    map = Map()

    rclpy.spin(map)

    map.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

