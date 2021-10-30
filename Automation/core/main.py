from Automation.MainWind.view import AutomatorMainWindow
from Automation.facebook_automation.controller import AutomatorFacebookWindow

from PyQt5 import QtCore, QtWidgets
import os 
import sys



class Windows():
    def __init__(self):
        
        self.main_wind = AutomatorMainWindow()
        
        self.main_wind.show()

        self.handleButtons()

    def handleButtons(self):
        self.main_wind.facebook_btn.clicked.connect(self.main_wind.hide)
        self.main_wind.facebook_btn.clicked.connect(lambda : AutomatorFacebookWindow(self.main_wind).show())

def Main_run():

    # Adjust window to screen
    os.environ["QtCore.QT_AUTO_SCREEN_SCALE_FACTOR"] = '1'
    # Enable High DPI display with PyQt5
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
    
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Windows()
    
    main_wind = AutomatorFacebookWindow(None)
    
    main_wind.show()

    # Run the event loop
    sys.exit(app.exec_())