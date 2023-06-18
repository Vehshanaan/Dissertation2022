# 地图节点
'''
流程：
    1. 初始化：从地图图片读入物理地图数据
    2. 保持服务畅通
        - 服务1： agent站点向地图发送，用来更新自己的位置
             - 输入： 坐标x，y 就从0开始用数组下标格式吧，不要折腾了
             - 输出：成功与否
        - 服务2： 向站点发送地图数据
             - 输入：无
             - 输出：真地图，但是打成一维，开头附上宽高数据，方便恢复。
'''


from interfaces.srv import MapSending, MapLocationUpdate
from interfaces.msg import MapVisualiserSiteMoves
from rclpy.node import Node
import rclpy
from PIL import Image

map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/map_builder/map1.png"


def map_reader(map_path):
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
                if pixels[j, i] == (255, 255, 255):
                    bool_array[i][j] = True
        return bool_array


def map_condenser(map_list_2d):
    '''
    将二维的数组压缩为一维的函数，压缩后在开头附上宽高数据，以便接收端恢复

    Args:
        map_list_2d (list[list[]]): 用来保存地图数据的二维数组 

    Returns:
        list: 被压缩为一维的数组，且开头附有宽高信息
    '''
    width = len(map_list_2d[0])
    height = len(map_list_2d)

    flattened = [_ for row in map_list_2d for _ in row]

    flattened.insert(0, width)
    flattened.insert(1, height)

    return flattened


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


class MapNode(Node):
    def __init__(self, name):
        super().__init__(name)

        self.get_logger().info("物理世界地图结点已启动")

        # 物理地图
        self.physical_map_ = map_reader(map_path)

        # 站点在地图中的位置，起始为空。
        self.sites_in_map_ = [[None for _ in row]
                              for row in self.physical_map_]

        # 向节点发送地图的服务
        self.map_sender_ = self.create_service(
            MapSending, "MapSender", self.map_init_sending_callback)

        # 节点申请移动的服务
        self.site_loaction_updater_ = self.create_service(
            MapLocationUpdate, "MapLocationUpdater", self.map_location_update_callback)

        # 每次有节点移动后告诉可视化器新消息的话题发布者
        self.site_moves_to_visualiser_publisher_ = self.create_publisher(
            MapVisualiserSiteMoves, "SiteMoves", 10)

    def map_location_update_callback(self, request, response):
        # 检查目的地是否是阻挡物，如果是则直接返回False
        x = request.x # 行号（纵坐标）
        y = request.y  # 列号（横坐标）
        node = request.applicant
        response.success = True  # 先初始化一个True, 后续根据条件结果修改
        # 检查目标位置是否超出范围。
        if y >= len(self.physical_map_) or x >= len(self.physical_map_[0]):
            response.success = False  # 目标位置出界了
        # 检查目标位置是否被阻挡
        if (self.sites_in_map_[x][y] != None and self.sites_in_map_[x][y] != node) or not self.physical_map_[x][y]:
            response.success = False  # 目标位置有别人或者有墙
            
        if response.success:  # 以下操作仅在成功移动时进行
            # 将图中所有此发送者占有的地方清空
            self.sites_in_map_ = [
                [None if element == node else element for element in sublist] for sublist in self.sites_in_map_]
            # 将新位置赋为发送者标号
            self.sites_in_map_[x][y] = node

            # 每有节点成功完成一次移动请求：向可视化节点发送移动情况。
            msg = MapVisualiserSiteMoves()  # 实例化信息对象
            msg.site_no = node
            msg.x = x
            msg.y = y
            self.site_moves_to_visualiser_publisher_.publish(msg)

        return response

    def map_init_sending_callback(self, request, response):
        '''
        服务回调函数：返回压缩为一维的地图，起始两位是地图宽，高。
        '''
        condensed_map = map_condenser(self.physical_map_)
        response.map_data = condensed_map
        print("进行了一次地图初始化服务")
        return response


def main(args=None):

    rclpy.init(args=args)

    map = MapNode("MapNode")

    rclpy.spin(map)

    rclpy.shutdown()
