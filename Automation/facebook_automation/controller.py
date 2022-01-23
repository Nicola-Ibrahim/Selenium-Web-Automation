
from Automation.core.excel_file import FacebookAccountsExcelFile, FacebookCommentsExcelFile, SelectedDataWithComments, SelectedDataWithoutComments
from Automation.core.mac_changer import EthernetMacChanger, MacChanger, WifiMacChanger
from Automation.facebook_automation.tasks import CommentOnPost, LikeAndCommentOnPost, LikeOnPost, PageFollowing
from Automation.core.drivers import ChromeWebDriver, CustomeWebDriver, FirefoxWebDriver

from Automation.facebook_automation.view import FacebookView
from Automation.facebook_automation.model import FacebookAccountsModel, FacebookAccountsSortoModel

from PyQt5 import QtCore, QtWidgets

from enum import Enum

class AdapterType(Enum):
    WIFI = 'Wi-Fi'
    ETHERNET = 'Ethernet'

class DriverType(Enum):
    CHROME = 'Chrome'
    FIREFOX = 'FireFox'

class FacebookController():
    def __init__(self):
        
        # View intialization
        self.view: FacebookView = FacebookView(self)

        # Models initialization
        self.accounts_base_model: FacebookAccountsModel = None
        self.accounts_sort_model: FacebookAccountsSortoModel = None
        
        # Create Setting file
        # self.settings = QtCore.QSettings('Viral Co.', 'Viral app')
        self.settings = QtCore.QSettings('Viral.ini', QtCore.QSettings.IniFormat)

        self.mac_changer: MacChanger = None
        self.custom_driver: CustomeWebDriver = None
        
       
        self.accounts_file: FacebookAccountsExcelFile = None
        self.comments_file: FacebookCommentsExcelFile = None
        
        self.setup()
    
    def setup(self):
        """Initial main values"""

        self.get_adapter_property()
        self.get_driver_property()

        # Set paths in textBoxes
        self.read_accounts_file()
        self.read_comments_file()
        self.set_post_url_txtBoxes()
        self.set_page_url_txtBoxes()

        # Show the facebook main windows
        self.view.show()

    def set_post_url_txtBoxes(self):
        
        for txt_box in (
            self.view.post_url_txt1,
            self.view.post_url_txt2, 
            self.view.post_url_txt3, 
        ):
            txt_box.setText(self.settings.value('post_url'))
    
    def set_page_url_txtBoxes(self):        
        self.view.post_url_txt5.setText(self.settings.value('post_url'))

    def set_adapter_property(self):
        """Set adapter's properties values """
        self.settings.setValue('adapter_name', self.view.adapter_name_txt.text())
        self.settings.setValue('adapter_type', self.view.adapter_type_comboBox.currentText())
        self.settings.sync()
  
    def get_adapter_property(self):
        """Get adapter's properties values"""        
        self.view.adapter_name_txt.setText(str(self.settings.value('adapter_name')))
        self.view.adapter_type_comboBox.setCurrentText(str(self.settings.value('adapter_type')))

    def set_driver_property(self):
        """Set custom_driver's properties values"""
        self.settings.setValue('driver_type', self.view.driver_type_comboBox.currentText())
        self.settings.sync()
  
    def get_driver_property(self):
        """Get custom_driver's properties values"""        
        self.view.driver_type_comboBox.setCurrentText(str(self.settings.value('driver_type')))


    def set_facbook_values(self):
        """Initialize values for the text boxes"""
        # self.view.start_acc_range_txt1.setText(str(self.settings.value('current_acc_ind')))
        # self.view.start_acc_range_txt2.setText(str(self.settings.value('current_acc_ind')))
        # self.view.start_acc_range_txt3.setText(str(self.settings.value('current_acc_ind')))
        # self.view.start_acc_range_txt4.setText(str(self.settings.value('current_acc_ind')))
        self.view.start_acc_range_txt1.setText('1')
        self.view.start_acc_range_txt2.setText('1')
        self.view.start_acc_range_txt3.setText('1')
        self.view.start_acc_range_txt4.setText('1')

        if(self.accounts_file.data is not None):
            self.view.end_acc_range_txt1.setText(str(self.accounts_file.data.shape[0]))
            self.view.end_acc_range_txt2.setText(str(self.accounts_file.data.shape[0]))
            self.view.end_acc_range_txt3.setText(str(self.accounts_file.data.shape[0]))
            self.view.end_acc_range_txt4.setText(str(self.accounts_file.data.shape[0]))
        
        self.view.num_of_workers_txt1.setText('1')
        self.view.num_of_workers_txt2.setText('1')
        self.view.num_of_workers_txt3.setText('1')
        self.view.num_of_workers_txt4.setText('1')
        self.view.num_of_workers_txt5.setText('1')

        self.view.comments_counter_lbl.setText('0')
        self.view.likes_counter_lbl.setText('0')
        self.view.comments_likes_counter_lbl.setText('0')
        self.view.page_followings_counter_lbl.setText('0')
        self.view.groups_likes_comments_counter_lbl.setText('0')

    def save_post_url(self, url):
        self.settings.setValue('post_url', url)
    
    def save_page_url(self, url):
        self.settings.setValue('page_url', url)
    

    ####################
    # Facebook Workers #
    ####################

    def initial_facebook_values(self):

        if(not self.view.check_initial_facebook_values()):
            return
        
        # Get the adapter name
        if(self.view.adapter_type_comboBox.currentText() == AdapterType.WIFI.value):
            self.mac_changer = WifiMacChanger(self.view.adapter_name_txt.text())
            
        elif(self.view.adapter_type_comboBox.currentText() == AdapterType.ETHERNET.value):
            self.mac_changer = EthernetMacChanger(self.view.adapter_name_txt.text())
        
        # Initializing a custom_driver
        if(self.view.driver_type_comboBox.currentText() == DriverType.CHROME.value):
            self.custom_driver = ChromeWebDriver()
        elif(self.view.driver_type_comboBox.currentText() == DriverType.FIREFOX.value):
            self.custom_driver = FirefoxWebDriver()

        
        self.set_adapter_property()
        self.set_driver_property()
    
    def add_comments_on_post(self):
        """Add comments on a post"""
        
        # Check if any of the text boxes is empty
        if(not self.view.check_comments_on_post_args()):
            return

        url = self.view.post_url_txt1.text()
        start_num = int(self.view.start_acc_range_txt1.text())
        end_num = int(self.view.end_acc_range_txt1.text())
        comments_type = self.view.comments_type_comboBox1.currentText()
        

        # Save post url
        self.save_post_url(url)
        
        # Reset view components' value
        # Reset passed accounts counter text box
        self.view.comments_counter_lbl.setText('0')
        # Reset error text box
        self.view.comments_error_lbl.setText('')
        self.view.comments_error_lbl.setStyleSheet('')

        selected_data = SelectedDataWithComments(self.accounts_file, start_num, end_num, self.comments_file, comments_type)

    
        CommentOnPost(
            self.custom_driver, 
            self.mac_changer, 
            selected_data,
            self.settings, 
            url,
            self.view,
        )
    
    def add_likes_on_post(self):
        """Add likes on a post"""

        if(not self.view.check_likes_on_post_args()):
            return

        url = self.view.post_url_txt2.text()
        start_num = int(self.view.start_acc_range_txt2.text())
        end_num = int(self.view.end_acc_range_txt2.text())

        # save post url in settings
        self.save_post_url(url)

        # Reset view components' value
        # Reset passed accounts counter text box
        self.view.likes_counter_lbl.setText('0')
        # Reset error text box
        self.view.likes_error_lbl.setText('')
        self.view.likes_error_lbl.setStyleSheet('')

        selected_data = SelectedDataWithoutComments(self.accounts_file, start_num, end_num)



        LikeOnPost(
            self.custom_driver, 
            self.mac_changer, 
            selected_data,
            self.settings, 
            url,
            self.view,
        )

    def add_likes_comments_on_post(self):
        """Add likes and comments on a post"""

        
        if(not self.view.check_likes_comments_on_post_args()):
            return


        url = self.view.post_url_txt3.text()
        start_num = int(self.view.start_acc_range_txt3.text())
        end_num = int(self.view.end_acc_range_txt3.text())
        comments_type = self.view.comments_type_comboBox2.currentText()

        # save post url in settings
        self.save_post_url(url)

        # Reset view components' value
        # Reset passed accounts counter text box
        self.view.comments_likes_counter_lbl.setText('0')
        # Reset error text box
        self.view.comments_likes_error_lbl.setText('')
        self.view.comments_likes_error_lbl.setStyleSheet('')

        selected_data = SelectedDataWithComments(self.accounts_file, start_num, end_num, self.comments_file, comments_type)

        # Creating thread                        
        LikeAndCommentOnPost(
            self.custom_driver, 
            self.mac_changer, 
            selected_data,
            self.settings, 
            url,
            self.view,
        )

    def add_page_following(self):
        """Add likes on a post"""

        if(self.view.check_add_page_following_args()):
            return

        url = self.view.page_url_txt4.text()
        start_num = int(self.view.start_acc_range_txt4.text())
        end_num = int(self.view.end_acc_range_txt4.text())

        # save post url in settings
        self.save_page_url(url)

        # Reset view components' value
        # Reset passed accounts counter text box
        self.view.page_followings_counter_lbl.setText('0')
        # Reset error text box
        self.view.page_folllowing_error_lbl.setText('')
        self.view.page_folllowing_error_lbl.setStyleSheet('')

        # Creating threads 
        selected_data = SelectedDataWithoutComments(self.accounts_file, start_num, end_num)
        
        PageFollowing(
            self.custom_driver, 
            self.mac_changer, 
            selected_data,
            self.settings, 
            url,
            self.view,
        )                       

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

    def show_facebook_accounts(self):
        self.accounts_base_model = FacebookAccountsModel(self.accounts_data)
        self.accounts_sort_model = FacebookAccountsSortoModel(self.accounts_base_model)
        self.view.set_accounts_model(self.accounts_sort_model)
        
    def addLikes_CommentsOnFriendPostUIRun(self):
        """Add likes and comments on a post"""
        url = self.post_url_txt5.text()
        num_of_comments = self.num_of_likes_comms_txt.text()
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
        
    
        elif(comments_type == ''):
            self.comments_type_comboBox3.setFocus()
            QtWidgets.QToolTip.showText(self.comments_type_comboBox3.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return
        
        elif(accounts_group == ''):
            self.groups_comboBox2.setFocus()
            QtWidgets.QToolTip.showText(self.groups_comboBox2.mapToGlobal(QtCore.QPoint(0,10)),"Enter number of workers")
            return

        num_of_comments = int(num_of_comments)


        # split accounts data frame into subsets depending on the number of threads
        data = self.accounts_data[self.accounts_data['Group']==accounts_group].sample(num_of_comments)
        accounts_data_splits = self.splitting_fn(data, num_of_workers)
        
        # Take commnets data as selected comments type data 
        comments_data_slices = self.comments_data[self.comments_data['Type']==comments_type]
        
        self.groups_add_likes_comments_run_btn.setEnabled(False)


        # Creating instance from the Facebook classs
        worker = LikeAndCommentOnPost(self.driver_type, self.accounts_file_path, accounts_data_splits[i], comments_data_slices, url, self)
        worker.finished.connect(lambda : self.groups_add_likes_comments_run_btn.setEnabled(True))
        worker.finished.connect(self.set_facbook_values)
        worker.finished.connect(worker.deleteLater)
        worker.passed_acc_counter.connect(lambda count: self.groups_likes_comments_counter_lbl.setText(f"{count}"))
        worker.run_error.connect(lambda ind, name : self.run_error_lbl5.setStyleSheet("color: rgb(255,0,0);"))
        worker.run_error.connect(lambda ind, name: self.run_error_lbl5.setText(f"Error occured at -> {ind} : {name}"))
        
        worker.start()
    
    def update_group(self):
        """Updating group comboBox by capturing the account id from a url"""

        reg = QtCore.QRegularExpression("&id=\d+")
        match = reg.match(self.post_url_txt5.text()).capturedTexts()
        if(match):
            match = match[-1][1:]
            # group = self.accounts_data.loc[self.accounts_data['Profile path'].str.contains(pat = match), 'Group'].values[0]
            group = self.accounts_data.loc[self.accounts_data['Profile path'].str.contains(pat = match), 'Group'].values[0]
            self.view.groups_comboBox2.setCurrentText(group)



    ##############
    # Read files #
    ##############
    def set_accounts_file_path(self):
        """Set accounts data file path"""

        # get the file path if it is not known
        if(self.accounts_file_path in (None, '')):
            self.accounts_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.view, caption='Open file',
                        directory = self.settings.value('facebook_accounts_file_path'),filter="XLSX files (*.xlsx)")

            self.settings.setValue('facebook_accounts_file_path', self.accounts_file_path)
            self.settings.sync()
    
            self.read_accounts_file()

    def read_accounts_file(self):
        """Read accounts data file"""

        self.accounts_file_path = self.settings.value('facebook_accounts_file_path')

        # check if the file extension is an Excel file
        reg = QtCore.QRegularExpression("\.xlsx$")
        if(not reg.match(self.accounts_file_path).hasMatch()):
            return

        try:
            self.accounts_file = FacebookAccountsExcelFile(self.accounts_file_path)
    
        # Exception if file is not follow the same structure as facebook accounts file
        except ValueError as e:
            self.view.accounts_file_txt.setStyleSheet(
                "QLineEdit {\n"
                "    border-width: 4px; \n"
                "    border-radius: 8px;\n"
                "    border-style: solid;\n"
                "    border-color: rgb(255,0,0);\n"
                "    font-size: 25px;\n"
                "}\n"
                )
            self.view.accounts_file_txt.setText('')
            self.accounts_file_path = None

        # Expection if file not found
        except FileNotFoundError as e:
            self.accounts_file_path = None
            QtWidgets.QMessageBox.warning(
                self.view,
                "Warning",
                "The facebook file is not existed !",
                QtWidgets.QMessageBox.Ok,
            )
            return
            


        else:
            # Reinialize values in text boxes
            self.set_facbook_values()

            self.view.set_accounts_groups(self.accounts_file.data['Group'].unique().tolist())

            # Set file path in text boxes and
            # change accounts file path text boxes properties
            text = self.accounts_file_path.split('/')[-1]

            self.view.accounts_file_txt.setText(text)
            self.view.accounts_file_txt.setStyleSheet("")

    def set_comments_file_path(self):
        """Set comments file path"""

        # get the file path
        if(self.comments_file_path in (None, '')):
            self.comments_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.view,caption='Open file',
                        directory = self.settings.value('facebook_comments_file_path'),filter="XLSX files (*.xlsx)")
            
            self.settings.setValue('facebook_comments_file_path', self.comments_file_path)
            self.settings.sync()
    
            self.read_comments_file()    
    
    def read_comments_file(self):
        """Read comments data file"""

        self.comments_file_path: str = self.settings.value('facebook_comments_file_path')
        
            
        # check if the file extension is an Excel file
        reg = QtCore.QRegularExpression("\.xlsx$")
        if (not reg.match(self.comments_file_path).hasMatch()):
            return

        try: 
            # self.comments_data = pd.read_excel(self.comments_file_path, usecols=['Comments', 'Type'])
            # self.comments_data.dropna(inplace=True)

            self.comments_file = FacebookCommentsExcelFile(self.comments_file_path)

            
        except ValueError:
            self.view.comments_file_txt.setStyleSheet(
                "QLineEdit {\n"
                "    border-width: 4px; \n"
                "    border-radius: 8px;\n"
                "    border-style: solid;\n"
                "    border-color: rgb(255,0,0);\n"
                "    font-size: 25px;\n"
                "}\n"
                )
            self.view.comments_file_txt.setText('')
            self.comments_file_path = None

        except FileNotFoundError:
            self.comments_file_path = None

        else:

            self.view.set_comments_in_comboBoxes(self.comments_file.data['Type'].unique().tolist())


            # Set file path in text boxes and
            # change accounts file path text boxes properties
            text = self.comments_file_path.split('/')[-1]
            self.view.comments_file_txt.setText(text)
            self.view.comments_file_txt.setStyleSheet("")
        









