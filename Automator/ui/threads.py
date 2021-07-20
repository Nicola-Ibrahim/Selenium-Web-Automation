from Automator.Facebook.facebook import Facebook
import typing
from PyQt5 import QtCore

class addLikeOnPostUIWorker(QtCore.QThread):
    
    finished = QtCore.pyqtSignal()

    def __init__(self, facebook, groups_items_df, start_num: int, end_num: int, group_num: int, url: str,  parent: typing.Optional['QtCore.QObject']) :
        super().__init__(parent=parent)

        self.facebook = facebook
        self.groups_items_df = groups_items_df
        self.start_num = start_num
        self.end_num = end_num
        self.group_num = group_num
        self.url = url

    def run(self):
        
        self.facebook.addLikeOnPostWorker(self.groups_items_df[self.group_num][int(self.start_num):int(self.end_num)], self.url)
        self.finished.emit()

    
    

