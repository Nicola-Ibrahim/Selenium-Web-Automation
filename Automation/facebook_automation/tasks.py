
from PyQt5 import QtCore

from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from Automation.core.excel_file import SelectedData
from Automation.facebook_automation.facebook import FacbookAutomator
from Automation.core.mac_changer import MacChanger
from Automation.core.drivers import CustomeWebDriver
from Automation.facebook_automation.view import FacebookView


from itertools import combinations, groupby, permutations
from operator import itemgetter

from enum import Enum
from emoji.core import emojize




class AccountStatus(Enum):
    INACTIVE = 'Inactive'
    ACTIVE = 'Activer'


class FacebookInteraction(QtCore.QThread):
    """Creating thread for interacting in facebook website"""
    
    # Sends the account name and his index 
    run_error = QtCore.pyqtSignal(int, str)
    
    # Sends number of passed accounts that work
    passed_acc_counter = QtCore.pyqtSignal(int)

    def __init__(self, custom_driver: CustomeWebDriver, mac_changer: MacChanger, selected_data:SelectedData, settings: QtCore.QSettings, url: str, parent:FacebookView) :
        super().__init__(parent=parent)

        self.custom_driver: CustomeWebDriver = custom_driver
        self.mac_changer: MacChanger = mac_changer
        self.selected_data: SelectedData = selected_data
        self.settings: QtCore.QSettings = settings
        self.url: str = url
        self.counter: int = 0
        self.parent = parent
        
        self.custom_driver.init_driver()
        
        self.facebook: FacbookAutomator = FacbookAutomator(custom_driver.driver)

        self.setup_worker()

    def run(self):
        """Main runnable method to make interaction in Facebook website"""


        try:
            # Looping to each account
            for ind, row in self.selected_data.desire_accounts_data.iterrows():
                # start = perf_counter()

                if(row['Account status'] == AccountStatus.INACTIVE.value):
                    continue

                # Change MAC address (from execl or generate new one)
                old_mac_address, new_mac_address = self.mac_changer.change_address(row['Mac address'])
                self.facebook.logger_wrt_info(f"Old mac address: {old_mac_address}, New mac address: {new_mac_address}")

                # Put the new or old mac address in the related cell
                self.selected_data.accounts_file.sheet.cell(ind + 2, 13).value = new_mac_address if(new_mac_address != None) else ''

                
                # Login to the account
                self.facebook.login(row['Email'], row['Facebook password'])


                # self.settings.setValue('current_acc_ind', ind+1)

                # Check if the account is active
                if(self.facebook.is_account_active()):
                    self.selected_data.accounts_file.sheet.cell(ind + 2, 9).value = 'Active'
                    self.selected_data.accounts_file.sheet.cell(ind + 2, 7).value = self.facebook.get_profile_link()
                    
                    self.do_task()
                    
                    self.counter += 1
                    self.passed_acc_counter.emit(self.counter)

                else:
                    self.selected_data.accounts_file.sheet.cell(ind + 2, 9).value = 'Inactive'


                # finish = perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
                self.custom_driver.open_new_tab()
               
            
        except (NoSuchWindowException, WebDriverException):
            self.run_error.emit(row['Id'], row['Full name'])
        
        else:
            # self.settings.setValue('current_acc_ind', 1)
            self.custom_driver.close()
            
        finally:
            # self.selected_data.accounts_file.worker_book.save(self.selected_data.accounts_file.file_path)
            # self.selected_data.accounts_file.worker_book.close()
            self.finished.emit()


    def setup_worker(self):  
        self.connect()
        self.start()


    def do_task(self):
        """The main task to be executed"""

    def connect(self):
        """Connect the task with view components"""


class CommentOnPost(FacebookInteraction):
    def do_task(self):
        self.facebook.add_comment_on_post(self.url, emojize(self.selected_data.comments_file.data.sample(1)['Comments'].values[0], use_aliases=True))
        self.facebook.logger_wrt_info(f"{self.selected_data.comments_file.data.sample(1)['Comments'].values}")
        
    def connect(self):
        self.passed_acc_counter.connect(lambda count: self.parent.comments_counter_lbl.setText(f"{count}"))
        self.run_error.connect(lambda ind, name: self.parent.comments_error_lbl.setStyleSheet("color: rgb(255,0,0);"))
        self.run_error.connect(lambda ind, name: self.parent.comments_error_lbl.setText(f"Error occured at -> {ind} : {name}"))
        self.finished.connect(lambda: self.parent.add_comments_run_btn.setEnabled(True))
        self.finished.connect(self.deleteLater)


class LikeOnPost(FacebookInteraction):
    
    def do_task(self):
        self.facebook.add_like_on_post(self.url)
    
    def connect(self):
        self.passed_acc_counter.connect(lambda count: self.parent.likes_counter_lbl.setText(f"{count}"))
        self.run_error.connect(lambda ind, name: self.parent.likes_error_lbl.setStyleSheet("color: rgb(255,0,0);"))
        self.run_error.connect(lambda ind, name: self.parent.likes_error_lbl.setText(f"Error occured at -> {ind} : {name}"))
        self.finished.connect(lambda: self.parent.add_likes_run_btn.setEnabled(True))
        self.finished.connect(self.deleteLater)


class LikeAndCommentOnPost(FacebookInteraction):
    def do_task(self):
        self.facebook.add_like_on_post(self.url)
        self.facebook.add_comment_on_post(self.url, emojize(self.selected_data.comments_file.data.sample(1)['Comments'].values[0], use_aliases=True))
    
    def connect(self):
        self.passed_acc_counter.connect(lambda count: self.parent.comments_likes_counter_lbl.setText(f"{count}"))
        self.run_error.connect(lambda ind, name: self.parent.comments_likes_error_lbl.setStyleSheet("color: rgb(255,0,0);"))
        self.run_error.connect(lambda ind, name: self.parent.comments_likes_error_lbl.setText(f"Error occured at -> {ind} : {name}"))
        self.finished.connect(lambda: self.parent.add_likes_comments_run_btn.setEnabled(True))
        self.finished.connect(self.deleteLater)
    
class PageFollowing(FacebookInteraction):

    def do_task(self):
        self.facebook.add_page_following(self.url)
        self.facebook.add_like_on_page(self.url)

    def connect(self):

        self.passed_acc_counter.connect(lambda count: self.parent.page_followings_counter_lbl.setText(f"{count}"))
        self.run_error.connect(lambda ind, name : self.parent.page_folllowing_error_lbl.setStyleSheet("color: rgb(255,0,0);"))
        self.run_error.connect(lambda ind, name: self.parent.page_folllowing_error_lbl.setText(f"Error occured at -> {ind} : {name}"))
        self.finished.connect(lambda : self.parent.add_page_followings_run_btn.setEnabled(True))
        self.finished.connect(self.deleteLater)


class AddMulitpleFriendsWorker(QtCore.QThread):
    """Add many persons among each others at the same group"""

    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, parent, method = 'all') :
        """method : as default 'enhance'
            we can use ('enhanced2', 'all')
            enhanced2 -> it uses combinations to select available accounts for adding for each individual account
            all -> can implement add person or response to received friendship request 
        """
        super().__init__(parent=parent)

        self.facebook: FacebookInteraction = FacebookInteraction(driver_type, accounts_file_path, accounts_data)
        self.method = method
        self.settings = QtCore.QSettings('Viral.ini', QtCore.QSettings.IniFormat)


    def run(self):
        
        try:
            for group in self.facebook.accounts_data['Group'].unique():
                data = self.facebook.accounts_data[self.facebook.accounts_data['Group']==group]

                # Chose the one of the methods to be used 
                # indices_tree : [(1,2)(1,3), ..., (2,1)(2,3), ...]
                if(self.method == 'enhanced2'):
                    indices_tree = list(combinations(data['Id'].values, r=2))
                elif(self.method == 'all'):
                    indices_tree = list(permutations(data['Id'].values, r=2))

                # Obtain available accounts for adding for each individual one  
                # Get all acounts
                indices_all = {key: {val for _, val in values} for key, values in groupby(indices_tree, itemgetter(0))}
                # Get previously add accounts
                indices_prev = {key: set(map(float, str(val).split(','))) for key, val in zip(data.loc[:,'Id'], data.loc[:,'Added Friends'])}
                # Get new availble accounts
                indices_avaiable = {key: indices_all[key].difference(indices_prev[key]) for key in indices_all.keys()}

                # Iterate at each individual account
                for key in indices_avaiable.keys():
                    if(len(indices_avaiable[key]) != 0):
                        
                        new_mac_address = changeMac(self.facebook, self.adapter_name, data.loc[key-1,'Mac address'])
                
                        self.selected_data.sheet.cell(key + 1, 13).value = new_mac_address if(new_mac_address != None) else ''

                        self.facebook.login(email=data.loc[key-1,'Email'], password=data.loc[key-1,'Facebook password'])
                        
                        if(self.facebook.isAccountActive()):
                            self.selected_data.sheet.cell(key + 1, 8).value = 'Active'
                            self.selected_data.sheet.cell(key + 1, 6).value = self.facebook.getProfileLink()
                            
                            # Store all previouse accounts' ids and add new one to them
                            ids = [int(val) for val in indices_prev[key] if (not isnan(val))]
                            for val in indices_avaiable[key]:
                                self.facebook.addPerson(profile_path=data.loc[val - 1,'Profile path'])
                                self.facebook.acceptPerson(profile_path=data.loc[val - 1,'Profile path'])

                                ids.append(data.loc[val - 1, 'Id'])
                                
                                self.selected_data.sheet.cell(key + 1, 12).value = ','.join(list(map(str, ids)))

                            self.facebook.logout()
                                                        
                        else:
                            self.selected_data.sheet.cell(key + 2, 8).value = 'Inactive'
                            self.facebook.logout(active_acc=False)
                        
                        self.facebook.driver.delete_all_cookies()
                    
                        self.facebook.driver.execute_script("""window.open("https://www.facebook.com/","_blank")""")              
                        self.facebook.driver.close()
                        self.facebook.driver.switch_to_window(self.facebook.driver.window_handles[0])


        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(key + 1, data.loc[key, 'Full name'])
        
        else:
            self.facebook.driver.close()
            
        finally:
            self.selected_data.worker_book.save(self.facebook.accounts_file_path)
            self.selected_data.worker_book.close()
            self.finished.emit()

class AcceptMulitpleFriendsWorker(QtCore.QThread): 

    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, comments_type, url, parent) :
       
        super().__init__(parent=parent)

        self.facebook: FacebookInteraction = FacebookInteraction(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.comments_data = comments_data[comments_data['Type']==comments_type].loc[:, 'Comments'].values
        self.settings = QtCore.QSettings('Viral.ini', QtCore.QSettings.IniFormat)

    def run(self):
    
        try:
            for group in self.facebook.accounts_data['Group'].unique():
                data = self.facebook.accounts_data[self.facebook.accounts_data['Group']==group].reset_index(drop=True)
                comb = list(combinations(data.index.values[::-1], r=2))

                indices = {key: [val for _, val in values] for key, values in groupby(comb, itemgetter(0))}

                for key in indices.keys():
                    self.facebook._logger.info(f"login to person {key}")
                    self.facebook.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
                    
                    if(self.facebook.isAccountActive()):
                        self.selected_data.sheet.cell(key + 2, 8).value = 'Active'
                        self.selected_data.sheet.cell(key + 2, 6).value = self.facebook.getProfileLink()
                    
                        for val in indices[key]:
                            self.facebook._logger.info(f"add person {val}")
                            self.facebook.acceptPerson(profile_path=data.loc[val,'Profile path'])
                    
                        self.facebook._logger.info(f"""Logout from {key}""")
                        self.facebook.logout()

                    else:
                        self.selected_data.sheet.cell(key + 2, 8).value = 'Inactive'
                        self.facebook.logout(active_acc=False)

        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(key + 1, self.facebook.accounts_data.loc[key, 'Full name'])
    
        else:
            self.facebook.driver.close()
            
        finally:
            self.selected_data.worker_book.save(self.facebook.accounts_file_path)
            self.selected_data.worker_book.close()
            self.finished.emit()
     
class Likes_CommentsOnFriendPostWorker(QtCore.QThread):
    """A thread responsible for putting likes and comments on the friend post"""
    
    
    ### Signals to be emited if there any error occures
    # Sends the account name and his index 
    run_error = QtCore.pyqtSignal(int, str)
    
    # Sends number of passed accounts that work
    passed_acc_counter = QtCore.pyqtSignal(int)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, url, parent) :
        super().__init__(parent=parent)

        self.facebook: FacebookInteraction = FacebookInteraction(driver_type, accounts_file_path, accounts_data, comments_data)
        self.url = url
        self.settings = QtCore.QSettings('Viral.ini', QtCore.QSettings.IniFormat)

    def run(self):
        try:
            counter = 0
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = perf_counter()


                # Change MAC address for each individual account
                new_mac_address = changeMac(self.facebook, self.adapter_name, row['Mac address'])
                
                self.selected_data.sheet.cell(ind + 2, 13).value = new_mac_address if(new_mac_address != None) else ''

                self.facebook.login(email=row['Email'], password=row['Facebook password'])

                self.settings.setValue('current_acc_ind', ind+1)

                # Check if the account is active
                if(self.facebook.isAccountActive()):
                    self.selected_data.sheet.cell(ind + 2, 9).value = 'Active'
                    self.selected_data.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.addCommentOnPost(self.url, emojize(self.selected_data.comments_file.data.sample(1)['Comments'].values[0], use_aliases=True))
                    self.facebook.logout()
                    counter +=1
                    self.passed_acc_counter.emit(counter)
                else:
                    self.selected_data.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
    
                self.facebook.driver.delete_all_cookies()
            
                self.facebook.driver.execute_script("""window.open("https://www.facebook.com/","_blank")""")              
                self.facebook.driver.close()
                self.facebook.driver.switch_to_window(self.facebook.driver.window_handles[0])


        except (NoSuchWindowException, WebDriverException):
            self.run_error.emit(ind + 1, row['Full name'])
        
        else:
            self.settings.setValue('current_acc_ind', 1)
            self.facebook.driver.close()
            
        finally:
            self.selected_data.worker_book.save(self.facebook.accounts_file_path)
            self.selected_data.worker_book.close()
            self.finished.emit()
            


