import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QPropertyAnimation, QPoint, QRect, QSize, Qt, SIGNAL, QObject, QTimer
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

class UI(QtWidgets.QMainWindow):
    def __init__(self, simulation):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.speed = 1
        self.simulation = simulation
        self.pixmap = QPixmap(self.ui.animationLabel.size())
        self.speedDisplay = self.ui.Editables.itemAt(2).widget()
        self.speedSlider = self.ui.Editables.itemAt(3).widget()
        self.massDisplay = self.ui.Editables.itemAt(0).widget()
        self.massEditor = self.ui.Editables.itemAt(1).widget()
        
        self.massDisplay.setText(f"Mass of right rectangle : {100}")
        self.massEditor.setPlaceholderText("100")
        #self.massEditor.setInputMask("9")
        self.pixmap.fill(QColor(255,255,255))
        # painter = QPainter(self.pixmap)
        self.ui.animationLabel.setPixmap(self.pixmap)

        self.simulationTimer = QTimer(self)
        self.simulationTimer.setInterval(10)
        self.simulationTimer.timeout.connect(self.animate)
        self.simulationTimer.start()

        self.massEditor.textChanged.connect(self.changeMass)

    def setSpeed(self, value):
        self.speedDisplay.setText(f"speed : {value}")

    def changeMass(self):
        mass = int(self.massEditor.text())
        collisions.changeMass(mass)
        collisions.restart()
        self.massDisplay.setText(f"Mass of right rectangle : {mass}")

    def animate(self):
        painter = QPainter(self.pixmap)
        leftPos, rightPos = self.simulation.animate()
        self.pixmap.fill(QColor(255,255,255))
        painter.drawRect(100 + leftPos, 100, RECT_WIDTH, RECT_HEIGHT)
        painter.drawRect(100 + rightPos, 100, RECT_WIDTH, RECT_HEIGHT)
        painter.end()
        self.ui.animationLabel.setPixmap(self.pixmap)
        self.ui.piDisplay.setText(f"current value of pi : {self.simulation.estimation}")
        self.speed = self.speedSlider.value()
        self.simulationTimer.setInterval(10-self.speed+1)
        self.speedDisplay.setText(f"speed : {self.speed}")

if __name__ == "__main__":
    #app = QtWidgets.QApplication([])
    app = QtWidgets.QApplication(sys.argv)
    collisions = collisions.Collisions(RECT_WIDTH)
    #mainWindow = MainWindowCol()
    #mainWindow.show()
    window = UI(collisions)
    window.show()
    sys.exit(app.exec())