
import pandas as pd
from Automator.ui.View import AutomatorMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import sys

def uiMain():
    
    # Read accounts file
    accounts_file_path = "Automator/Facebook/Facebook Accounts.xlsx"
    accounts_data = pd.read_excel(accounts_file_path, usecols=['Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name', 'group'])
    
    # Adjust window to screen
    os.environ["QtCore.QT_AUTO_SCREEN_SCALE_FACTOR"] = '1'
    # Enable High DPI display with PyQt5
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
    
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    main_win = AutomatorMainWindow(accounts_file_path, accounts_data)
    main_win.show()


    # Run the event loop
    sys.exit(app.exec_())