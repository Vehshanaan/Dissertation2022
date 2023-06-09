import rclpy

from rclpy.node import Node

from prototype_interfaces.srv import PrototypeSrv


class MyClient(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("这是此节点被启动时自动发送的一条信息，此节点的名字为%s。" % self.get_name())

        # 创建客户端 回调函数在呼唤服务处调用，不在这里加入
        self.client_ = self.create_client(PrototypeSrv, "fuwu")

        self.money_to_lend_ = 10

    # 在这个函数中，节点呼唤服务
    def callService(self):
        self.get_logger().info('调用服务：想借%d' % self.money_to_lend_)

        # 在调用前先确定服务是否在线
        while not self.client_.wait_for_service(1):  # 当想调用的服务不在线时：
            # wait4service函数：只要超时或服务上线就立即返回值。服务在线就返回True，不在线就返回False
            self.get_logger().warn("想调用的服务不在线。")
        
        # 构造请求的内容

        # 新建请求对象 也可以把这个玩意儿变成类成员，然后再在调用服务的时候编辑其值
        request = PrototypeSrv.Request()
        # 填信息
        request.name = self.get_name()
        request.borrow = self.money_to_lend_

        # 发送异步服务请求
        self.client_.call_async(request).add_done_callback(self.client_callback)



    # 获得调用服务的返回的时候运行的回调函数
    def client_callback(self, future):
        # future是异步服务的执行返回结果，是某种占位符
        result = future.result() # 当future.done()为真的时候才有这个。其实我这么写鲁棒性一般
        if (result.lend_or_not):
            self.get_logger().info("能借钱，借了%d" % result.lend)
        else:
            self.get_logger().info("不借，没借着")



def main(args=None):

    rclpy.init(args=args)

    ClientNode = MyClient("ClientNodeNameHere")

    # 调用服务
    ClientNode.callService()

    rclpy.spin(ClientNode)

    rclpy.shutdown()

