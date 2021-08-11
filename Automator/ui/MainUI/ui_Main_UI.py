# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/Main_UIvEJiEq.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 137)
        MainWindow.setStyleSheet("/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"\n"
"\n"
"\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(47, 113, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"    border-width: 4px; \n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-color: rgb(150,150,150);\n"
"    font-size: 25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-width: 4px; \n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-color: rgb(244, 154, 32);\n"
"    font-size: 25px;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QLabel {\n"
"    color:rgb(150,150,150);\n"
"    font-size: 25px;\n"
"\n"
"}\n"
"QSpinBox {\n"
"    padding-right: 10px; /* make room for the arrows */\n"
"    border-width: 6;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QToolTip {\n"
"    font: 12pt \"Times New Roman\";\n"
"    border: 2px solid rgb(174,174,174);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    font-size: 25px;\n"
"\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(150,150,150);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style:  solid;\n"
"    \n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(174,174,174);\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.instagram_btn = QtWidgets.QPushButton(self.frame_6)
        self.instagram_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.instagram_btn.setObjectName("instagram_btn")
        self.horizontalLayout.addWidget(self.instagram_btn)
        self.facebook_btn = QtWidgets.QPushButton(self.frame_6)
        self.facebook_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.facebook_btn.setObjectName("facebook_btn")
        self.horizontalLayout.addWidget(self.facebook_btn)
        self.verticalLayout.addWidget(self.frame_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(0, 81, 255);\n"
"padding: 5px;\n"
"font: 12pt \"Century Gothic\";")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.instagram_btn.setText(_translate("MainWindow", "Instagram"))
        self.facebook_btn.setText(_translate("MainWindow", "Facebook"))
        self.label.setText(_translate("MainWindow", "Created by Eng. Nicola Ibrahim"))

