import rclpy

from rclpy.node import Node

from interfaces.srv import MapSending, MapLocationUpdate


class TesterNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("测试用节点，启动！")

        self.timer_period_ = 1

        # 初始化时接收地图用的函数
        self.client_ = self.create_client(MapSending, "MapSender")

        # 移动时向地图更新位置的函数
        self.client_map_move_ = self.create_client(
            MapLocationUpdate, "MapLocationUpdater")

        # 地图的物理信息
        self.map_data_ = None

        # 站点在地图中的位置
        self.location_ = [1, 1]

        # 初始化时加载地图
        self.load_map()

        self.create_timer(self.timer_period_, self.move)

    def load_map(self):
        request = MapSending.Request()
        future = self.client_.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.map_data_ = future.result()
        print(self.map_data_)

    def move_callback(self, future):

        result = future.result()
        if result.success:
            print("成功移动，当前位置为%d,%d" % (self.location_[0], self.location_[1]))
            self.location_[0] += 1
            self.location_[1] += 1
        else:
            print("移动失败，目标位置为%d,%d" % (self.location_[0], self.location_[1]))
            pass

    def move(self):
        # 移动到指定位置，实际上就是向地图更新自己的位置，会返回成功与否。
        # 调用服务，获取结果
        request = MapLocationUpdate.Request()
        request.applicant = -1
        request.x = self.location_[0]
        request.y = self.location_[1]
        self.client_map_move_.call_async(
            request).add_done_callback(self.move_callback)


def main(args=None):

    rclpy.init(args=args)

    tester = TesterNode("test_node")

    rclpy.spin(tester)

    rclpy.shutdown
