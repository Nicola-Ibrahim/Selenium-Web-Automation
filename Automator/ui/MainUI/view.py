from Automator.ui.MainUI.ui_Main_UI import Ui_MainWindow

from PyQt5 import QtWidgets

class AutomatorMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)