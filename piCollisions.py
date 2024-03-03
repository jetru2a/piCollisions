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
        leftPos, rightPos = self.simulation.animate(1)
        self.pixmap.fill(QColor(255,255,255))
        painter.drawRect(100 + leftPos, 100, RECT_WIDTH, RECT_HEIGHT)
        painter.drawRect(100 + rightPos, 100, RECT_WIDTH, RECT_HEIGHT)
        painter.end()
        self.ui.animationLabel.setPixmap(self.pixmap)
        self.ui.piDisplay.setText(f"current value of pi : {self.simulation.estimation}")

    #def animate(self):
    #    leftPos, rightPos = self.simulation.animate(1)


if __name__ == "__main__":
    #app = QtWidgets.QApplication([])
    app = QtWidgets.QApplication(sys.argv)
    collisions = collisions.Collisions(RECT_WIDTH)
    #mainWindow = MainWindowCol()
    #mainWindow.show()
    window = UI(collisions)
    window.show()
    sys.exit(app.exec())