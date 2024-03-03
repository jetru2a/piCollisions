# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 868)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1030, 569, 311, 241))
        self.Editables = QVBoxLayout(self.verticalLayoutWidget)
        self.Editables.setSpacing(0)
        self.Editables.setObjectName(u"Editables")
        self.Editables.setContentsMargins(0, 0, 0, 0)
        self.massDisplay = QLabel(self.verticalLayoutWidget)
        self.massDisplay.setObjectName(u"massDisplay")

        self.Editables.addWidget(self.massDisplay)

        self.massEditor = QTextEdit(self.verticalLayoutWidget)
        self.massEditor.setObjectName(u"massEditor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.massEditor.sizePolicy().hasHeightForWidth())
        self.massEditor.setSizePolicy(sizePolicy)
        self.massEditor.setMaximumSize(QSize(16777215, 30))

        self.Editables.addWidget(self.massEditor)

        self.speedDisplay = QLabel(self.verticalLayoutWidget)
        self.speedDisplay.setObjectName(u"speedDisplay")

        self.Editables.addWidget(self.speedDisplay)

        self.speedSlider = QSlider(self.verticalLayoutWidget)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setOrientation(Qt.Horizontal)

        self.Editables.addWidget(self.speedSlider)

        self.animationLabel = QLabel(self.centralwidget)
        self.animationLabel.setObjectName(u"animationLabel")
        self.animationLabel.setGeometry(QRect(12, 0, 1021, 811))
        self.piDisplay = QLabel(self.centralwidget)
        self.piDisplay.setObjectName(u"piDisplay")
        self.piDisplay.setGeometry(QRect(1040, 0, 309, 211))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.massDisplay.setText(QCoreApplication.translate("MainWindow", u"Mass of right rectangle : ", None))
        self.speedDisplay.setText(QCoreApplication.translate("MainWindow", u"Speed : ", None))
        self.animationLabel.setText("")
        self.piDisplay.setText(QCoreApplication.translate("MainWindow", u"current value of pi : ", None))
    # retranslateUi

