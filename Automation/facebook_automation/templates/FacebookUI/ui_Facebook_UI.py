# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Facebook_UIXHMZDL.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 791)
        MainWindow.setStyleSheet(u"/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"\n"
"\n"
"\n"
"QMainWindow {\n"
"\n"
"}\n"
"#stackedWidget, #main_buttons_frame{\n"
"	border: 4px solid;\n"
"	border-radius: 10px;\n"
"	border-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(100, 100, 100);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    color: rgb(255,255,255);\n"
"	\n"
"	background-color: rgb(47, 113, 255);\n"
"}\n"
"\n"
"QTableView{\n"
"	\n"
"	alternate-background-color : rgb(220, 220, 220); \n"
"	selection-background-color : 	rgb(174, 174, 174);     \n"
"\n"
"\n"
"	gridline-color: rgb(0, 31, 98);\n"
"\n"
"	font: 16pt \"Arial\";\n"
"	\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius:4px;\n"
"\n"
"	border-color: rgb(244, 154,"
                        " 32);\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(0, 31, 98) ;\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    border: 4px solid #6c6c6c;\n"
"	font: 75 18pt \"Arial\";\n"
"\n"
"	border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"	border-radius:4px;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: rgb(255, 170, 0);\n"
"	border-radius:4px;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    background:  rgb(244, 154, 32);\n"
"    border: 2px outset red;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QTreeView {\n"
"    show-decoration-selected:1;\n"
"	\n"
"	font: 16pt \"Times New Roman\";\n"
"}\n"
"\n"
"QTreeView::item {\n"
"     border: 1px solid #d9d9d9;\n"
"    bo"
                        "rder-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
"    border: 1px solid #bfcde4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    border: 1px solid #567dbc;\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image:url(:/icons/icons/vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/icons/icons/branch-more.png)  0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/icons/icons/branch-end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branc"
                        "h:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image:url(:/icons/icons/branch-closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"        border-image: none;\n"
"        image: url(:/icons/icons/branch-open.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox{\n"
"	\n"
"	font-size:25px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"	font-size: 14px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(95, 95, 95);\n"
"	border: 1px solid gray;\n"
"  	padding:  1em 1em;\n"
"  	border-radius: 16px;\n"
" }\n"
"\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad"
                        ", x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right"
                        "-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradie"
                        "nt(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-width: 4px; \n"
"	border-radius: 8px;\n"
"	border-style: solid;\n"
"	border-color: rgb(150,150,150);\n"
"	font-size: 25px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border-width: 4px; \n"
"	border-radius: 8px;\n"
"	border-style: solid;\n"
"	border-color: rgb(244, 154, 32);\n"
"	font-size: 25px;\n"
"	selection-background-color: darkgray;\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QLabel {\n"
"	color:rgb(150,150,150);\n"
"	font-size: 25px;\n"
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
"	font: 12pt \"Times New Roman\";\n"
"    border: 2px soli"
                        "d rgb(174,174,174);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QRadioButton {\n"
"	color: 000000;\n"
"	padding: 1px;\n"
"	font-size:25px;\n"
"\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	  width:25px;\n"
"    height: 25px;\n"
"\n"
"	border-style:solid;\n"
"	border-radius:14px;\n"
"	border-width: 2px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	  width:25px;\n"
"    height: 25px;\n"
"\n"
"	border-style:solid;\n"
"	border-radius:14px;\n"
"	border-width: 2px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
""
                        "\n"
"\n"
"QPushButton{\n"
"	font-size: 25px;\n"
"\n"
"	border-style: solid;\n"
"	border-width: 0px;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"	color: rgb(255,255,255);\n"
"	\n"
"	background-color: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:  solid;\n"
"	border-width: 0px;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(150,150,150);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style:  solid;\n"
"	\n"
"	border-width: 0px;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(174,174,174);\n"
"}\n"
"\n"
"\n"
"QLCDNumber {\n"
"	color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(230, 230, 230);\n"
"	border-style: solid;\n"
"	background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5"
                        ", y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"	color: #000000;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	border-bottom-co"
                        "lor: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #000000;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	color: #000000;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	\n"
"	background-color: rgb(224, 224, 224);\n"
"	\n"
"	\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(223,223,223);\n"
"		background-color:rgb(226,226,226);\n"
"		border-style: solid;\n"
"		border-width: 2px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	bo"
                        "rder-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	color: #000000;\n"
"	padd"
                        "ing: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-left-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, "
                        "x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:1px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));"
                        "\n"
"}\n"
"\n"
"\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, "
                        "x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-rad"
                        "ius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrol"
                        "lBar::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(3"
                        "4, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizon"
                        "tal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
" "
                        "  height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollB"
                        "ar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.social_media_stackedWidget = QStackedWidget(self.centralwidget)
        self.social_media_stackedWidget.setObjectName(u"social_media_stackedWidget")
        self.facebook_frame = QWidget()
        self.facebook_frame.setObjectName(u"facebook_frame")
        self.gridLayout_2 = QGridLayout(self.facebook_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_buttons_frame = QFrame(self.facebook_frame)
        self.main_buttons_frame.setObjectName(u"main_buttons_frame")
        self.main_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.main_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_buttons_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login_btn = QPushButton(self.main_buttons_frame)
        self.login_btn.setObjectName(u"login_btn")

        self.verticalLayout.addWidget(self.login_btn)

        self.post_btn = QPushButton(self.main_buttons_frame)
        self.post_btn.setObjectName(u"post_btn")
        self.post_btn.setMinimumSize(QSize(200, 50))

        self.verticalLayout.addWidget(self.post_btn)

        self.page_btn = QPushButton(self.main_buttons_frame)
        self.page_btn.setObjectName(u"page_btn")
        self.page_btn.setMinimumSize(QSize(200, 50))

        self.verticalLayout.addWidget(self.page_btn)

        self.groups_btn = QPushButton(self.main_buttons_frame)
        self.groups_btn.setObjectName(u"groups_btn")
        self.groups_btn.setEnabled(False)
        self.groups_btn.setMinimumSize(QSize(200, 50))

        self.verticalLayout.addWidget(self.groups_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.return_btn = QPushButton(self.main_buttons_frame)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setMinimumSize(QSize(200, 30))
        self.return_btn.setMaximumSize(QSize(150, 16777215))
        self.return_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.return_btn)


        self.gridLayout_2.addWidget(self.main_buttons_frame, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.facebook_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(100, 0))
        self.login_interaction_frame = QWidget()
        self.login_interaction_frame.setObjectName(u"login_interaction_frame")
        self.verticalLayout_13 = QVBoxLayout(self.login_interaction_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_7 = QFrame(self.login_interaction_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_5.addWidget(self.label_8)

        self.login_account_id_txt = QLineEdit(self.frame_13)
        self.login_account_id_txt.setObjectName(u"login_account_id_txt")
        self.login_account_id_txt.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_5.addWidget(self.login_account_id_txt)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(200, 0))
        self.label_9.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_6.addWidget(self.label_9)

        self.login_account_name_txt = QLineEdit(self.frame_13)
        self.login_account_name_txt.setObjectName(u"login_account_name_txt")

        self.horizontalLayout_6.addWidget(self.login_account_name_txt)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.sign_in_btn = QPushButton(self.frame_7)
        self.sign_in_btn.setObjectName(u"sign_in_btn")

        self.verticalLayout_12.addWidget(self.sign_in_btn)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_11)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.login_interaction_frame)
        self.post_interaction_frame = QWidget()
        self.post_interaction_frame.setObjectName(u"post_interaction_frame")
        self.verticalLayout_6 = QVBoxLayout(self.post_interaction_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_15 = QLabel(self.post_interaction_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_15)

        self.post_url_txt = QLineEdit(self.post_interaction_frame)
        self.post_url_txt.setObjectName(u"post_url_txt")
        self.post_url_txt.setMinimumSize(QSize(500, 50))

        self.verticalLayout_6.addWidget(self.post_url_txt)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.frame_26 = QFrame(self.post_interaction_frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_26)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.label_5 = QLabel(self.frame_26)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_5)

        self.post_like_checkBox = QCheckBox(self.frame_26)
        self.post_like_checkBox.setObjectName(u"post_like_checkBox")

        self.verticalLayout_3.addWidget(self.post_like_checkBox)

        self.frame_10 = QFrame(self.frame_26)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 11, 0, 11)
        self.post_comment_checkBox = QCheckBox(self.frame_10)
        self.post_comment_checkBox.setObjectName(u"post_comment_checkBox")

        self.horizontalLayout_8.addWidget(self.post_comment_checkBox)

        self.post_comments_type_comboBox = QComboBox(self.frame_10)
        self.post_comments_type_comboBox.setObjectName(u"post_comments_type_comboBox")
        self.post_comments_type_comboBox.setEnabled(True)
        self.post_comments_type_comboBox.setMinimumSize(QSize(250, 50))
        self.post_comments_type_comboBox.setMaximumSize(QSize(250, 16777215))
        self.post_comments_type_comboBox.setEditable(True)

        self.horizontalLayout_8.addWidget(self.post_comments_type_comboBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addWidget(self.frame_10)


        self.verticalLayout_6.addWidget(self.frame_26)

        self.frame_5 = QFrame(self.post_interaction_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.post_start_acc_range_txt = QLineEdit(self.frame_4)
        self.post_start_acc_range_txt.setObjectName(u"post_start_acc_range_txt")
        self.post_start_acc_range_txt.setMinimumSize(QSize(90, 50))
        self.post_start_acc_range_txt.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.post_start_acc_range_txt)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 50))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.post_end_acc_range_txt = QLineEdit(self.frame_4)
        self.post_end_acc_range_txt.setObjectName(u"post_end_acc_range_txt")
        self.post_end_acc_range_txt.setMinimumSize(QSize(90, 50))
        self.post_end_acc_range_txt.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.post_end_acc_range_txt)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.frame_11 = QFrame(self.post_interaction_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)

        self.post_accounts_num_lbl = QLabel(self.frame_11)
        self.post_accounts_num_lbl.setObjectName(u"post_accounts_num_lbl")
        self.post_accounts_num_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.post_accounts_num_lbl)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.frame_12 = QFrame(self.post_interaction_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.post_error_lbl = QLabel(self.frame_12)
        self.post_error_lbl.setObjectName(u"post_error_lbl")
        self.post_error_lbl.setMinimumSize(QSize(0, 50))

        self.verticalLayout_11.addWidget(self.post_error_lbl)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.frame_2 = QFrame(self.post_interaction_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(364, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.post_run_btn = QPushButton(self.frame_2)
        self.post_run_btn.setObjectName(u"post_run_btn")
        self.post_run_btn.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_2.addWidget(self.post_run_btn)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.post_interaction_frame)
        self.page_interaction_frame = QWidget()
        self.page_interaction_frame.setObjectName(u"page_interaction_frame")
        self.verticalLayout_17 = QVBoxLayout(self.page_interaction_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_18 = QLabel(self.page_interaction_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_18)

        self.page_url_txt = QLineEdit(self.page_interaction_frame)
        self.page_url_txt.setObjectName(u"page_url_txt")
        self.page_url_txt.setMinimumSize(QSize(500, 50))

        self.verticalLayout_17.addWidget(self.page_url_txt)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)

        self.frame_27 = QFrame(self.page_interaction_frame)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_27)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.label_10 = QLabel(self.frame_27)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_10)

        self.page_like_checkBox = QCheckBox(self.frame_27)
        self.page_like_checkBox.setObjectName(u"page_like_checkBox")

        self.verticalLayout_5.addWidget(self.page_like_checkBox)

        self.frame_14 = QFrame(self.frame_27)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 11, 0, 11)
        self.page_follow_checkBox = QCheckBox(self.frame_14)
        self.page_follow_checkBox.setObjectName(u"page_follow_checkBox")

        self.horizontalLayout_9.addWidget(self.page_follow_checkBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addWidget(self.frame_14)


        self.verticalLayout_17.addWidget(self.frame_27)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.frame_15 = QFrame(self.page_interaction_frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_11)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.page_start_acc_range_txt = QLineEdit(self.frame_16)
        self.page_start_acc_range_txt.setObjectName(u"page_start_acc_range_txt")
        self.page_start_acc_range_txt.setMinimumSize(QSize(90, 50))
        self.page_start_acc_range_txt.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.page_start_acc_range_txt)

        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(80, 50))
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.page_end_acc_range_txt = QLineEdit(self.frame_16)
        self.page_end_acc_range_txt.setObjectName(u"page_end_acc_range_txt")
        self.page_end_acc_range_txt.setMinimumSize(QSize(90, 50))
        self.page_end_acc_range_txt.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.page_end_acc_range_txt)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_15.addWidget(self.frame_16)


        self.verticalLayout_17.addWidget(self.frame_15)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_12)

        self.frame_17 = QFrame(self.page_interaction_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_16)

        self.page_accounts_num_lbl = QLabel(self.frame_17)
        self.page_accounts_num_lbl.setObjectName(u"page_accounts_num_lbl")
        self.page_accounts_num_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.page_accounts_num_lbl)


        self.verticalLayout_17.addWidget(self.frame_17)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_13)

        self.frame_19 = QFrame(self.page_interaction_frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_19)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, -1, 0, -1)
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)

        self.page_error_lbl = QLabel(self.frame_19)
        self.page_error_lbl.setObjectName(u"page_error_lbl")
        self.page_error_lbl.setMinimumSize(QSize(0, 50))

        self.verticalLayout_18.addWidget(self.page_error_lbl)


        self.verticalLayout_17.addWidget(self.frame_19)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.frame_3 = QFrame(self.page_interaction_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(364, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.page_run_btn = QPushButton(self.frame_3)
        self.page_run_btn.setObjectName(u"page_run_btn")
        self.page_run_btn.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_3.addWidget(self.page_run_btn)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_interaction_frame)
        self.accounts_groups_frame = QWidget()
        self.accounts_groups_frame.setObjectName(u"accounts_groups_frame")
        self.horizontalLayout_28 = QHBoxLayout(self.accounts_groups_frame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_32 = QFrame(self.accounts_groups_frame)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_32)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.groups_friends_btn = QPushButton(self.frame_32)
        self.groups_friends_btn.setObjectName(u"groups_friends_btn")
        self.groups_friends_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_7.addWidget(self.groups_friends_btn)

        self.groups_comms_likes_btn = QPushButton(self.frame_32)
        self.groups_comms_likes_btn.setObjectName(u"groups_comms_likes_btn")
        self.groups_comms_likes_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.groups_comms_likes_btn)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)


        self.horizontalLayout_28.addWidget(self.frame_32)

        self.accounts_groups_stackedWidget = QStackedWidget(self.accounts_groups_frame)
        self.accounts_groups_stackedWidget.setObjectName(u"accounts_groups_stackedWidget")
        self.acc_groups_add_friends_frame = QWidget()
        self.acc_groups_add_friends_frame.setObjectName(u"acc_groups_add_friends_frame")
        self.horizontalLayout_30 = QHBoxLayout(self.acc_groups_add_friends_frame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_21 = QFrame(self.acc_groups_add_friends_frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_21)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, -1, 0, -1)
        self.accounts_tableView = QTableView(self.frame_21)
        self.accounts_tableView.setObjectName(u"accounts_tableView")

        self.gridLayout_4.addWidget(self.accounts_tableView, 2, 0, 1, 1)

        self.frame_30 = QFrame(self.frame_21)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 11, 0, 11)
        self.label_26 = QLabel(self.frame_30)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_27.addWidget(self.label_26)

        self.groups_comboBox1 = QComboBox(self.frame_30)
        self.groups_comboBox1.setObjectName(u"groups_comboBox1")
        self.groups_comboBox1.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_27.addWidget(self.groups_comboBox1)


        self.gridLayout_4.addWidget(self.frame_30, 0, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_21)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, -1, 0, -1)
        self.label_27 = QLabel(self.frame_31)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_29.addWidget(self.label_27)

        self.add_friendship_run_btn = QPushButton(self.frame_31)
        self.add_friendship_run_btn.setObjectName(u"add_friendship_run_btn")

        self.horizontalLayout_29.addWidget(self.add_friendship_run_btn)


        self.gridLayout_4.addWidget(self.frame_31, 3, 0, 1, 1)


        self.horizontalLayout_30.addWidget(self.frame_21)

        self.accounts_groups_stackedWidget.addWidget(self.acc_groups_add_friends_frame)
        self.acc_groups_likes_comments_frame = QWidget()
        self.acc_groups_likes_comments_frame.setObjectName(u"acc_groups_likes_comments_frame")
        self.verticalLayout_8 = QVBoxLayout(self.acc_groups_likes_comments_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_28 = QLabel(self.acc_groups_likes_comments_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_28)

        self.post_url_txt5 = QLineEdit(self.acc_groups_likes_comments_frame)
        self.post_url_txt5.setObjectName(u"post_url_txt5")
        self.post_url_txt5.setMinimumSize(QSize(500, 50))

        self.verticalLayout_8.addWidget(self.post_url_txt5)

        self.frame_34 = QFrame(self.acc_groups_likes_comments_frame)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_32.setSpacing(7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 11, 0, 11)
        self.label_30 = QLabel(self.frame_34)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(400, 50))

        self.horizontalLayout_32.addWidget(self.label_30)

        self.num_of_likes_comms_txt = QLineEdit(self.frame_34)
        self.num_of_likes_comms_txt.setObjectName(u"num_of_likes_comms_txt")
        self.num_of_likes_comms_txt.setMinimumSize(QSize(90, 50))
        self.num_of_likes_comms_txt.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_32.addWidget(self.num_of_likes_comms_txt)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_16)


        self.verticalLayout_8.addWidget(self.frame_34)

        self.frame_24 = QFrame(self.acc_groups_likes_comments_frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_20.addWidget(self.label_24)

        self.groups_likes_comments_counter_lbl = QLabel(self.frame_24)
        self.groups_likes_comments_counter_lbl.setObjectName(u"groups_likes_comments_counter_lbl")

        self.horizontalLayout_20.addWidget(self.groups_likes_comments_counter_lbl)


        self.verticalLayout_8.addWidget(self.frame_24)

        self.frame_36 = QFrame(self.acc_groups_likes_comments_frame)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 50))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, -1, 0, -1)
        self.run_error_lbl5 = QLabel(self.frame_36)
        self.run_error_lbl5.setObjectName(u"run_error_lbl5")

        self.horizontalLayout_34.addWidget(self.run_error_lbl5)


        self.verticalLayout_8.addWidget(self.frame_36)

        self.frame_33 = QFrame(self.acc_groups_likes_comments_frame)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, -1, 0, -1)
        self.label_29 = QLabel(self.frame_33)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_31.addWidget(self.label_29)

        self.num_of_workers_txt5 = QLineEdit(self.frame_33)
        self.num_of_workers_txt5.setObjectName(u"num_of_workers_txt5")
        self.num_of_workers_txt5.setMinimumSize(QSize(90, 50))
        self.num_of_workers_txt5.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_31.addWidget(self.num_of_workers_txt5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_15)


        self.verticalLayout_8.addWidget(self.frame_33)

        self.frame_39 = QFrame(self.acc_groups_likes_comments_frame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_37.setSpacing(7)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 11, 0, 11)
        self.label_34 = QLabel(self.frame_39)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_37.addWidget(self.label_34)

        self.comments_type_comboBox3 = QComboBox(self.frame_39)
        self.comments_type_comboBox3.setObjectName(u"comments_type_comboBox3")
        self.comments_type_comboBox3.setMinimumSize(QSize(250, 50))

        self.horizontalLayout_37.addWidget(self.comments_type_comboBox3)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_19)


        self.verticalLayout_8.addWidget(self.frame_39)

        self.frame_35 = QFrame(self.acc_groups_likes_comments_frame)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 11, 0, 11)
        self.label_32 = QLabel(self.frame_35)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_33.addWidget(self.label_32)

        self.groups_comboBox2 = QComboBox(self.frame_35)
        self.groups_comboBox2.setObjectName(u"groups_comboBox2")
        self.groups_comboBox2.setMinimumSize(QSize(250, 50))

        self.horizontalLayout_33.addWidget(self.groups_comboBox2)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_18)


        self.verticalLayout_8.addWidget(self.frame_35)

        self.verticalSpacer_9 = QSpacerItem(20, 233, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.frame_37 = QFrame(self.acc_groups_likes_comments_frame)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(364, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_17)

        self.groups_add_likes_comments_run_btn = QPushButton(self.frame_37)
        self.groups_add_likes_comments_run_btn.setObjectName(u"groups_add_likes_comments_run_btn")
        self.groups_add_likes_comments_run_btn.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_35.addWidget(self.groups_add_likes_comments_run_btn)


        self.verticalLayout_8.addWidget(self.frame_37)

        self.accounts_groups_stackedWidget.addWidget(self.acc_groups_likes_comments_frame)

        self.horizontalLayout_28.addWidget(self.accounts_groups_stackedWidget)

        self.stackedWidget.addWidget(self.accounts_groups_frame)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.social_media_stackedWidget.addWidget(self.facebook_frame)
        self.stackedWidget.raise_()
        self.main_buttons_frame.raise_()
        self.Main_frame = QWidget()
        self.Main_frame.setObjectName(u"Main_frame")
        self.gridLayout_3 = QGridLayout(self.Main_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_27, 2, 0, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_28, 2, 2, 1, 1)

        self.frame_8 = QFrame(self.Main_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_7.addWidget(self.label_13)

        self.driver_type_comboBox = QComboBox(self.frame_9)
        self.driver_type_comboBox.setObjectName(u"driver_type_comboBox")
        self.driver_type_comboBox.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_7.addWidget(self.driver_type_comboBox)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_20)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.line_2 = QFrame(self.frame_8)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.frame_25 = QFrame(self.frame_8)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.label_31 = QLabel(self.frame_25)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_21.addWidget(self.label_31)

        self.adapter_name_txt = QLineEdit(self.frame_25)
        self.adapter_name_txt.setObjectName(u"adapter_name_txt")
        self.adapter_name_txt.setMinimumSize(QSize(300, 50))

        self.horizontalLayout_21.addWidget(self.adapter_name_txt)

        self.line = QFrame(self.frame_25)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(50, 0))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_21.addWidget(self.line)

        self.label_33 = QLabel(self.frame_25)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_21.addWidget(self.label_33)

        self.adapter_type_comboBox = QComboBox(self.frame_25)
        self.adapter_type_comboBox.addItem("")
        self.adapter_type_comboBox.addItem("")
        self.adapter_type_comboBox.setObjectName(u"adapter_type_comboBox")
        self.adapter_type_comboBox.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_21.addWidget(self.adapter_type_comboBox)


        self.verticalLayout_2.addWidget(self.frame_25)

        self.line_4 = QFrame(self.frame_8)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.frame_40 = QFrame(self.frame_8)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_38.setSpacing(20)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, -1, 0, -1)
        self.label_35 = QLabel(self.frame_40)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_38.addWidget(self.label_35)

        self.accounts_file_txt = QLineEdit(self.frame_40)
        self.accounts_file_txt.setObjectName(u"accounts_file_txt")
        self.accounts_file_txt.setMinimumSize(QSize(300, 50))
        self.accounts_file_txt.setReadOnly(True)

        self.horizontalLayout_38.addWidget(self.accounts_file_txt)

        self.load_accounts_file_btn = QPushButton(self.frame_40)
        self.load_accounts_file_btn.setObjectName(u"load_accounts_file_btn")
        self.load_accounts_file_btn.setMinimumSize(QSize(70, 50))

        self.horizontalLayout_38.addWidget(self.load_accounts_file_btn)


        self.verticalLayout_2.addWidget(self.frame_40)

        self.line_5 = QFrame(self.frame_8)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.frame_41 = QFrame(self.frame_8)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_39.setSpacing(20)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, -1, 0, -1)
        self.label_36 = QLabel(self.frame_41)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_39.addWidget(self.label_36)

        self.line_3 = QFrame(self.frame_41)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_39.addWidget(self.line_3)

        self.comments_file_txt = QLineEdit(self.frame_41)
        self.comments_file_txt.setObjectName(u"comments_file_txt")
        self.comments_file_txt.setMinimumSize(QSize(300, 50))
        self.comments_file_txt.setReadOnly(True)

        self.horizontalLayout_39.addWidget(self.comments_file_txt)

        self.load_commetns_file_btn = QPushButton(self.frame_41)
        self.load_commetns_file_btn.setObjectName(u"load_commetns_file_btn")
        self.load_commetns_file_btn.setMinimumSize(QSize(70, 50))

        self.horizontalLayout_39.addWidget(self.load_commetns_file_btn)


        self.verticalLayout_2.addWidget(self.frame_41)

        self.line_6 = QFrame(self.frame_8)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.next_btn = QPushButton(self.frame_6)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(200, 50))

        self.horizontalLayout.addWidget(self.next_btn)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.gridLayout_3.addWidget(self.frame_8, 2, 1, 1, 1)

        self.label_37 = QLabel(self.Main_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_37, 1, 1, 1, 1)

        self.social_media_stackedWidget.addWidget(self.Main_frame)

        self.verticalLayout_9.addWidget(self.social_media_stackedWidget)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: rgb(0, 81, 255);\n"
"padding: 5px;\n"
"font: 12pt \"Century Gothic\";")

        self.verticalLayout_9.addWidget(self.label_25)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 19))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.post_comment_checkBox.clicked.connect(self.post_comments_type_comboBox.setVisible)

        self.social_media_stackedWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        self.accounts_groups_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.post_btn.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.page_btn.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.groups_btn.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.return_btn.setText(QCoreApplication.translate("MainWindow", u"Reutrn", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT LOGIN", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Account ID:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.sign_in_btn.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"POST INTERACTION", None))
        self.post_url_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter post url", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Interaction Type", None))
        self.post_like_checkBox.setText(QCoreApplication.translate("MainWindow", u"LIkes", None))
        self.post_comment_checkBox.setText(QCoreApplication.translate("MainWindow", u"Comments", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Accounts range", None))
        self.post_start_acc_range_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"from", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.post_end_acc_range_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Num of passed accounts", None))
        self.post_accounts_num_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
        self.post_error_lbl.setText("")
        self.post_run_btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"PAGE INTERACTION", None))
        self.page_url_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter page url", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Interaction Type", None))
        self.page_like_checkBox.setText(QCoreApplication.translate("MainWindow", u"LIke", None))
        self.page_follow_checkBox.setText(QCoreApplication.translate("MainWindow", u"Follow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Accounts range", None))
        self.page_start_acc_range_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"from", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.page_end_acc_range_txt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Num of passed accounts", None))
        self.page_accounts_num_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
        self.page_error_lbl.setText("")
        self.page_run_btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.groups_friends_btn.setText(QCoreApplication.translate("MainWindow", u"Friends", None))
        self.groups_comms_likes_btn.setText(QCoreApplication.translate("MainWindow", u"Comments\n"
"and\n"
"Likes", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Account group", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Friendships", None))
        self.add_friendship_run_btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ADD COMMENTS and LIKES on fiends post", None))
        self.post_url_txt5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter post url", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Number of likes and comments", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Num of passed accounts:", None))
        self.groups_likes_comments_counter_lbl.setText("")
        self.run_error_lbl5.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"# of worker", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Comments Type", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Account group", None))
        self.groups_add_likes_comments_run_btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Select driver type", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Adapter name", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Adapter type", None))
        self.adapter_type_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Ethernet", None))
        self.adapter_type_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Wi-Fi", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Accounts file", None))
        self.load_accounts_file_btn.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Comments file", None))
        self.load_commetns_file_btn.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Created by Eng. Nicola Ibrahim", None))
    # retranslateUi

