import sys
from PySide6 import QtWidgets
from PySide6.QtCore import SIGNAL, QTimer
from PySide6.QtGui import QPainter, QPixmap, QColor, QPen
import collisions
from ui_mainwindow import Ui_MainWindow

RECT_HEIGHT = 100
RECT_WIDTH = 75
SCREEN_HEIGHT = 164
SCREEN_WIDTH = 700
SCREEN_XPOS = 700
SCREEN_YPOS = 250
WALL_XPOS = 0

class UI(QtWidgets.QMainWindow):
    def __init__(self, simulation):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.simulation = simulation
        self.pixmap = QPixmap(self.ui.animationLabel.size())
        self.massDisplay = self.ui.massDisplay
        self.massEditor = self.ui.massEditor
        self.speedDisplay = self.ui.speedDisplay
        self.speedSlider = self.ui.speedSlider
        self.restartButton = self.ui.restartButton

        self.setupDisplays()
        self.setupSimulation()
        self.setupInputs()

    def setupDisplays(self):
        self.massDisplay.setText(f"Mass of right rectangle : {100}kg (only estimates pi for powers of 100)")
        self.speedDisplay.setText(f"speed : {1}")
        self.massEditor.setText("100")
        self.pixmap.fill(QColor(255,255,255))
        self.ui.animationLabel.setPixmap(self.pixmap)

    def setupSimulation(self):
        self.simulationTimer = QTimer(self)
        self.simulationTimer.setInterval(10)
        self.simulationTimer.timeout.connect(self.animate)
        self.simulationTimer.start()

    def setupInputs(self):
        self.restartButton.clicked.connect(self.simulation.restart)
        self.speedSlider.valueChanged.connect(self.setSpeed)
        self.massEditor.textChanged.connect(self.changeMass)        

    def setSpeed(self, value):
        self.speedDisplay.setText(f"speed : {value}")
        self.simulationTimer.setInterval(10-value+1)

    def changeMass(self):
        if not self.massEditor.text().isnumeric():
            mass = 0
        else:
            mass = int(self.massEditor.text())
        collisions.changeMass(mass)
        collisions.restart()
        self.massDisplay.setText(f"Mass of right rectangle : {mass}kg")

    def animate(self):
        painter = QPainter(self.pixmap)
        leftPos, rightPos = self.simulation.simulate()
        self.pixmap.fill(QColor(255,255,255))
        painter.setPen(QPen(QColor(0,0,0), 5))
        painter.drawRect(WALL_XPOS + leftPos, SCREEN_HEIGHT, self.simulation.rectWidth, RECT_HEIGHT)
        painter.drawRect(WALL_XPOS + rightPos, SCREEN_HEIGHT, self.simulation.rectWidth, RECT_HEIGHT)
        painter.end()
        self.ui.animationLabel.setPixmap(self.pixmap)
        piEstimation = self.simulation.estimation()
        self.ui.piDisplay.setText(f"current value of pi : {piEstimation}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    collisions = collisions.Collisions()
    window = UI(collisions)
    window.show()
    sys.exit(app.exec())