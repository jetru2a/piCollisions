# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QLabel, QLineEdit,
    QMenuBar, QPushButton, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.animationLabel = QLabel(self.centralwidget)
        self.animationLabel.setObjectName(u"animationLabel")
        self.animationLabel.setGeometry(QRect(30, 30, 901, 271))
        self.animationLabel.setStyleSheet(u"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.piDisplay = QLabel(self.centralwidget)
        self.piDisplay.setObjectName(u"piDisplay")
        self.piDisplay.setGeometry(QRect(670, 330, 251, 41))
        self.piDisplay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.restartButton = QPushButton(self.centralwidget)
        self.restartButton.setObjectName(u"restartButton")
        self.restartButton.setGeometry(QRect(670, 400, 231, 71))
        font = QFont()
        font.setPointSize(12)
        self.restartButton.setFont(font)
        self.restartButton.setIconSize(QSize(20, 20))
        self.restartButton.setAutoDefault(False)
        self.speedDisplay = QLabel(self.centralwidget)
        self.speedDisplay.setObjectName(u"speedDisplay")
        self.speedDisplay.setGeometry(QRect(30, 330, 111, 21))
        self.speedSlider = QSlider(self.centralwidget)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setGeometry(QRect(30, 360, 319, 23))
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(10)
        self.speedSlider.setOrientation(Qt.Horizontal)
        self.speedSlider.setTickPosition(QSlider.TicksAbove)
        self.speedSlider.setTickInterval(0)
        self.massEditor = QLineEdit(self.centralwidget)
        self.massEditor.setObjectName(u"massEditor")
        self.massEditor.setGeometry(QRect(30, 440, 371, 28))
        self.massDisplay = QLabel(self.centralwidget)
        self.massDisplay.setObjectName(u"massDisplay")
        self.massDisplay.setGeometry(QRect(30, 400, 381, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.animationLabel.setText("")
        self.piDisplay.setText(QCoreApplication.translate("MainWindow", u"current value of pi : ", None))
        self.restartButton.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.speedDisplay.setText(QCoreApplication.translate("MainWindow", u"Speed : ", None))
        self.massDisplay.setText(QCoreApplication.translate("MainWindow", u"Mass of right rectangle : ", None))
    # retranslateUi

