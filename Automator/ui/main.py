
import pandas as pd
from Automator.ui.View import AutomatorMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import sys

def uiMain():

    # Adjust window to screen
    os.environ["QtCore.QT_AUTO_SCREEN_SCALE_FACTOR"] = '1'
    # Enable High DPI display with PyQt5
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
    
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    main_win = AutomatorMainWindow()
    main_win.show()


    # Run the event loop
    sys.exit(app.exec_())