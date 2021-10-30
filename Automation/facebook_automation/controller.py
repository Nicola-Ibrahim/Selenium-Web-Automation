
import pandas as pd
from Automation.core.ChangeMac import EthernetMacChanger, WifiMacChanger

from Automation.facebook_automation.model import FacebookAccountsModel, FacebookAccountsSortoModel
from Automation.facebook_automation.threads import AddMulitpleFriendsWorker, LikeOnPost, LikeAndCommentOnPost, CommentOnPost, PageFollowing
from Automation.facebook_automation.templates.FacebookUI.ui_Facebook_UI import Ui_MainWindow
from Automation.core.drivers import ChromeWebDriver, FirefoxWebDriver
from Automation.core.website_automator import enhanced_splitting 

from PyQt5 import QtCore, QtGui, QtWidgets


class AutomatorFacebookWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, main_wind, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.main_wind = main_wind

        # self.settings = QtCore.QSettings('Viral Co.', 'Viral app')
        self.settings = QtCore.QSettings('Viral.ini', QtCore.QSettings.IniFormat)

        self.accounts_file_path = self.settings.value('facebook_accounts_file_path')
        self.accounts_data = None
        self.comments_file_path = self.settings.value('facebook_comments_file_path')
        self.comments_data = None
        self.driver_type = None
        self.adapter_name = None

       
        self.facebook_accounts_sort_model = None
        
        self.setupUi(self)
        self.uiChanges()
        self.handleButtons()
        self.regexValidation()
        # self.initialValues()
    
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

    def uiChanges(self):
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
        
    def initialValues(self):
        """Initialize values for the text boxes"""
        self.start_acc_range_txt1.setText(str(self.settings.value('current_acc_ind')))
        self.start_acc_range_txt2.setText(str(self.settings.value('current_acc_ind')))
        self.start_acc_range_txt3.setText(str(self.settings.value('current_acc_ind')))
        self.start_acc_range_txt4.setText(str(self.settings.value('current_acc_ind')))

        if(self.accounts_data is not None):
            self.end_acc_range_txt1.setText(str(self.accounts_data.shape[0]))
            self.end_acc_range_txt2.setText(str(self.accounts_data.shape[0]))
            self.end_acc_range_txt3.setText(str(self.accounts_data.shape[0]))
            self.end_acc_range_txt4.setText(str(self.accounts_data.shape[0]))
        
        self.num_of_workers_txt1.setText('1')
        self.num_of_workers_txt2.setText('1')
        self.num_of_workers_txt3.setText('1')
        self.num_of_workers_txt4.setText('1')
        self.num_of_workers_txt5.setText('1')

        self.comments_counter_lbl.setText('0')
        self.likes_counter_lbl.setText('0')
        self.comments_likes_counter_lbl.setText('0')
        self.page_followings_counter_lbl.setText('0')
        self.groups_likes_comments_counter_lbl.setText('0')

    def handleButtons(self):

        # Panels buttons
        self.comments_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame')))
        self.likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'likes_frame')))
        self.comments_likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_likes_frame')))
        self.page_following_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'page_following_frame')))
        self.groups_friends_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_add_friends_frame')))
        self.groups_comms_likes_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_likes_comments_frame')))

        self.groups_btn.clicked.connect(self.dispFacebookAccounts)

        # Run buttons
        self.add_comments_run_btn.clicked.connect(self.addCommentsOnPostUIworker)
        self.add_likes_run_btn.clicked.connect(self.addLikesOnPostUIRun)
        self.add_likes_comments_run_btn.clicked.connect(self.addLikes_CommentsOnPostUIRun)
        self.add_page_followings_run_btn.clicked.connect(self.addPageFollowingUIRun)
        self.groups_add_likes_comments_run_btn.clicked.connect(self.addLikes_CommentsOnFriendPostUIRun)
        self.add_friendship_run_btn.clicked.connect(self.addMulitpleFriendsUIRun)

       
        
        # load accounts buttons
        self.load_accounts_file_btn.clicked.connect(self.readAccountDataFile)
        self.load_commetns_file_btn.clicked.connect(self.readCommentsDataFile)
        
        
        self.next_btn.clicked.connect(self.facebookPanel)

        self.return_btn.clicked.connect(lambda : self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame')))

        # self.post_url_txt5.textChanged['QString'].connect(self.updateGroup)

    def regexValidation(self):
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
    def facebookPanel(self):
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

        self.adapter_name = self.adapter_name_txt.text()
        self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'facebook_frame'))
    
    def addCommentsOnPostUIworker(self):
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

        start_num = int(start_num) - 1
        end_num = int(end_num)

        if(end_num <= start_num):
            self.end_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        accounts_data_splits = enhanced_splitting(self.accounts_data[start_num:end_num], num_of_workers)
        
        # Take commnets data as selected comments type data 
        comments_data_slices = self.comments_data[self.comments_data['Type']==comments_type]
        
        self.add_likes_run_btn.setEnabled(False)

        
        # Get the adapter name
        if(self.adapter_type_comboBox.currentText()=='Wi-Fi'):
            mac_changer = WifiMacChanger(self.adapter_name)
            
        elif(self.adapter_type_comboBox.currentText()=='Ethernet'):
            mac_changer = EthernetMacChanger(self.adapter_name)
        
        # Initializing a driver
        if(self.driver_type_comboBox.currentText() == 'Chrome'):
            driver = ChromeWebDriver()
        elif(self.driver_type_comboBox.currentText() == 'FireFox'):
            driver = FirefoxWebDriver()

        # Creating threads
        for i in range(num_of_workers):
            
            # worker = CommentsOnPostWorker(self.driver_type, self.accounts_file_path, accounts_data_splits[i], comments_data_slices, url, self)
            
            worker = CommentOnPost(driver, mac_changer, self.accounts_file_path, accounts_data_splits[i], comments_data_slices, url, self)
            worker.finished.connect(lambda : self.add_likes_run_btn.setEnabled(True))
            worker.finished.connect(self.initialValues)
            worker.finished.connect(worker.deleteLater)
            worker.passed_acc_counter.connect(lambda count: self.comments_counter_lbl.setText(f"{count}"))
            worker.run_error.connect(lambda ind, name : self.run_error_lbl1.setStyleSheet("color: rgb(255,0,0);"))
            worker.run_error.connect(lambda ind, name: self.run_error_lbl1.setText(f"Error occured at -> {ind} : {name}"))
            
            worker.start()
  
    def addLikesOnPostUIRun(self):
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

        start_num = int(start_num) - 1
        end_num = int(end_num)

        if(end_num <= start_num):
            self.end_acc_range_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt2.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        accounts_data_splits = enhanced_splitting(self.accounts_data[start_num:end_num], num_of_workers)
        

        self.add_likes_run_btn.setEnabled(False)


        # Get the adapter name
        if(self.adapter_type_comboBox.currentText()=='Wi-Fi'):
            mac_changer = WifiMacChanger(self.adapter_name)
            
        elif(self.adapter_type_comboBox.currentText()=='Ethernet'):
            mac_changer = EthernetMacChanger(self.adapter_name)
        
        # Initializing a driver
        if(self.driver_type_comboBox.currentText() == 'Chrome'):
            driver = ChromeWebDriver()
        elif(self.driver_type_comboBox.currentText() == 'FireFox'):
            driver = FirefoxWebDriver()


        # Creating threads
        for i in range(num_of_workers):
            
            worker = LikeOnPost(driver, mac_changer, self.accounts_file_path, accounts_data_splits[i], url, self)
            worker.passed_acc_counter.connect(lambda count: self.likes_counter_lbl.setText(f"{count}"))
            worker.run_error.connect(lambda ind, name : self.run_error_lbl2.setStyleSheet("color: rgb(255,0,0);"))
            worker.run_error.connect(lambda ind, name: self.run_error_lbl2.setText(f"Error occured at -> {ind} : {name}"))
            worker.finished.connect(lambda : self.add_likes_run_btn.setEnabled(True))
            worker.finished.connect(self.initialValues)
            worker.finished.connect(worker.deleteLater)
            worker.finished.connect(lambda : self.likes_counter_lbl.setText('0'))
            
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

        start_num = int(start_num) -1 
        end_num = int(end_num)

        if(end_num <= start_num):
            self.end_acc_range_txt3.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt3.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return
        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        accounts_data_splits = enhanced_splitting(self.accounts_data[start_num:end_num], num_of_workers)
        
        # Take commnets data as selected comments type data 
        comments_data_slices = self.comments_data[self.comments_data['Type']==comments_type]
        
        self.add_likes_comments_run_btn.setEnabled(False)


        # Get the adapter name
        if(self.adapter_type_comboBox.currentText()=='Wi-Fi'):
            mac_changer = WifiMacChanger(self.adapter_name)
            
        elif(self.adapter_type_comboBox.currentText()=='Ethernet'):
            mac_changer = EthernetMacChanger(self.adapter_name)
        
        # Initializing a driver
        if(self.driver_type_comboBox.currentText() == 'Chrome'):
            driver = ChromeWebDriver()
        elif(self.driver_type_comboBox.currentText() == 'FireFox'):
            driver = FirefoxWebDriver()


        # Creating threads
        for i in range(num_of_workers):
            # Creating instance from the Facebook classs
            
            worker = LikeAndCommentOnPost(driver, mac_changer, self.accounts_file_path, accounts_data_splits[i], comments_data_slices, url, self)
            worker.passed_acc_counter.connect(lambda count: self.comments_likes_counter_lbl.setText(f"{count}"))
            worker.finished.connect(lambda : self.add_likes_comments_run_btn.setEnabled(True))
            worker.finished.connect(self.initialValues)
            worker.finished.connect(worker.deleteLater)
            worker.run_error.connect(lambda ind, name : self.run_error_lbl3.setStyleSheet("color: rgb(255,0,0);"))
            worker.run_error.connect(lambda ind, name: self.run_error_lbl3.setText(f"Error occured at -> {ind} : {name}"))
            
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

        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        accounts_data_splits = enhanced_splitting(self.accounts_data[start_num:end_num], num_of_workers)
        
        
        self.add_page_followings_run_btn.setEnabled(False)


        # Get the adapter name
        if(self.adapter_type_comboBox.currentText()=='Wi-Fi'):
            mac_changer = WifiMacChanger(self.adapter_name)
            
        elif(self.adapter_type_comboBox.currentText()=='Ethernet'):
            mac_changer = EthernetMacChanger(self.adapter_name)
        
        # Initializing a driver
        if(self.driver_type_comboBox.currentText() == 'Chrome'):
            driver = ChromeWebDriver()
        elif(self.driver_type_comboBox.currentText() == 'FireFox'):
            driver = FirefoxWebDriver()
            
        # Creating threads
        for i in range(num_of_workers):
            
            # worker = PageFollowingUIWorker(self.driver_type, self.accounts_file_path, accounts_data_splits[i], url, self)
            worker = PageFollowing(driver, mac_changer, self.accounts_file_path, accounts_data_splits[i], url, self)
            worker.finished.connect(lambda : self.add_page_followings_run_btn.setEnabled(True))
            worker.finished.connect(worker.deleteLater)
            worker.passed_acc_counter.connect(lambda count: self.page_followings_counter_lbl.setText(f"{count}"))
            worker.run_error.connect(lambda ind, name : self.run_error_lbl4.setStyleSheet("color: rgb(255,0,0);"))
            worker.run_error.connect(lambda ind, name: self.run_error_lbl4.setText(f"Error occured at -> {ind} : {name}"))
            
            worker.start()

    def addMulitpleFriendsUIRun(self):
        """Add friends"""
       
        accounts_group = self.groups_comboBox1.currentText()

        # Check if any of the texts is empty
        if(accounts_group == ''):
            self.groups_comboBox1.setFocus()
            QtWidgets.QToolTip.showText(self.groups_comboBox1.mapToGlobal(QtCore.QPoint(0,10)),"Select a group")
            return


        # split accounts data frame into subsets depending on the number of threads
        accounts_data_splits = self.accounts_data[self.accounts_data['Group']==accounts_group]
        

        self.add_friendship_run_btn.setEnabled(False)


        # Creating threads
        for i in range(1):
            
            worker = AddMulitpleFriendsWorker(self.driver_type, self.accounts_file_path, accounts_data_splits, self)
            worker.finished.connect(lambda : self.add_friendship_run_btn.setEnabled(True))
            worker.finished.connect(worker.deleteLater)
            # worker.run_error.connect(lambda ind, name : self.run_error_lbl4.setStyleSheet("color: rgb(255,0,0);"))
            # worker.run_error.connect(lambda ind, name: self.run_error_lbl4.setText(f"Error occured at -> {ind} : {name}"))
            
            worker.start()

    def dispFacebookAccounts(self):
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'accounts_groups_frame'))
        self.facebook_accounts_sort_model = FacebookAccountsSortoModel(FacebookAccountsModel(self.accounts_data))
        self.accounts_tableView.setModel(self.facebook_accounts_sort_model)
        
        # Change comboBox selected item actions
        self.groups_comboBox1.currentTextChanged['QString'].connect(lambda group_name: self.facebook_accounts_sort_model.setAccountGroupFilter(group_name))
        self.groups_comboBox2.currentTextChanged['QString'].connect(lambda group_name: self.facebook_accounts_sort_model.setAccountGroupFilter(group_name))

    def addLikes_CommentsOnFriendPostUIRun(self):
        """Add likes and comments on a post"""
        url = self.post_url_txt5.text()
        num_of_comments = self.num_of_likes_comms_txt.text()
        num_of_workers = self.num_of_workers_txt5.text()
        comments_type = self.comments_type_comboBox3.currentText()
        accounts_group = self.groups_comboBox2.currentText()

        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt5.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt5.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        

        elif(num_of_comments == ''):
            self.num_of_likes_comms_txt.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_likes_comms_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
      
        elif(num_of_workers == ''):
            self.num_of_workers_txt5.setFocus()
            QtWidgets.QToolTip.showText(self.num_of_workers_txt5.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        elif(comments_type == ''):
            self.comments_type_comboBox3.setFocus()
            QtWidgets.QToolTip.showText(self.comments_type_comboBox3.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return
        
        elif(accounts_group == ''):
            self.groups_comboBox2.setFocus()
            QtWidgets.QToolTip.showText(self.groups_comboBox2.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        num_of_comments = int(num_of_comments)
        num_of_workers = int(num_of_workers)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[self.accounts_data['Group']==accounts_group].sample(num_of_comments)
        accounts_data_splits = enhanced_splitting(data, num_of_workers)
        
        # Take commnets data as selected comments type data 
        comments_data_slices = self.comments_data[self.comments_data['Type']==comments_type]
        
        self.groups_add_likes_comments_run_btn.setEnabled(False)


        # Creating threads
        for i in range(num_of_workers):
            # Creating instance from the Facebook classs
            
            worker = Likes_CommentsOnPostWorker(self.driver_type, self.accounts_file_path, accounts_data_splits[i], comments_data_slices, url, self)
            worker.finished.connect(lambda : self.groups_add_likes_comments_run_btn.setEnabled(True))
            worker.finished.connect(self.initialValues)
            worker.finished.connect(worker.deleteLater)
            worker.passed_acc_counter.connect(lambda count: self.groups_likes_comments_counter_lbl.setText(f"{count}"))
            worker.run_error.connect(lambda ind, name : self.run_error_lbl5.setStyleSheet("color: rgb(255,0,0);"))
            worker.run_error.connect(lambda ind, name: self.run_error_lbl5.setText(f"Error occured at -> {ind} : {name}"))
            
            worker.start()
    
    def updateGroup(self):
        """Updating group comboBox by capturing the account id from a url"""
        reg = QtCore.QRegularExpression("&id=\d+")
        match = reg.match(self.post_url_txt5.text()).capturedTexts()
        if(match):
            match = match[-1][1:]
            # group = self.accounts_data.loc[self.accounts_data['Profile path'].str.contains(pat = match), 'Group'].values[0]
            group = self.accounts_data.loc[self.accounts_data['Profile path'].str.contains(pat = match), 'Group'].values[0]
            self.groups_comboBox2.setCurrentText(group)

    ###############
    # Read files #
    ##############
    def readAccountDataFile(self):
        """Read accounts data file"""

        # get the file path if it is not known
        if(self.accounts_file_path in (None, '')):
            self.accounts_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,caption='Open file',
                        directory = self.settings.value('facebook_accounts_file_path'),filter="XLSX files (*.xlsx)")

            self.settings.setValue('facebook_accounts_file_path', self.accounts_file_path)
            self.settings.sync()

        # check if the file extension is an Excel file
        reg = QtCore.QRegularExpression("\.xlsx$")
        if(reg.match(self.accounts_file_path).hasMatch()):
            try:
                self.accounts_data = pd.read_excel(self.accounts_file_path, usecols=['Id', 'Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name', 'Group', 'Added Friends', 'Mac address'])
                self.accounts_data.dropna(thresh=4, inplace=True)
                
            except ValueError as e:
                self.accounts_file_txt.setStyleSheet(
                    "QLineEdit {\n"
                    "    border-width: 4px; \n"
                    "    border-radius: 8px;\n"
                    "    border-style: solid;\n"
                    "    border-color: rgb(255,0,0);\n"
                    "    font-size: 25px;\n"
                    "}\n"
                    )
                self.accounts_file_txt.setText('')
                self.accounts_file_path = None
                self.readAccountDataFile()    

            except FileNotFoundError as e:
                self.accounts_file_path = None
                self.readAccountDataFile() 

            else:
                # Reinialize values in text boxes
                self.initialValues()


                # Set accounts groups in group comboBox
                for groups in (self.groups_comboBox1, self.groups_comboBox2):
                    groups.clear()
                    groups.addItems([''] + self.accounts_data['Group'].unique().tolist())

                # Set file path in text boxes and
                # change accounts file path text boxes properties
                text = self.accounts_file_path.split('/')[-1]
                self.accounts_file_txt.setText(text)
                self.accounts_file_txt.setStyleSheet("")
    
    def readCommentsDataFile(self):
        """Read comments data file"""

        # get the file path
        if(self.comments_file_path in (None, '')):
            self.comments_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,caption='Open file',
                        directory = self.settings.value('facebook_comments_file_path'),filter="XLSX files (*.xlsx)")
            
            self.settings.setValue('facebook_comments_file_path', self.comments_file_path)
            self.settings.sync()
            
        # check if the file extension is an Excel file
        reg = QtCore.QRegularExpression("\.xlsx$")

        if (reg.match(self.comments_file_path).hasMatch()):

            try: 
                self.comments_data = pd.read_excel(self.comments_file_path, usecols=['Comments', 'Type'])
                self.comments_data.dropna(inplace=True)

                
            except ValueError:
                self.comments_file_txt.setStyleSheet(
                    "QLineEdit {\n"
                    "    border-width: 4px; \n"
                    "    border-radius: 8px;\n"
                    "    border-style: solid;\n"
                    "    border-color: rgb(255,0,0);\n"
                    "    font-size: 25px;\n"
                    "}\n"
                    )
                self.comments_file_txt.setText('')
                self.comments_file_path = None
                self.readCommentsDataFile()

            except FileNotFoundError:
                self.comments_file_path = None
                self.readCommentsDataFile()

            else:
                # Reinialize values in text boxes
                self.initialValues()


                # Set file path in text boxes and
                # change accounts file path text boxes properties
                text = self.comments_file_path.split('/')[-1]
                self.comments_file_txt.setText(text)
                self.comments_file_txt.setStyleSheet("")
            
                # Set type of comments in comboBoxes
                for comm_type in (self.comments_type_comboBox1, self.comments_type_comboBox2, self.comments_type_comboBox3):
                    comm_type.clear()
                    comm_type.addItems([''] + self.comments_data['Type'].unique().tolist())









