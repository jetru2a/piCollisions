import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtQuick
from PySide6.QtCore import QPropertyAnimation, QPoint
from PySide6.QtWidgets import QWidget
import collisions

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.left = QWidget(self)
        self.left.setStyleSheet("background-color:red;border-radius:15px;")
        self.left.resize(100, 100)
        self.anim = QPropertyAnimation(self.left, b"pos")
        self.anim.setEndValue(QPoint(400,400))
        self.anim.setDuration(1500)
        self.anim.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    collisions = collisions.Collision()
    widget = MyWidget(collisions)
    widget.show()

    sys.exit(app.exec())