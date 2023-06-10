import rclpy

from rclpy.node import Node

from interfaces.srv import MapSending

class TesterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("测试用节点，启动！")

        self.timer_period_ = 1

        self.client_ = self.create_client(MapSending,"MapSender")

        self.map_data_ = None

        self.load_map()

    def load_map(self):
        request = MapSending.Request()
        future = self.client_.call_async(request)
        rclpy.spin_until_future_complete(self,future)
        self.map_data_ = future.result()
        print(self.map_data_)
        


def main(args=None):

    rclpy.init(args=args)

    tester = TesterNode("test_node")

    rclpy.spin(tester)

    rclpy.shutdown
        