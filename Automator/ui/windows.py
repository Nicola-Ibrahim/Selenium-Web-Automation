from Automator.ui.FacebookUI.view import AutomatorFacebookWindow
from Automator.ui.MainUI.view import AutomatorMainWindow

class Windows():
    def __init__(self):
        
        self.main_wind = AutomatorMainWindow()
        
        self.main_wind.show()

        self.handleButtons()

    def handleButtons(self):
        self.main_wind.facebook_btn.clicked.connect(self.main_wind.hide)
        self.main_wind.facebook_btn.clicked.connect(lambda : AutomatorFacebookWindow(self.main_wind).show())