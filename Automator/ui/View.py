
from Automator.ui.threads import addLikeOnPostUIWorker
from Automator.WebAutomation import splitting
from Automator.Facebook.facebook import Facebook
from Automator.ui.MainUI.ui_Facebook_UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType

class AutomatorMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, accounts_file_path, accounts_data, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.accounts_data = accounts_data
        self.accounts_file_path = accounts_file_path

        self.setupUi(self)
        self.uiChanges()
        self.handleButtons()
        self.regexValidation()
    
    # def closeEvent(self, event):
    
    #     """UI close envet handler"""
    #     reply = QtWidgets.QMessageBox.question(
    #         self,
    #         "إغلاق",
    #         " تأكيد  ؟",
    #         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    #     )
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    def uiChanges(self):
        """UI changes after run the program"""
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame'))
        self.init_num_of_comments_txt1.setText('0')
        self.init_num_of_comments_txt2.setText('0')
        self.init_num_of_comments_txt3.setText('0')
        self.init_num_of_comments_txt4.setText('0')

        self.end_num_of_comments_txt1.setText(str(self.accounts_data.shape[0]))
        self.end_num_of_comments_txt2.setText(str(self.accounts_data.shape[0]))
        self.end_num_of_comments_txt3.setText(str(self.accounts_data.shape[0]))
        self.end_num_of_comments_txt4.setText(str(self.accounts_data.shape[0]))
        

    def handleButtons(self):
        self.comments_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame')))
        self.Likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'likes_frame')))
        self.comm_likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_likes_frame')))
        self.page_following_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'page_following_frame')))
        
        self.run_btn2.clicked.connect(self.addLikesOnPostUIworker)
        
    def regexValidation(self):
        """Apply regular expression to some UI elements"""
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('\d+'))
        self.init_num_of_comments_txt1.setValidator(validator)
        self.init_num_of_comments_txt2.setValidator(validator)
        self.init_num_of_comments_txt3.setValidator(validator)
        self.init_num_of_comments_txt4.setValidator(validator)

        self.end_num_of_comments_txt1.setValidator(validator)
        self.end_num_of_comments_txt2.setValidator(validator)
        self.end_num_of_comments_txt3.setValidator(validator)
        self.end_num_of_comments_txt4.setValidator(validator)
        
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.)(\w+)(.[a-zA-Z]{1,3})(\/[a-zA-Z0-9\.-]*)*'))
        self.post_url_txt1.setValidator(validator)
        self.post_url_txt2.setValidator(validator)
        self.post_url_txt3.setValidator(validator)
        self.page_url_txt.setValidator(validator)


    ############
    # comments #
    ############
    def addCommentsOnPostUIworker(self):
        start = self.init_num_of_comments_txt1.text()
        end = self.end_num_of_comments_txt1.text()
        Facebook(self.accounts_file_path).addCommentOnPostWorker(self.accounts_file_path[start:end], self.post_url_txt1, '..')


    ############
    # comments #
    ############
    def addLikesOnPostUIworker(self):
        url = self.post_url_txt2.text()
        start_num = self.init_num_of_comments_txt2.text()
        end_num = self.end_num_of_comments_txt2.text()
        if(url == ''):
            self.post_url_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(start_num == ''):
            self.init_num_of_comments_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.init_num_of_comments_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_num_of_comments_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.end_num_of_comments_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            return


        # Number of threads to be run
        NUM_OF_WORKERS = 1
        groups_items_df = splitting(self.accounts_data, NUM_OF_WORKERS)
        
        
        self.run_btn2.setEnabled(False)

        facebook = Facebook(self.accounts_file_path)

        # Creating threads
        for i in range(NUM_OF_WORKERS):

            worker = addLikeOnPostUIWorker(facebook, groups_items_df, start_num, end_num, i, url, self)
            worker.finished.connect(worker.deleteLater)
            worker.finished.connect(lambda : self.run_btn2.setEnabled(True))
            worker.finished.connect(lambda : facebook.driver.close())
            
            worker.start()
            
        
            










