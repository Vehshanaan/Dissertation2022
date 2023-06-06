import rclpy

from rclpy.node import Node

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt, QThread, pyqtSignal

from interfaces.msg import Slot


name_for_stdma_channel = "STDMA_Channel"


class RosThread(QThread):

    channel_message = pyqtSignal(dict)

# 创建一个节点，监听话题，并制造pyqtsignal
    def run(self):

        rclpy.init()
        self.node_ = rclpy.create_node("ChannelVisualiser")

        def callback(msg):
            msg_dict = {
                "slot_no": msg.slot_no,
                "slot_total": msg.slot_total,
                "sender_no": msg.sender_no,
            }
            self.channel_message.emit(msg_dict)

        self.subscribe_ = self.node_.create_subscription(
            Slot, name_for_stdma_channel, callback, 10)

        rclpy.spin(self.node_)
        rclpy.shutdown()


class VisualiserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Channel")
        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.inited = False
        self.ros_thread = RosThread()
        self.ros_thread.channel_message.connect(self.update_table)
        self.ros_thread.start()

    def update_table(self, msg_dict):
        # 根据收到的信息更新表格内容

        # 如果还没初始化：初始化
        if not self.inited:

            self.table.setRowCount(1)
            self.table.setColumnCount(msg_dict["slot_total"])

            # 初始化表格内容和背景色
            for row in range(self.table.rowCount()):
                for col in range(self.table.columnCount()):
                    item = QTableWidgetItem(str("inited"))
                    item.setBackground(QColor(0, 0, 255))  # 初始化背景色为蓝色
                    self.table.setItem(row, col, item)
                    print("%d,%d" % (row, col))

            self.inited = True


        # 根据收到的信息更新内容
        if msg_dict["sender_no"] == -1:
            color = QColor(255, 0, 0)  # 没人用的标红
            item = QTableWidgetItem("Not used yet")
            item.setBackground(color)

            self.table.setItem(0, msg_dict["slot_no"]-1, item)

        else:
            color = QColor(0, 255, 0)  # 有人用的标绿

            item = QTableWidgetItem(str(msg_dict["sender_no"]))  # 把归谁写上
            item.setBackground(color)

            self.table.setItem(0, msg_dict["slot_no"]-1, item)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()



def main(args=None):
    app = QApplication([])
    window = VisualiserWindow()
    window.show()

    app.exec()
