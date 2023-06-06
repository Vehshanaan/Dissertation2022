import rclpy

from rclpy.node import Node

from interfaces.msg import Slot

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6 import QtGui


name_for_stdma_channel = "STDMA_Channel"


class ChannelShow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        # 初始化表格
        self.inited = False

    def init_table(self, ColumnNum):
        self.table.setRowCount(1)
        self.table.setColumnCount(ColumnNum)

        # 设置表格内容和背景色
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                value = "Not used yet"
                item = QTableWidgetItem(str(value))
                item.setBackground(QtGui.QColor(255, 0, 0))  # 设置背景色为红色
                self.table.setItem(row, col, item)

        # 设置表格自适应大小
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        self.table.show()

        self.inited = True
        self.show()

    def update_cell(self, slot_num, node_num):

        if node_num == -1:
            color = QtGui.QColor(255, 0, 0)
        else:
            color = QtGui.QColor(0, 255, 0)

        item = QTableWidgetItem(str(node_num))
        item.setBackground(color)

        self.table.setItem(1, slot_num-1, item)

        self.table.show()


class ChannelVisualiser(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("信道可视化工具启动")

        self.subscriber_ = self.create_subscription(
            Slot, name_for_stdma_channel, self.subscriber_callback, 10)

        self.table = ChannelShow()

        self.table.show()

    def subscriber_callback(self, msg):
        self.received_msg = msg
        self.get_logger().info("msg received: slot %d/%d from site %d." %
                               (self.received_msg.slot_no, self.received_msg.slot_total, self.received_msg.sender_no))

        # 保存收到的信道信息
        self.frame_length_ = msg.slot_total
        self.current_slot_ = msg.slot_no
        if not hasattr(self, "occupied_"):
            self.occupied_ = [-1]*self.frame_length_

        self.occupied_[self.current_slot_-1] = msg.occupied
        # 更新信道可视化信息

        if not self.table.inited:
            self.table.init_table(self.frame_length_)

        # 设置格子内容
        # 当前格子上色
        # 如果没人用，设为红色
        # 如果有人用，设为绿色
        # 把用户编号写在格子里面
        self.table.update_cell(self.current_slot_, msg.occupied)
        self.table.show()


def main(args=None):

    app = QApplication([])

    rclpy.init(args=args)

    VisualiserInst = ChannelVisualiser("ChannelVisualiser")

    rclpy.spin(VisualiserInst)

    app.exec()

    rclpy.shutdown()
