import rclpy
import pygame
import os
import sys
import math
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
import stdma_talker

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

from rclpy.logging import LoggingSeverity

log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/log1.log"

def size_cal(node_num):
    '''
    根据节点数目安排一个合适的宽高

    Args:
        node_num (int): 节点数目

    Returns:
        （width, height）: 注意，单位均为"个"
    '''
    width = math.ceil(math.sqrt(node_num))
    height = math.ceil(node_num/width)
    return (width,height)

def pos_find(width,number):
    '''
    根据标号寻找在表格内位置的函数，假设标号均从0开始（行列标号，number标号均如此）

    Args:
        width (_type_): _description_
        number (_type_): _description_

    Returns:
        （x,y）: （横坐标，纵坐标）
    '''
    x = number % width  # 横坐标
    y = number // width # 纵坐标

    return (x,y)



class ChannelVisualiser(stdma_talker.StdmaTalker):

    def __init__(self):

        

        super().__init__()
        # 显示所有信息
        self.get_logger().set_level(LoggingSeverity.FATAL) 

        # 初始化pygame
        pygame.init()

        # 定义窗口和表格参数

        self.window_size = size_cal(self.num_slots) # 用slot数目计算合适的窗口大小，单位为"个节点"

        # 初始化格子大小
        self.grid_size = 100
        while self.grid_size*self.window_size[0]>800 or self.grid_size*self.window_size[1]>800:
            self.grid_size -=1
            if self.grid_size == 1:
                break

        self.screen = pygame.display.set_mode((self.window_size[0]*self.grid_size, self.window_size[1]*self.grid_size))
        pygame.display.set_caption('Channel')

        # 初始化占用情况记录
        self.occupation = {}


        # 初始化涂成某一颜色
        self.screen.fill(WHITE)

        pygame.display.flip()

    def end_slot_callback(self):
        super().end_slot_callback()
        self.my_slot = -2  # 将自己想要的槽位锁死在-2。这样阻止节点入网
        self.state = "listen"  # 锁死在侦听状态



    def timer_callback(self, msg):
        self.my_slot = -1
        # 如果是槽位结束处（msg.data=True）:更新绘制的图形
        if msg.data:
            self.update_cells()

        super().timer_callback(msg)





    def update_cells(self):
        '''
        在一槽结束时被调用，根据当前槽位标号和收到的信息（发送者pid）更新格子
        '''
        received_msg = self.inbox
        self.occupation[self.slot]  = received_msg.copy() # 更新占用情况

        self.screen.fill(WHITE) # 先刷白

        # 然后用占用情况重新绘制
        for pos,resident in self.occupation.items():
            if not resident: continue
            cell_x, cell_y = pos_find(self.window_size[0],pos)
            cell_x = cell_x*self.grid_size
            cell_y = cell_y*self.grid_size
            cell_value = [_.data for _ in resident].__str__()
            color = GREEN
            if len(resident)>1: color = RED
            pygame.draw.rect(self.screen,color,pygame.Rect(cell_x,cell_y,self.grid_size,self.grid_size),0)
            font = pygame.font.Font(None,20)
            text = font.render(cell_value, True, BLACK)
            text_rect = text.get_rect(center=(cell_x + self.grid_size / 2, cell_y + self.grid_size / 2))
            self.screen.blit(text, text_rect)

        # 绘制当前位置四周的黑框线
        left,top = pos_find(self.window_size[0],self.slot)
        left = left*self.grid_size
        top = top*self.grid_size
        pygame.draw.rect(self.screen,BLACK,(left,top,self.grid_size,self.grid_size),1)

        pygame.display.flip()


def main(args=None):

    rclpy.init(args=args)

    CV = ChannelVisualiser()

    rclpy.spin(CV)

    CV.destroy_node()
    rclpy.shutdown()
