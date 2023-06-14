import rclpy
import pygame

from rclpy.node import Node

from interfaces.srv import MapSending
from interfaces.msg import MapVisualiserSiteMoves

# 初始化地图信息的服务名称
name_for_map_init_service = "MapSender"

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 定义窗口和单个网格大小
WINDOW_SIZE = (500, 500)
GRID_SIZE = 50

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

class MapVisualiser(Node):
    def __init__(self, name):
        super().__init__(name)

        # 地图的物理信息保存
        self.map_ = None


        # 地图上的节点物理位置保存
        self.site_loactions_ = None

        # 初始化时接收地图信息的客户端
        self.map_init_client_ = self.create_client(
            MapSending, name_for_map_init_service)

        # 初始化地图有人移动时接收信息的客户端
        self.site_move_subscriber_ = self.create_subscription(
            MapVisualiserSiteMoves, "SiteMoves", self.site_moves_callback, 10)

        # 站点编号
        self.site_no_ = -1

        # 向地图站点申请地图的物理信息
        self.load_map_()

        # 根据物理地图信息绘制地图
        self.draw_map_init()

        # 写数字时用的字体
        pygame.font.init()
        self.font = pygame.font.Font(None, int(GRID_SIZE * 0.8))
        

    def load_map_(self):
        '''
        应在节点初始化阶段调用，从地图节点中读取地图物理信息的函数
        '''
        while not self.map_init_client_.wait_for_service(1):
            self.get_logger().info("地图节点还妹开呢。")
        request = MapSending.Request()
        request.applicant = self.site_no_
        future = self.map_init_client_.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.map_ = map_uncondenser(future.result().map_data)
        self.get_logger().info("名为%s的节点地图加载成功。" % self.get_name())
        self.width = len(self.map_[0])
        self.height = len(self.map_)

    def draw_map_init(self):
        '''
        根据初始化时收到的地图物理信息绘制地图
        '''
        self.window = pygame.display.set_mode((self.width*GRID_SIZE, self.height*GRID_SIZE))
        self.window.fill(WHITE)

        for row in range(self.height):
            for col in range(self.width):
                cell_color = BLACK if self.map_[row][col]==0 else WHITE
                pygame.draw.rect(
                    self.window,
                    cell_color,
                    (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

        # 绘制网格线
        for row in range(self.height):
            pygame.draw.line(
                self.window,
                BLACK,
                (0, row * GRID_SIZE),
                (self.width*GRID_SIZE, row * GRID_SIZE)
            )
        for col in range(self.width):
            pygame.draw.line(
                self.window,
                BLACK,
                (col * GRID_SIZE, 0),
                (col * GRID_SIZE, self.height*GRID_SIZE)
            )

        pygame.display.flip()

    def map_cell_update(self,col,row,value,color):
        '''
        根据给定的颜色和坐标更新地图的格子颜色

        Args:
            col (int): 纵坐标
            row (int): 横坐标
            value (int): 节点标号
            color ((int,int,int)): RGB颜色
        '''
        pygame.draw.rect(
            self.window,
            color,
            (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )
        center_x = col * GRID_SIZE + GRID_SIZE // 2
        center_y = row * GRID_SIZE + GRID_SIZE // 2
        number_text = self.font.render(str(value), True, GREEN)
        text_rect = number_text.get_rect(center=(center_x, center_y))
        self.window.blit(number_text, text_rect)
        pygame.display.flip()


        

    def site_moves_callback(self, msg):
        '''
        收到map节点的消息：有节点试图移动。根据信息更新地图。
    

        Args:
            msg (_type_): _description_
        '''
        moved_site_no = msg.site_no
        target_x = msg.x
        target_y = msg.y
        self.map_cell_update(target_x,target_y,moved_site_no,RED)


def main(args=None):
    rclpy.init(args=args)

    MapVisNode = MapVisualiser("MapVisualiser")

    rclpy.spin(MapVisNode)

    rclpy.shutdown()
