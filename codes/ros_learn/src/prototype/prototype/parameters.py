import rclpy

from rclpy.node import Node


class MyParameter(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("这是此节点被启动时自动发送的一条信息，此节点的名字为%s。" % self.get_name())

        # （可选）加上参数的描述
        from rcl_interfaces.msg import ParameterDescriptor
        paramDesript = ParameterDescriptor(description="对参数的描述")

        # 参数初始化
        self.declare_parameter("parameter_name", 10, paramDesript)

        # 来复读一个一直输出并一直叠加参数值的函数
        self.timer = self.create_timer(1, self.timer_callback)

    # 被上述timer复读的一直输出并一直叠加参数值的函数
    def timer_callback(self):

        # 取得参数值
        param_value_prev = self.get_parameter(
            "parameter_name").get_parameter_value().integer_value

        self.get_logger().info("参数当前的值是%d，此后每次都会加一。" % param_value_prev)

        # 修改参数值
        param_new = rclpy.Parameter(
            "parameter_name", rclpy.Parameter.Type.INTEGER, param_value_prev+1)
        all_new_parameters=[param_new]
        self.set_parameters(all_new_parameters)


def main(args=None):

    rclpy.init(args=args)

    ParameterNode = MyParameter("NodeNameHere")

    rclpy.spin(ParameterNode)

    rcpy.shutdown()
