import rclpy 

from rclpy.node import Node

from rclpy.action import ActionServer

from prototype_interfaces.action import PrototypeAction

import time

class MyActionServer(Node):

    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("这是此节点被启动时自动发送的一条信息，此节点的名字为%s。" % self.get_name())

        self._action_server = ActionServer(
            self,
            PrototypeAction,
            "dongzuo",
            self.execute_callback
        )
    
    def execute_callback(self, goal_handle): # 此方法在接受目标时被调用

        self.get_logger().info("正在执行goal...")

        # 算一下斐波那契数列
        feedback_msg = PrototypeAction.Feedback() # 初始化反馈对象

        feedback_msg.partial_sequence = [0, 1]

        # 生成数列
        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])

            self.get_logger().info('反馈：{0}'.format(feedback_msg.partial_sequence))

            goal_handle.publish_feedback(feedback_msg) # 发送反馈

            time.sleep(1)


        goal_handle.succeed() # 此句用来表示目标已达成

        # 返回结果：
        result = PrototypeAction.Result()
        result.sequence = feedback_msg.partial_sequence

        return result
    

def main(args=None):
    rclpy.init(args=args)

    ActionServerNode = MyActionServer("ActionServerNameHere")

    rclpy.spin(ActionServerNode)

if __name__ == "__main__":
    main()
