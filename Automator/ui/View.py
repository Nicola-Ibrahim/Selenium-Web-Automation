
import re

import pandas as pd
from Automator.ui.threads import CommentsOnPostWorker, LikesOnPostUIWorker, Likes_CommentsOnPostWorker, PageFollowingUIWorker
from Automator.ui.MainUI.ui_Facebook_UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from Automator.WebAutomation import splitting

class AutomatorMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.accounts_file_path = None
        self.accounts_data = None
        self.comments_file_path = None
        self.comments_data = None
        self.driver_type = None

        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

        self.setupUi(self)
        self.uiChanges()
        self.handleButtons()
        self.regexValidation()
        self.initialValues()
    
    def closeEvent(self, event):
    
        """UI close envet handler"""
        self.settings.setValue('facebook_file_path', self.accounts_file_path)
        self.settings.setValue('comments_file_path', self.comments_file_path)

        reply = QtWidgets.QMessageBox.question(
            self,
            "إغلاق",
            " تأكيد  ؟",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def uiChanges(self):
        """UI changes after run the program"""
        self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame'))
        
        self.settings.setValue('start_count', 1)
        # Centrize the dialog
        r = self.geometry()
        r.moveCenter(QtWidgets.QApplication.desktop().availableGeometry().center()) 
        self.setGeometry(r)
        
    def initialValues(self):
        """Initialize values for the text boxes"""
        self.start_acc_range_txt1.setText(str(self.settings.value('start_count')))
        self.start_acc_range_txt2.setText(str(self.settings.value('start_count')))
        self.start_acc_range_txt3.setText(str(self.settings.value('start_count')))
        self.start_acc_range_txt4.setText(str(self.settings.value('start_count')))

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
        self.run_btn3.clicked.connect(self.addLikes_CommentsOnPostUIRun)
        self.run_btn4.clicked.connect(self.addPageFollowingUIRun)

        self.load_accounts_file_btn1.clicked.connect(self.readAccountDataFile)
        self.load_accounts_file_btn2.clicked.connect(self.readAccountDataFile)
        self.load_accounts_file_btn3.clicked.connect(self.readAccountDataFile)
        self.load_accounts_file_btn4.clicked.connect(self.readAccountDataFile)
        
        self.load_commetns_file_btn1.clicked.connect(self.readCommentsDataFile)
        self.load_commetns_file_btn3.clicked.connect(self.readCommentsDataFile)
        
        
        self.facebook_btn.clicked.connect(lambda : self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'facebook_frame')))
        self.instagram_btn.clicked.connect(lambda : self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'instagram_frame')))
        
        self.facebook_btn.clicked.connect(self.selectDriverType)
        self.instagram_btn.clicked.connect(self.selectDriverType)
        
        
        self.return_btn1.clicked.connect(lambda : self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame')))

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
        # validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.)*(\w+)(.[a-zA-Z]{1,3})(\/[ء-يa-zA-Z0-9\.-=?_&#]*)*'))
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.facebook.com)(.)*'))
        self.post_url_txt1.setValidator(validator)
        self.post_url_txt2.setValidator(validator)
        self.post_url_txt3.setValidator(validator)
        self.page_url_txt4.setValidator(validator)


    def selectDriverType(self):
        self.driver_type = self.driver_type_comboBox.currentText()

    ####################
    # Facebook Workers #
    ####################
    def addCommentsOnPostUIworker(self):
        """Add comments on a post"""
        url = self.post_url_txt1.text()
        start_num = self.start_acc_range_txt1.text()
        end_num = self.end_acc_range_txt1.text()
        num_of_workers = self.num_of_workers_txt1.text()
        comments_type = self.comments_type_comboBox1.currentText()

        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(self.accounts_data is None):
            self.accounts_file_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.accounts_file_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter Facebook file")
            return
        
        elif(self.comments_data is None):
            self.comments_file_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.comments_file_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter Comments file")
            return

        
        elif(start_num == ''):
            self.start_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.start_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            return
        
        elif(num_of_workers == ''):
            self.num_of_workers_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_workers_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return
        
        elif(comments_type == ''):
            self.comments_type_comboBox1.currentText.setFocus()
            QtWidgets.QToolTip.showText(self.comments_type_comboBox1.currentText.mapToGlobal(QtCore.QPoint(0,10)),"Enter comments type")
            return

        start_num = int(start_num) - 1
        end_num = int(end_num)

        if(end_num <= start_num):
            self.end_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[start_num:end_num]
        groups_items_df = splitting(data, num_of_workers)
        
        self.run_btn2.setEnabled(False)


        # Creating threads
        for i in range(num_of_workers):
            # Creating instance from the Facebook classs
            
            worker = CommentsOnPostWorker(self.driver_type, self.accounts_file_path, groups_items_df[i], self.comments_data, comments_type, url, self)
            worker.finished.connect(lambda : self.run_btn2.setEnabled(True))
            worker.finished.connect(self.initialValues)
            worker.finished.connect(worker.deleteLater)
            
            worker.start()
  
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
            self.accounts_file_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.accounts_file_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter Facebook file")
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
        if(end_num <= start_num):
            self.end_acc_range_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt2.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[start_num:end_num]
        groups_items_df = splitting(data, num_of_workers)
        
        self.run_btn2.setEnabled(False)


        # Creating threads
        for i in range(num_of_workers):
            
            worker = LikesOnPostUIWorker(self.driver_type, self.accounts_file_path, groups_items_df[i], url, self)
            worker.finished.connect(lambda : self.run_btn2.setEnabled(True))
            worker.finished.connect(self.initialValues)
            worker.finished.connect(worker.deleteLater)
            worker.run_error.connect(lambda ind, name: self.run_error_lbl2.setText(f"Error occured at the account:: {ind} : {name}"))
            
            worker.start()

    def addLikes_CommentsOnPostUIRun(self):
        """Add likes and comments on a post"""
        url = self.post_url_txt3.text()
        start_num = self.start_acc_range_txt3.text()
        end_num = self.end_acc_range_txt3.text()
        num_of_workers = self.num_of_workers_txt3.text()
        comments_type = self.comments_type_comboBox2.currentText()

        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt3.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(self.accounts_data is None):
            self.accounts_file_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.accounts_file_txt3.mapToGlobal(QtCore.QPoint(0,10)),"Enter Facebook file")
            return
        
        elif(self.comments_data is None):
            self.comments_file_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.comments_file_txt3.mapToGlobal(QtCore.QPoint(0,10)),"Enter Comments file")
            return

        
        elif(start_num == ''):
            self.start_acc_range_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.start_acc_range_txt3.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_acc_range_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt3.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            return
        
        elif(num_of_workers == ''):
            self.num_of_workers_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_workers_txt3.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        elif(comments_type == ''):
            self.comments_type_comboBox2.currentText.setFocus()
            QtWidgets.QToolTip.showText(self.comments_type_comboBox2.currentText.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        start_num = int(start_num)
        end_num = int(end_num)
        if(end_num <= start_num):
            self.end_acc_range_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt3.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return
        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[start_num:end_num]
        groups_items_df = splitting(data, num_of_workers)
        
        self.run_btn3.setEnabled(False)


        # Creating threads
        for i in range(num_of_workers):
            # Creating instance from the Facebook classs
            
            worker = Likes_CommentsOnPostWorker(self.driver_type, self.accounts_file_path, groups_items_df[i], self.comments_data, comments_type, url, self)
            worker.finished.connect(lambda : self.run_btn3.setEnabled(True))
            worker.finished.connect(self.initialValues)
            worker.finished.connect(worker.deleteLater)
            
            worker.start()
  
    def addPageFollowingUIRun(self):
        """Add likes on a post"""
        url = self.page_url_txt4.text()
        start_num = self.start_acc_range_txt4.text()
        end_num = self.end_acc_range_txt4.text()
        num_of_workers = self.num_of_workers_txt4.text()

        # Check if any of the texts is empty
        if(url == ''):
            self.page_url_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.page_url_txt4.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(self.accounts_data is None):
            self.accounts_file_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.accounts_file_txt4.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
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
        if(end_num <= start_num):
            self.end_acc_range_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt4.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[start_num:end_num]
        groups_items_df = splitting(data, num_of_workers)
        
        self.run_btn4.setEnabled(False)


         # Creating threads
        for i in range(num_of_workers):
            
            worker = PageFollowingUIWorker(self.driver_type, self.accounts_file_path, groups_items_df[i], url, self)
            worker.finished.connect(lambda : self.run_btn4.setEnabled(True))
            worker.finished.connect(worker.deleteLater)
            
            worker.start()


    ###############
    # Read files #
    ##############
    def readAccountDataFile(self):
        """Read accounts data file"""

        # get the file name which is saved
        self.accounts_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,caption='Open file',
                    directory = self.settings.value('facebook_file_path'),filter="XLSX files (*.xlsx)")
                
        # check if the file extension is an Excel file
        reg = re.compile(r"\.xlsx$")
        
        if (reg.search(self.accounts_file_path) is not None):
            try:
                self.accounts_data = pd.read_excel(self.accounts_file_path, usecols=['Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name', 'group'])
                
                # Reinialize values in text boxes
                self.initialValues()


                # Set file path in text boxes and
                # change accounts file path text boxes properties
                text = self.accounts_file_path.split('/')[-1]
                for txt_box in [self.accounts_file_txt1, self.accounts_file_txt2, self.accounts_file_txt3, self.accounts_file_txt4]:
                    txt_box.setText(text)
                    txt_box.setStyleSheet("")

            except ValueError as e:
                for txt_box in [self.accounts_file_txt1, self.accounts_file_txt2, self.accounts_file_txt3, self.accounts_file_txt4]:
                    txt_box.setStyleSheet(
                        "QLineEdit {\n"
                        "    border-width: 4px; \n"
                        "    border-radius: 8px;\n"
                        "    border-style: solid;\n"
                        "    border-color: rgb(255,0,0);\n"
                        "    font-size: 25px;\n"
                        "}\n"
                        )
                    txt_box.setText('')
                    
    def readCommentsDataFile(self):
        """Read comments data file"""

        # get the file name which is saved
        self.comments_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,caption='Open file',
                    directory = self.settings.value('comments_file_path'),filter="XLSX files (*.xlsx)")
                
        # check if the file extension is an Excel file
        reg = re.compile(r"\.xlsx$")

        if (reg.search(self.comments_file_path) is not None):

            try: 
                self.comments_data = pd.read_excel(self.comments_file_path, usecols=['Comments', 'Type'])

                # Reinialize values in text boxes
                self.initialValues()


                # Set file path in text boxes and
                # change accounts file path text boxes properties
                text = self.comments_file_path.split('/')[-1]
                for txt_box in [self.comments_file_txt1, self.comments_file_txt3]:
                    txt_box.setText(text)
                    txt_box.setStyleSheet("")
            
                # Set type of comments in comboBoxes
                com_type = self.comments_data['Type'].unique()

                self.comments_type_comboBox1.clear()
                self.comments_type_comboBox2.clear()
                self.comments_type_comboBox1.addItems(com_type)
                self.comments_type_comboBox2.addItems(com_type)

            except ValueError as e:
                for txt_box in [self.comments_file_txt1, self.comments_file_txt3]:
                    txt_box.setStyleSheet(
                        "QLineEdit {\n"
                        "    border-width: 4px; \n"
                        "    border-radius: 8px;\n"
                        "    border-style: solid;\n"
                        "    border-color: rgb(255,0,0);\n"
                        "    font-size: 25px;\n"
                        "}\n"
                        )
                    txt_box.setText('')









