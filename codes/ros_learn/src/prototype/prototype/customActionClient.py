import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from prototype_interfaces.action import PrototypeAction


class MyActionClient(Node):

    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("这是此节点被启动时自动发送的一条信息，此节点的名字为%s。" % self.get_name())

        # 创建客户端
        self._action_client = ActionClient(self, PrototypeAction, 'dongzuo')


    def send_goal(self, order):

        # 初始化要发送的目标信息
        goal_msg = PrototypeAction.Goal()
        goal_msg.order = order

        # 等待动作服务器准备好
        self._action_client.wait_for_server()

        # 返回的是一个future对象
        future = self._action_client.send_goal_async(goal_msg)

        self._send_goal_future = future

        # 当请求受到回应时，调用指定的回调函数
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    # 请求被回应时调用的回调函数
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("请求被拒绝")
            return

        self.get_logger().info("请求被接受")

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.goal_result_callback)

    def goal_result_callback(self, future):
        result = future.result().result
        self.get_logger().info("已收到结果：{0}".format(result.sequence))

        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    action_client = MyActionClient("ClientNodeNameHere")

    action_client.send_goal(10)

    rclpy.spin(action_client)

    #rclpy.shutdown()


if __name__ == '__main__':
    main()
