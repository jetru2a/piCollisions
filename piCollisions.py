import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QPropertyAnimation, QPoint, QRect, QSize, Qt
from PySide6.QtWidgets import QWidget, QMainWindow, QLabel
from PySide6.QtGui import QPainter, QPaintEvent, QPixmap, QColor, QColorConstants, QIcon
import collisions
from ui_mainwindow import Ui_MainWindow

RECT_HEIGHT = 100
RECT_WIDTH = 75
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700
SCREEN_XPOS = 700
SCREEN_YPOS = 250


# class Painter(QWidget):
#     def __init__(self, parent=None, ):
#         super().__init__(parent)


#     def paintEvent(self, event: QPaintEvent):
#         leftPos, rightPos = self.simulation.animate()
#         leftRect, rightRect = QRect(leftPos,100,RECT_WIDTH,RECT_HEIGHT), QRect(100,100,50,50)
#         QPainter.drawRect(leftRect)
#         QPainter.drawRect(rightRect)

class MainWindowCol(QtWidgets.QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setGeometry(SCREEN_XPOS, SCREEN_YPOS, SCREEN_HEIGHT, SCREEN_WIDTH)
        self.simulation = collisions
        self.pixmap = QPixmap(QSize(SCREEN_HEIGHT, SCREEN_WIDTH))
        label = QLabel(self)
        label.setPixmap(self.pixmap)
        self.setCentralWidget(label)
        color = QColor(0,125,10)
        self.pixmap.fill(color)
        #self.resize(600,600)
        #self.left = QWidget(self)
        #self.left.setStyleSheet("background-color:red;border-radius:15px;")
        #self.left.resize(50, 100)
        #self.painter = QPainter(self.simulationScreen)
        #self.painter.drawEllipse(0,0,128,128)


    #def animate(self):
    #   simulationScreen = self.

class UI(QtWidgets.QMainWindow):
    def __init__(self, simulation):
        super().__init__()
        self.simulation = simulation
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pixmap = QPixmap(self.ui.animationLabel.size())
        self.pixmap.fill(QColor(255,255,255))
        painter = QPainter(self.pixmap)
        self.ui.animationLabel.setPixmap(self.pixmap)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self.pixmap)
        painter.drawEllipse(0,0,128,128)
        painter.end()
        self.animate()
        self.ui.animationLabel.setPixmap(self.pixmap)

    def animate(self):
        leftPos, rightPos = self.simulation.animate(1)

if __name__ == "__main__":
    #app = QtWidgets.QApplication([])
    app = QtWidgets.QApplication(sys.argv)
    collisions = collisions.Collisions()
    #mainWindow = MainWindowCol()
    #mainWindow.show()
    window = UI(collisions)
    window.show()
    sys.exit(app.exec())