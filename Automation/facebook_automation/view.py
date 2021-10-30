from Automation.facebook_automation.templates.FacebookUI.ui_Facebook_UI import Ui_MainWindow

from PyQt5 import QtWidgets

class AutomatorFacebookWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, main_wind, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.main_wind = main_wind