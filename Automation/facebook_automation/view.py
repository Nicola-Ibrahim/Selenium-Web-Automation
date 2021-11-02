from Automation.facebook_automation.templates.FacebookUI.ui_Facebook_UI import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

class AutomatorFacebookWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, main_wind, controller, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.main_wind = main_wind
        self.controller: AutomatorFacebookWindow = controller

        self.setupUi(self)
        
        self.uiChanges()
        self.initialValues()
        self.handleButtons()
        self.regexValidation()
    

    def closeEvent(self, event):
    
        """UI close envet handler"""
        

        reply = QtWidgets.QMessageBox.question(
            self,
            "Close",
            "Closing the app ?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            if(self.main_wind != None):
                self.main_wind.show()
        else:
            event.ignore()

    def ui_changes(self):
        """UI changes after run the program"""
        self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame'))
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame'))
        
        # Resize tables view header sections into contentes
        self.accounts_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.accounts_tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        self.accounts_tableView.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)


        self.settings.setValue('current_acc_ind', 1)

        # self.group_btn.hide()
        # Centrize the dialog
        r = self.geometry()
        r.moveCenter(QtWidgets.QApplication.desktop().availableGeometry().center()) 
        self.setGeometry(r)

        # # Read accounts and comments files
        # if(self.accounts_data != None or self.comments_data != None):
        #     self.readAccountDataFile()
        #     self.readCommentsDataFile()
        
    def handle_buttons(self):

        # Panels buttons
        self.comments_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame')))
        self.likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'likes_frame')))
        self.comments_likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_likes_frame')))
        self.page_following_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'page_following_frame')))
        self.groups_friends_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_add_friends_frame')))
        self.groups_comms_likes_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_likes_comments_frame')))

        self.groups_btn.clicked.connect(self.dispFacebookAccounts)

        # Run buttons
        self.add_comments_run_btn.clicked.connect(self.controller.add_comments_on_post)
        self.add_likes_run_btn.clicked.connect(self.controller.add_likes_on_post)
        self.add_likes_comments_run_btn.clicked.connect(self.controller.add_likes_comments_on_post)
        self.add_page_followings_run_btn.clicked.connect(self.controller.add_page_following)
        self.add_friendship_run_btn.clicked.connect(self.controller.addMulitpleFriendsUIRun)
        self.groups_add_likes_comments_run_btn.clicked.connect(self.controller.addLikes_CommentsOnFriendPostUIRun)

       
        
        # load accounts buttons
        self.load_accounts_file_btn.clicked.connect(self.controller.readAccountDataFile)
        self.load_commetns_file_btn.clicked.connect(self.controller.readCommentsDataFile)
        
        
        self.next_btn.clicked.connect(self.initial_facebook_values)

        self.return_btn.clicked.connect(lambda : self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame')))

        # self.post_url_txt5.textChanged['QString'].connect(self.updateGroup)

    def regex_validation(self):
        """Apply regular expression to some UI elements"""

        # Set validation for checking accounts range
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('[1-9]\d+'))
        self.start_acc_range_txt1.setValidator(validator)
        self.start_acc_range_txt2.setValidator(validator)
        self.start_acc_range_txt3.setValidator(validator)
        self.start_acc_range_txt4.setValidator(validator)

        self.end_acc_range_txt1.setValidator(validator)
        self.end_acc_range_txt2.setValidator(validator)
        self.end_acc_range_txt3.setValidator(validator)
        self.end_acc_range_txt4.setValidator(validator)
        
        # # Set validation for checking number of workers
        # validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('[1-4]{1}'))
        # self.num_of_workers_txt1.setValidator(validator)
        # self.num_of_workers_txt2.setValidator(validator)
        # self.num_of_workers_txt3.setValidator(validator)
        # self.num_of_workers_txt4.setValidator(validator)
        # self.num_of_workers_txt5.setValidator(validator)

        # Set validation for checking url values
        # validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.)*(\w+)(.[a-zA-Z]{1,3})(\/[ء-يa-zA-Z0-9\.-=?_&#]*)*'))
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.facebook.com)(.)*'))
        self.post_url_txt1.setValidator(validator)
        self.post_url_txt2.setValidator(validator)
        self.post_url_txt3.setValidator(validator)
        self.page_url_txt4.setValidator(validator)
        self.post_url_txt5.setValidator(validator)

    ####################
    # Facebook Workers #
    ####################
    def check_initial_facebook_values(self):
        if(self.adapter_name_txt.text()==''):
            self.adapter_name_txt.setFocus()
            QtWidgets.QToolTip.showText(self.adapter_name_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter adapter name")
            return

        elif(self.accounts_data is None):
            self.accounts_file_txt.setFocus()
            QtWidgets.QToolTip.showText(self.accounts_file_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter facebook accounts file path")
            return

        elif(self.comments_data is None):
            self.comments_file_txt.setFocus()
            QtWidgets.QToolTip.showText(self.comments_file_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter facebook comments file path")
            return

        self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'facebook_frame'))

    def check_comments_on_post_values(self):
        """Add comments on a post"""

        # Reset error text boxe
        self.run_error_lbl1.setText('')
        self.run_error_lbl1.setStyleSheet('')

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
        
        elif(start_num == ''):
            self.start_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.start_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            return
        
        elif(num_of_workers == ''):
            self.num_of_workers_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_workers_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return
        
        elif(comments_type == ''):
            self.comments_type_comboBox1.setFocus()
            QtWidgets.QToolTip.showText(self.comments_type_comboBox1.mapToGlobal(QtCore.QPoint(0,10)),"Enter comments type")
            return
    
    def check_likes_on_post_values(self):
        """Add likes on a post"""

        # Reset error text boxe
        self.run_error_lbl2.setText('')
        self.run_error_lbl2.setStyleSheet('')

        url = self.post_url_txt2.text()
        start_num = self.start_acc_range_txt2.text()
        end_num = self.end_acc_range_txt2.text()
        num_of_workers = self.num_of_workers_txt2.text()


        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt2.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
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

    def check_likes_comments_on_post_values(self):
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
            self.comments_type_comboBox2.setFocus()
            QtWidgets.QToolTip.showText(self.comments_type_comboBox2.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

    def check_add_page_following_values(self):
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

        start_num = int(start_num) - 1
        end_num = int(end_num)

        if(end_num <= start_num):
            self.end_acc_range_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt4.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

       