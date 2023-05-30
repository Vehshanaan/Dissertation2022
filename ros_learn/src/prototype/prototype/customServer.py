import rclpy

from rclpy.node import Node

from prototype_interfaces.srv import PrototypeSrv

# 记得去修改package.xml，加上对服务功能包的依赖


class MyServer(Node):
    def __init__(self, name):
        # 初始化部分
        super().__init__(name)
        self.get_logger().info("这是此节点被启动时自动发送的一条信息，此节点的名字为%s。" % self.get_name())

        # 声明服务节点
        self.server_ = self.create_service(
            PrototypeSrv, "fuwu", self.server_callback)

        # 为了虚拟的使用场景，创建一个余额成员
        self.account = 10000  # 我是万元户

    # 服务的回调函数
    def server_callback(self, request, response):
        # request ： 来自客户端的请求数据
        self.get_logger().info("收到来自%s的借款申请，目前账户中有：%d，此人想借%d" %
                               (request.name, self.account, request.borrow))
        # response: 服务后的返回值

        response.lend_or_not = True
        # 没钱不借
        if (request.borrow >= self.account*0.1):
            response.lend_or_not = False
            self.get_logger().info("不借，爬吧")

        # 出账
        if (response.lend_or_not):
            self.account -= request.borrow
            response.lend = request.borrow
            self.get_logger().info("借出%d，还剩%d。" % (request.borrow, self.account))

        return response


def main(args=None):

    rclpy.init(args=args)

    server = MyServer("NodeNameHere")

    rclpy.spin(server)

    rclpy.shutdown()
