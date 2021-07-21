
import os
import re

import pandas as pd
from Automator.ui.threads import LikesOnPostUIWorker, PageFollowingUIWorker
from Automator.WebAutomation import splitting
from Automator.Facebook.facebook import Facebook
from Automator.ui.MainUI.ui_Facebook_UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class AutomatorMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.accounts_file_path = None
        self.accounts_data = None
        self.comments_file_path = None
        self.comments_data = None

        self.setupUi(self)
        self.uiChanges()
        self.handleButtons()
        self.regexValidation()
        self.initialValues()
    
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
    
    def initialValues(self):
        """Initialize values for the text boxes"""
        self.start_acc_range_txt1.setText('0')
        self.start_acc_range_txt2.setText('0')
        self.start_acc_range_txt3.setText('0')
        self.start_acc_range_txt4.setText('0')

        if(self.accounts_data is not None):
            self.end_acc_range_txt1.setText(str(self.accounts_data.shape[0]))
            self.end_acc_range_txt2.setText(str(self.accounts_data.shape[0]))
            self.end_acc_range_txt3.setText(str(self.accounts_data.shape[0]))
            self.end_acc_range_txt4.setText(str(self.accounts_data.shape[0]))
        
        self.num_of_workers_txt1.setText('1')
        self.num_of_workers_txt2.setText('1')
        self.num_of_workers_txt3.setText('1')
        self.num_of_workers_txt4.setText('1')

    def handleButtons(self):
        self.comments_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame')))
        self.Likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'likes_frame')))
        self.comm_likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_likes_frame')))
        self.page_following_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'page_following_frame')))
        
        self.run_btn1.clicked.connect(self.addCommentsOnPostUIworker)
        self.run_btn2.clicked.connect(self.addLikesOnPostUIRun)
        self.run_btn3.clicked.connect(self.addLikesOnPostUIRun)
        self.run_btn4.clicked.connect(self.addLikesOnPostUIRun)

        self.load_accounts_file_btn.clicked.connect(self.readAccountDataFile)
        
    def regexValidation(self):
        """Apply regular expression to some UI elements"""

        # Set validation for checking number values
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('\d+'))
        self.start_acc_range_txt1.setValidator(validator)
        self.start_acc_range_txt2.setValidator(validator)
        self.start_acc_range_txt3.setValidator(validator)
        self.start_acc_range_txt4.setValidator(validator)

        self.end_acc_range_txt1.setValidator(validator)
        self.end_acc_range_txt2.setValidator(validator)
        self.end_acc_range_txt3.setValidator(validator)
        self.end_acc_range_txt4.setValidator(validator)
        

        # Set validation for checking url values
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.)(\w+)(.[a-zA-Z]{1,3})(\/[a-zA-Z0-9\.-]*)*'))
        self.post_url_txt1.setValidator(validator)
        self.post_url_txt2.setValidator(validator)
        self.post_url_txt3.setValidator(validator)
        self.page_url_txt4.setValidator(validator)


    ############
    # comments #
    ############
    def addCommentsOnPostUIworker(self):
        """Add likes on a post"""
        url = self.post_url_txt2.text()
        start_num = self.start_acc_range_txt2.text()
        end_num = self.end_acc_range_txt2.text()
        num_of_workers = self.num_of_workers_txt2.text()

        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(self.accounts_data is None):
            self.load_accounts_file_btn.setFocus()
            QtWidgets.QToolTip.showText(self.load_accounts_file_btn.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return

        
        elif(start_num == ''):
            self.start_acc_range_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.start_acc_range_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_acc_range_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            return
        
        elif(num_of_workers == ''):
            self.num_of_workers_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_workers_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        start_num = int(start_num)
        end_num = int(end_num)
        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[start_num:end_num]
        groups_items_df = splitting(data, num_of_workers)
        
        self.run_btn2.setEnabled(False)


        # Creating threads
        for i in range(num_of_workers):
            # Creating instance from the Facebook classs
            facebook = Facebook(self.accounts_file_path)
            
            worker = LikesOnPostUIWorker(facebook, groups_items_df, i, url, self)
            worker.finished.connect(lambda : self.run_btn2.setEnabled(True))
            worker.finished.connect(lambda : facebook.driver.close())
            worker.finished.connect(worker.deleteLater)
            
            worker.start()


    #########
    # Likes #
    #########
    def addLikesOnPostUIRun(self):
        """Add likes on a post"""
        url = self.post_url_txt2.text()
        start_num = self.start_acc_range_txt2.text()
        end_num = self.end_acc_range_txt2.text()
        num_of_workers = self.num_of_workers_txt2.text()

        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(self.accounts_data is None):
            self.load_accounts_file_btn.setFocus()
            QtWidgets.QToolTip.showText(self.load_accounts_file_btn.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return

        
        elif(start_num == ''):
            self.start_acc_range_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.start_acc_range_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_acc_range_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            return
        
        elif(num_of_workers == ''):
            self.num_of_workers_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_workers_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        start_num = int(start_num)
        end_num = int(end_num)
        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[start_num:end_num]
        groups_items_df = splitting(data, num_of_workers)
        
        self.run_btn2.setEnabled(False)


        # Creating threads
        for i in range(num_of_workers):
            
            worker = LikesOnPostUIWorker(self.accounts_file_path, groups_items_df[i], url, self)
            worker.finished.connect(lambda : self.run_btn2.setEnabled(True))
            worker.finished.connect(worker.deleteLater)
            
            worker.start()


    
    ###################
    # Page followings #
    ###################         
    def pageFollowingUIRun(self):
        """Add likes on a post"""
        url = self.post_url_txt4.text()
        start_num = self.start_acc_range_txt4.text()
        end_num = self.end_acc_range_txt4.text()
        num_of_workers = self.num_of_workers_txt4.text()

        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt4.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(self.accounts_data is None):
            self.load_accounts_file_btn.setFocus()
            QtWidgets.QToolTip.showText(self.load_accounts_file_btn.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return

        
        elif(start_num == ''):
            self.start_acc_range_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.start_acc_range_txt4.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_acc_range_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt4.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            return
        
        elif(num_of_workers == ''):
            self.num_of_workers_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_workers_txt4.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        start_num = int(start_num)
        end_num = int(end_num)
        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[start_num:end_num]
        groups_items_df = splitting(data, num_of_workers)
        
        self.run_btn4.setEnabled(False)


         # Creating threads
        for i in range(num_of_workers):
            
            worker = PageFollowingUIWorker(self.accounts_file_path, groups_items_df[i], url, self)
            worker.finished.connect(lambda : self.run_btn2.setEnabled(True))
            worker.finished.connect(worker.deleteLater)
            
            worker.start()


    def readAccountDataFile(self):
        """Read accounts data file"""

        # get the file name which is saved
        self.accounts_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,caption='Open file',
                    directory = os.path.join(os.getcwd(),'Automator/Facebook'),filter="XLSX files (*.xlsx)")
                
        # check if the file extension is an Excel file
        reg = re.compile(r"\.xlsx$")

        if (reg.search(self.accounts_file_path) is not None):
            self.accounts_data = pd.read_excel(self.accounts_file_path, usecols=['Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name', 'group'])

            # Reinialize values in text boxes
            self.initialValues()
    
    def readCommentsDataFile(self):
        """Read comments data file"""

        # get the file name which is saved
        self.comments_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,caption='Open file',
                    directory = os.path.join(os.getcwd(),'Automator/Facebook'),filter="XLSX files (*.xlsx)")
                
        # check if the file extension is an Excel file
        reg = re.compile(r"\.xlsx$")

        if (reg.search(self.comments_file_path) is not None):
            self.accounts_data = pd.read_excel(self.comments_data, usecols=['Comments'])

            # Reinialize values in text boxes
            self.initialValues()










