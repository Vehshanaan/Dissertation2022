from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QSizePolicy

from PyQt6 import QtGui

app = QApplication([])

table = QTableWidget(1, 5)
table.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])
table.setItem(0, 0, QTableWidgetItem('Item (0,0)'))
table.setItem(0, 1, QTableWidgetItem('Item (0,1)'))
table.setItem(0, 2, QTableWidgetItem('Item (0,2)'))
table.setItem(0, 3, QTableWidgetItem('Item (0,3)'))



item = QTableWidgetItem("Content for cell ({}, {})".format(0, 4))
item.setBackground(QtGui.QColor(255, 0, 0)) # set background color to red
table.setItem(0, 4, item)


item = QTableWidgetItem(str(-1))
item.setBackground(QtGui.QColor(255,0,0))

table.setItem(0, 4, item)
# Set the window size to fit the table
table.resizeColumnsToContents()
table.resizeRowsToContents()
table.show()

app.exec()

