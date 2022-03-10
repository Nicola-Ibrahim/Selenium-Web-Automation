from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Any, Dict, List, Union
from Automation.facebook_automation.exceptions import NotChosenException, UrlException

from Automation.facebook_automation.templates.FacebookUI.ui_Facebook_UI import Ui_MainWindow

class FacebookView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, controller, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.controller = controller

        self.setup()

    def setup(self):

        self.setupUi(self)
        self.custom_ui_changes()
        self.handle_buttons()
        # self.regex_validation()
    

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

    def custom_ui_changes(self):
        """UI changes after run the program"""

        self.social_media_stackedWidget.setCurrentWidget(self.social_media_stackedWidget.findChild(QtWidgets.QWidget, 'Main_frame'))
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'login_interaction_frame'))
        
        # Resize tables view header sections into content
        self.accounts_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.accounts_tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        self.accounts_tableView.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)

        self.post_comments_type_comboBox.setVisible(False)


        # self.group_btn.hide()
        # Centrize the dialog
        r = self.geometry()
        r.moveCenter(QtWidgets.QApplication.desktop().availableGeometry().center()) 
        self.setGeometry(r)


        
    def handle_buttons(self):
        """Handle buttons signals"""

        # Panels buttons
        self.login_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'login_interaction_frame')))
        self.post_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'post_interaction_frame')))
        self.page_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'page_interaction_frame')))
        self.groups_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, 'accounts_groups_frame')))

        # self.groups_friends_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_add_friends_frame')))
        # self.groups_comms_likes_btn.clicked.connect(lambda : self.accounts_groups_stackedWidget.setCurrentWidget(self.accounts_groups_stackedWidget.findChild(QtWidgets.QWidget, 'acc_groups_likes_comments_frame')))

        # self.groups_btn.clicked.connect(self.controller.show_facebook_accounts)

        # Run buttons
        # self.sign_in_btn.clicked.connect(self.controller.sign_in)
        self.post_run_btn.clicked.connect(self.controller.interact_w_post)
        self.page_run_btn.clicked.connect(self.controller.interact_w_page)
        # self.add_comments_run_btn.clicked.connect(self.controller.add_comments_on_post)
        # self.add_friendship_run_btn.clicked.connect(self.controller.addMulitpleFriendsUIRun)
        # self.groups_add_likes_comments_run_btn.clicked.connect(self.controller.addLikes_CommentsOnFriendPostUIRun)

       
        
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
        numerical_lst = [
            self.start_acc_range_txt1, 
            self.start_acc_range_txt2, 
            self.start_acc_range_txt3, 
            self.start_acc_range_txt4, 
            self.end_acc_range_txt1,
            self.end_acc_range_txt2,
            self.end_acc_range_txt3,
            self.end_acc_range_txt4
            ]
        for numeric_txt in numerical_lst:
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

    def check_on_post_args(self) -> Dict[str, Any]:
        """Check if any of post panel's componets is empty"""

        url = self.post_url_txt.text()
        start_num = self.post_start_acc_range_txt.text()
        end_num = self.post_end_acc_range_txt.text()
        comments_type = self.post_comments_type_comboBox.currentText()


        # Check if any of the texts is empty
        if(url == ''):
            self.post_url_txt.setFocus()
            QtWidgets.QToolTip.showText(self.post_url_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            raise UrlException("The url text is empty")
        
        elif(not self.post_like_checkBox.isChecked() and not self.post_comment_checkBox.isChecked()):
            self.post_like_checkBox.setFocus()
            QtWidgets.QToolTip.showText(self.post_like_checkBox.mapToGlobal(QtCore.QPoint(0,10)),"Select")
            raise NotChosenException("desire check box is selected")
        
        elif(self.post_comment_checkBox.isChecked() and comments_type == ''):
            self.post_comments_type_comboBox.setFocus()
            QtWidgets.QToolTip.showText(self.post_comments_type_comboBox.mapToGlobal(QtCore.QPoint(0,10)),"Select comments type")
            raise NotChosenException("The comments type not selected")


        elif(start_num == ''):
            self.post_start_acc_range_txt.setFocus()
            QtWidgets.QToolTip.showText(self.post_start_acc_range_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            raise ValueError("The starting range didn't enter")
        
        elif(end_num == ''):
            self.post_end_acc_range_txt.setFocus()
            QtWidgets.QToolTip.showText(self.post_end_acc_range_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            raise ValueError("The Ending range didn't enter")
        

        if(end_num <= start_num):
            self.post_end_acc_range_txt.setFocus()
            QtWidgets.QToolTip.showText(self.post_end_acc_range_txt.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            raise ValueError("The starting range is bigger than ending")

        
        values = {
            "url" : url,
            "start_num" : int(start_num),
            "end_num" : int(end_num),
            "likes" : self.post_like_checkBox.isChecked(),
            "comments" : self.post_comment_checkBox.isChecked(),
            "comments_type" : comments_type if(self.post_comment_checkBox.isChecked()) else None,
        }


        return values

    def check_on_page_args(self) -> Dict[str, Any]:
        """Check if any of post panel's componets is empty"""

        url = self.page_url_txt.text()
        start_num = self.page_start_acc_range_txt.text()
        end_num = self.page_end_acc_range_txt.text()


        # Check if any of the texts is empty
        if(url == ''):
            self.page_url_txt.setFocus()
            QtWidgets.QToolTip.showText(self.page_url_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter url")
            raise UrlException("The url text is empty")
                    
        elif(not self.page_like_checkBox.isChecked() and not self.page_follow_checkBox.isChecked()):
            self.page_like_checkBox.setFocus()
            QtWidgets.QToolTip.showText(self.page_like_checkBox.mapToGlobal(QtCore.QPoint(0,10)),"Select")
            raise NotChosenException("desire check box is selected")
            
        elif(start_num == ''):
            self.page_start_acc_range_txt.setFocus()
            QtWidgets.QToolTip.showText(self.page_start_acc_range_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter start number")
            raise ValueError("The starting range didn't enter")
        
        elif(end_num == ''):
            self.page_end_acc_range_txt.setFocus()
            QtWidgets.QToolTip.showText(self.page_end_acc_range_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter end number")
            raise ValueError("The Ending range didn't enter")
        
        if(end_num <= start_num):
            self.page_end_acc_range_txt.setFocus()
            QtWidgets.QToolTip.showText(self.page_end_acc_range_txt.mapToGlobal(QtCore.QPoint(0,10)),"set value bigger than start value")
            raise ValueError("The starting range is bigger than ending")
            

        values = {
            "url" : url,
            "start_num" : int(start_num),
            "end_num" : int(end_num),
            "like" : self.page_like_checkBox.isChecked(),
            "follow" : self.page_follow_checkBox.isChecked()
        }

        return values


    
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
        self.post_comments_type_comboBox.clear()
        self.post_comments_type_comboBox.addItems([''] + comments_type)