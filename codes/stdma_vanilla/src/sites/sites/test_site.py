import rclpy

from rclpy.node import Node

from interfaces.srv import MapSending, MapLocationUpdate


class TesterNode(Node):
    def __init__(self, name):
        super().__init__(name)

        self.timer_period_ = 1

        # 初始化时接收地图用的函数
        self.client_map_init_ = self.create_client(MapSending, "MapSender")

        # 移动时向地图更新位置的函数
        self.client_map_move_ = self.create_client(
            MapLocationUpdate, "MapLocationUpdater")

        # 地图的物理信息
        self.map_data_ = None


        # 站点在地图中的位置
        self.declare_parameter("x", 1)
        self.declare_parameter("y", 1)

        self.get_logger().info("测试用节点，启动！此节点的名字是%s, 初始坐标为(x = %d, y = %d)"%(self.get_name(),self.get_local_location()[0],self.get_local_location()[1]))

        # 初始化时加载地图
        self.load_map()

        self.create_timer(self.timer_period_, self.move)

        

    def set_local_location(self, x, y):
        '''
        更新以参数形式保存在本地的自身位置数据。也就是self.x,self.y

        Args:
            x (int): 横坐标
            y (int): 纵坐标
        '''
        x_new = rclpy.parameter.Parameter(
            "x",
            rclpy.Parameter.Type.INTEGER,
            x
        )

        y_new = rclpy.parameter.Parameter(
            "y",
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
        x = self.get_parameter("x").get_parameter_value().integer_value
        y = self.get_parameter("y").get_parameter_value().integer_value

        return [x,y]

    def load_map(self):
        '''
        节点初始化时从地图节点读取地图数据的函数
        '''
        while not self.client_map_init_.wait_for_service(1):
            self.get_logger().info('Map node is not available. Retrying...')
        request = MapSending.Request()
        future = self.client_map_init_.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.map_data_ = future.result()
        self.get_logger().info("%s地图加载成功"%self.get_name())

    def move_callback(self, future):
        '''
        发送移动服务并处理成功后进行的操作。这是一个回调函数。
        '''
        result = future.result()
        if result.success:
            self.get_logger().info("%s成功移动，当前位置为%d,%d" % (self.get_name(), self.get_local_location()[0], self.get_local_location()[1]))
            self.set_local_location(self.get_local_location()[0]+1,self.get_local_location()[1]+1)
        else:
            self.get_logger().info("%s移动失败，目标位置为%d,%d" % (self.get_name(), self.get_local_location()[0], self.get_local_location()[1]))
            pass

    def move(self):
        '''
        移动到指定位置，实际上就是向地图更新自己的位置，会返回成功与否。

        调用服务，获取结果

        调用完服务之后会调用另一个回调函数来处理

          - 我刚刚惊奇地发现，这个备注内部是markdown格式的
        '''
        request = MapLocationUpdate.Request()
        request.applicant = int(self.get_name()[-1])
        request.x = self.get_local_location()[0]
        request.y = self.get_local_location()[1]
        self.client_map_move_.call_async(
            request).add_done_callback(self.move_callback)


def main(args=None):

    rclpy.init(args=args)

    tester = TesterNode("test_node")

    rclpy.spin(tester)

    rclpy.shutdown
