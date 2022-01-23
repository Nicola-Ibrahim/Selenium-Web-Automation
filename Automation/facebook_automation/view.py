from PyQt5 import QtCore, QtGui, QtWidgets
from typing import List

from Automation.facebook_automation.templates.FacebookUI.ui_Facebook_UI import Ui_MainWindow


class FacebookView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, controller, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.controller = controller

        self.setup()

    def setup(self):

        self.setupUi(self)
        self.custome_ui_changes()
        self.handle_buttons()
        self.regex_validation()
    

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
            # if(self.controller.main_wind != None):
            #     self.controller.main_wind.show()
        else:
            event.ignore()

    def custome_ui_changes(self):
        """UI changes after run the program"""

        self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame'))
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame'))
        
        # Resize tables view header sections into contentes
        self.accounts_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.accounts_tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        self.accounts_tableView.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)


        # self.controller.settings.setValue('current_acc_ind', 1)

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
        """Handle buttons signals"""

        # Panels buttons
        self.comments_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_frame')))
        self.likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'likes_frame')))
        self.comments_likes_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'comments_likes_frame')))
        self.page_following_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'page_following_frame')))
        self.groups_friends_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_add_friends_frame')))
        self.groups_comms_likes_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_likes_comments_frame')))

        self.groups_btn.clicked.connect(self.controller.show_facebook_accounts)

        # Run buttons
        self.add_comments_run_btn.clicked.connect(self.controller.add_comments_on_post)
        self.add_likes_run_btn.clicked.connect(self.controller.add_likes_on_post)
        self.add_likes_comments_run_btn.clicked.connect(self.controller.add_likes_comments_on_post)
        self.add_page_followings_run_btn.clicked.connect(self.controller.add_page_following)
        self.add_friendship_run_btn.clicked.connect(self.controller.addMulitpleFriendsUIRun)
        self.groups_add_likes_comments_run_btn.clicked.connect(self.controller.addLikes_CommentsOnFriendPostUIRun)

       
        
        # load accounts buttons
        self.load_accounts_file_btn.clicked.connect(self.controller.set_accounts_file_path)
        self.load_commetns_file_btn.clicked.connect(self.controller.set_comments_file_path)
        
        

        # Facebook main window buttons
        self.return_btn.clicked.connect(lambda : self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame')))
        self.next_btn.clicked.connect(self.controller.initial_facebook_values)

        # self.post_url_txt5.textChanged['QString'].connect(self.updateGroup)

    def regex_validation(self):
        """Apply regular expression to some UI elements"""

        # Set validation for checking accounts range
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('[1-9]\d+'))
        numericals_lst = [
            self.start_acc_range_txt1, 
            self.start_acc_range_txt2, 
            self.start_acc_range_txt3, 
            self.start_acc_range_txt4, 
            self.end_acc_range_txt1,
            self.end_acc_range_txt2,
            self.end_acc_range_txt3,
            self.end_acc_range_txt4
            ]
        for numeric_txt in numericals_lst:
            numeric_txt.setValidator(validator)


        # Set validation for checking url values
        # validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.)*(\w+)(.[a-zA-Z]{1,3})(\/[ء-يa-zA-Z0-9\.-=?_&#]*)*'))
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('(https://www.facebook.com)(.)*'))
        urls_lst = [self.post_url_txt1, self. post_url_txt2, self.post_url_txt3, self.page_url_txt4, self.post_url_txt5]
        for url_txt in urls_lst:
            url_txt.setValidator(validator)
       

    ####################
    # Facebook Workers #
    ####################
    def check_initial_facebook_values(self):
        if(self.adapter_name_txt.text() == ''):
            self.adapter_name_txt.setFocus()
            QtWidgets.QToolTip.showText(self.adapter_name_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter adapter name")
            return
        

        elif(self.accounts_file_txt.text() == ''):
            self.accounts_file_txt.setFocus()
            QtWidgets.QToolTip.showText(self.accounts_file_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter facebook accounts file path")
            return

        elif(self.comments_file_txt.text() == ''):
            self.comments_file_txt.setFocus()
            QtWidgets.QToolTip.showText(self.comments_file_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter facebook comments file path")
            return

        self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'facebook_frame'))
        
        return True

    def check_comments_on_post_args(self):
        """Check if any of comments panel's textBoxes is empty"""

        

        url = self.post_url_txt1.text()
        start_num = self.start_acc_range_txt1.text()
        end_num = self.end_acc_range_txt1.text()
        comments_type = self.comments_type_comboBox1.currentText()


        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            return
        
        elif(start_num == ''):
            self.start_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.start_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            return
        
        elif(end_num == ''):
            self.end_acc_range_txt1.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt1.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
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

        # Disable run button
        self.add_comments_run_btn.setEnabled(False)

        return True

    def check_likes_on_post_args(self):
        """Check if any of likes panel's textBoxes is empty"""



        url = self.post_url_txt2.text()
        start_num = self.start_acc_range_txt2.text()
        end_num = self.end_acc_range_txt2.text()


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
      

        
        start_num = int(start_num) - 1
        end_num = int(end_num)

        if(end_num <= start_num):
            self.end_acc_range_txt2.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt2.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

        # Disable run button
        self.add_likes_run_btn.setEnabled(False)

        return True

    def check_likes_comments_on_post_args(self):
        """Check if any of likes and comments panel's textBoxes is empty"""

        url = self.post_url_txt3.text()
        start_num = self.start_acc_range_txt3.text()
        end_num = self.end_acc_range_txt3.text()
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


        # Disable run button
        self.add_likes_comments_run_btn.setEnabled(False)

        return True

    def check_add_page_following_args(self):
        """Check if any of page following textBoxes is empty"""
        
        url = self.page_url_txt4.text()
        start_num = self.start_acc_range_txt4.text()
        end_num = self.end_acc_range_txt4.text()

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
        
        

        start_num = int(start_num) - 1
        end_num = int(end_num)

        if(end_num <= start_num):
            self.end_acc_range_txt4.setFocus()
            QtWidgets.QToolTip.showText(self.end_acc_range_txt4.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            return

        
        # Disable run button
        self.add_page_followings_run_btn.setEnabled(False)

        return True

    def set_accounts_model(self, model: QtCore.QSortFilterProxyModel):
        """Link accountes model to related view"""

        # Change current widget
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'accounts_groups_frame'))
        
        # Link view with related model
        self.accounts_tableView.setModel(model)
        

        # Change comboBox selected item actions
        self.groups_comboBox1.currentTextChanged['QString'].connect(lambda group_name: self.controller.facebook_accounts_sort_model.setAccountGroupFilter(group_name))
        self.groups_comboBox2.currentTextChanged['QString'].connect(lambda group_name: self.controller.facebook_accounts_sort_model.setAccountGroupFilter(group_name))

    def set_accounts_groups(self, groups: List[str]):
        """Set accounts groups in group comboBox"""
        for groups_combo in (self.groups_comboBox1, self.groups_comboBox2):
            groups.clear()
            groups_combo.addItems([''] + groups)
    
    def set_comments_in_comboBoxes(self, comments_type: List[str]):
        """Set type of comments in comboBoxes"""
        for comm_type in (self.comments_type_comboBox1, self.comments_type_comboBox2, self.comments_type_comboBox3):
            comm_type.clear()
            comm_type.addItems([''] + comments_type)