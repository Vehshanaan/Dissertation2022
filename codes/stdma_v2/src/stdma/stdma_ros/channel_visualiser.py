import rclpy
import pygame
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
import stdma_talker

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

from rclpy.logging import LoggingSeverity

class ChannelVisualiser(stdma_talker.StdmaTalker):

    def __init__(self):

        

        super().__init__()
        # 显示所有信息
        self.get_logger().set_level(LoggingSeverity.INFO) 

        # 初始化pygame
        pygame.init()

        # 定义窗口和表格参数
        pygame.init()
        self.screen = pygame.display.set_mode((800, 100))
        pygame.display.set_caption('Channel Visualization')

        # 初始化表格相关变量
        self.cell_width = 50
        self.cell_height = 50
        self.columns = self.num_slots

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
        # 如果无人说：槽无主
        if not received_msg:
            color = WHITE
            return
        # 如果只有一个人在说：槽有主
        elif len(received_msg) == 1:
            color = GREEN
        # 如果有好几个人在说：写一下哥几个撞了
        elif len(received_msg) > 1:
            color = RED

        cell_x = self.slot * self.cell_width
        cell_y = 0
        cell_value = [_.data for _ in received_msg].__str__()

        pygame.draw.rect(self.screen, color, pygame.Rect(
            cell_x, cell_y, self.cell_width, self.cell_height), 0)

        font = pygame.font.Font(None, 20)
        text = font.render(cell_value, True, BLACK)
        text_rect = text.get_rect(
            center=(cell_x + self.cell_width / 2, cell_y + self.cell_height / 2))
        self.screen.blit(text, text_rect)

        pygame.display.flip()


def main(args=None):

    rclpy.init(args=args)

    CV = ChannelVisualiser()

    rclpy.spin(CV)

    CV.destroy_node()
    rclpy.shutdown()
