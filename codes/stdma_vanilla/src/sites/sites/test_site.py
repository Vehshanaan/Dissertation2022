import rclpy

from rclpy.node import Node

from interfaces.srv import MapSending

class TesterNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("测试用节点，启动！")

        self.timer_period_ = 1

        self.client_ = self.create_client(MapSending,"MapSender")

        

        self.create_timer(self.timer_period_,self.timer_callback)

    def timer_callback(self):
        '''
        索要地图信息
        '''
        request = MapSending.Request()
        request.applicant = -1


        self.map_received_ = None


def main(args=None):

    rclpy.init(args=args)

    tester = TesterNode("test_node")

    rclpy.spin(tester)

    rclpy.shutdown
        