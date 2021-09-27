from time import sleep
from emoji.core import emojize
from numpy import isnan
from Automator.Auto_Core.ChangeMac import changeMacAddress
from PyQt5.QtCore import QSettings, QThread, pyqtSignal

from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from Automator.Facebook.facebook import Facebook

from itertools import combinations, groupby, permutations
from operator import itemgetter



def delete_cache(driver):
	driver.execute_script("window.open('');")
	sleep(1)
	driver.switch_to.window(driver.window_handles[-1])
	sleep(1)
	driver.get('chrome://settings/clearBrowserData')
	sleep(1)
	actions = ActionChains(driver) 
	actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
	actions.perform()
	sleep(1)
	actions = ActionChains(driver) 
	actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
	actions.perform()
	sleep(1) # wait some time to finish
	driver.close() # close this tab
	driver.switch_to.window(driver.window_handles[0]) # switch back
     

def changeMac(object, avaiable_mac):
    # Change MAC address (from execl or generate new one)
    desire_mac_address = str(avaiable_mac) if(type(avaiable_mac) == str) else None
    current_mac_address, new_mac_address = changeMacAddress(desire_mac_address=desire_mac_address, change_wifi=False, change_ethernet=True)

    # We renavigate to facebook website because it will be crashed by the enternet disconnection
    object.driver.get(object.website)

    return new_mac_address


class LikesOnPostUIWorker(QThread):
    """A thread responsible for putting likes of post"""

    
    ### Signals to be emited if there any error occures
    # Sends the account name and his index 
    run_error = pyqtSignal(int, str)
    
    # Sends number of passed accounts that work
    passed_acc_counter = pyqtSignal(int)

    def __init__(self, driver_type, accounts_file_path, accounts_data, url,  parent) :
        super().__init__(parent=parent)

        
        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.settings = QSettings('Viral Co.', 'Viral app')

    def run(self):
        try:
            counter = 0
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = perf_counter()
                new_mac_address = changeMac(self.facebook, row['Mac address'])

                self.facebook.sheet.cell(ind + 2, 13).value = new_mac_address if(new_mac_address != None) else ''

                self.facebook.login(email=row['Email'], password=row['Facebook password'])

                self.settings.setValue('current_acc_ind', ind+1)

                # Check if the account is active
                if(self.facebook.isAccountActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.logout()
                    counter +=1
                    self.passed_acc_counter.emit(counter)

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)


                # finish = perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
                self.facebook.driver.delete_all_cookies()
                #
                self.facebook.driver.execute_script("""window.open("https://www.facebook.com/","_blank")""")              
                self.facebook.driver.close()
                self.facebook.driver.switch_to_window(self.facebook.driver.window_handles[0])


        except (NoSuchWindowException, WebDriverException):
            self.run_error.emit(row['Id'], row['Full name'])
        
        else:
            self.settings.setValue('current_acc_ind', 1)
            self.facebook.driver.close()
            
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()

class PageFollowingUIWorker(QThread):
    """A thread responsible for putting following for page"""

    ### Signals to be emited if there any error occures
    # Sends the account name and his index 
    run_error = pyqtSignal(int, str)
    
    # Sends number of passed accounts that work
    passed_acc_counter = pyqtSignal(int)

    def __init__(self, driver_type, accounts_file_path, accounts_data, url,  parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.settings = QSettings('Viral Co.', 'Viral app')

    def run(self):
        try:
            counter = 0
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = perf_counter()

                new_mac_address = changeMac(self.facebook, row['Mac address'])
                
                self.facebook.sheet.cell(ind + 2, 13).value = new_mac_address if(new_mac_address != None) else ''

                self.facebook.login(email=row['Email'], password=row['Facebook password'])

                self.settings.setValue('current_acc_ind', ind+1)

                # Check if the account is active
                if(self.facebook.isAccountActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addPageFollowing(self.url)
                    self.facebook.logout()
                    counter +=1
                    self.passed_acc_counter.emit(counter)
                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")

                self.facebook.driver.delete_all_cookies()
            
                self.facebook.driver.execute_script("""window.open("https://www.facebook.com/","_blank")""")              
                self.facebook.driver.close()
                self.facebook.driver.switch_to_window(self.facebook.driver.window_handles[0])

            
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(row['Id'], row['Full name'])
        
        else:
            self.settings.setValue('current_acc_ind', 1)
            self.facebook.driver.close()

        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()

class CommentsOnPostWorker(QThread):
    """A thread responsible for putting comments on post"""
    
    ### Signals to be emited if there any error occures
    # Sends the account name and his index 
    run_error = pyqtSignal(int, str)
    
    # Sends number of passed accounts that work
    passed_acc_counter = pyqtSignal(int)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data, comments_data)
        self.url = url
        self.settings = QSettings('Viral Co.', 'Viral app')

    def run(self):
        try:
            counter = 0
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = perf_counter()

                new_mac_address = changeMac(self.facebook, row['Mac address'])
                
                self.facebook.sheet.cell(ind + 2, 13).value = new_mac_address if(new_mac_address != None) else ''

                self.facebook.login(email=row['Email'], password=row['Facebook password'])

                self.settings.setValue('current_acc_ind', ind+1)

                # Check if the account is active
                if(self.facebook.isAccountActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addCommentOnPost(self.url, emojize(self.facebook.comments_data.sample(1)['Comments'].values[0], use_aliases=True))
                    # self.facebook.addCommentOnPost(self.url, emojize(random.choice(self.facebook.comments_data), use_aliases=True))
                    self.facebook.logout()
                    counter +=1
                    self.passed_acc_counter.emit(counter)
                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
            
                self.facebook.driver.delete_all_cookies()
            
                self.facebook.driver.execute_script("""window.open("https://www.facebook.com/","_blank")""")              
                self.facebook.driver.close()
                self.facebook.driver.switch_to_window(self.facebook.driver.window_handles[0])


            
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(row['Id'], row['Full name'])
        
        else:
            self.settings.setValue('current_acc_ind', 1)
            self.facebook.driver.close()

        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()
            
class Likes_CommentsOnPostWorker(QThread):
    """A thread responsible for putting likes and comments on post"""
    
    
    ### Signals to be emited if there any error occures
    # Sends the account name and his index 
    run_error = pyqtSignal(int, str)
    
    # Sends number of passed accounts that work
    passed_acc_counter = pyqtSignal(int)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data, comments_data)
        self.url = url
        self.settings = QSettings('Viral Co.', 'Viral app')

    def run(self):
        try:
            counter = 0
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = perf_counter()

                new_mac_address = changeMac(self.facebook, row['Mac address'])
                
                self.facebook.sheet.cell(ind + 2, 13).value = new_mac_address if(new_mac_address != None) else ''

                self.facebook.login(email=row['Email'], password=row['Facebook password'])

                self.settings.setValue('current_acc_ind', ind+1)

                # Check if the account is active
                if(self.facebook.isAccountActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.addCommentOnPost(self.url, emojize(self.facebook.comments_data.sample(1)['Comments'].values[0], use_aliases=True))
                    # self.facebook.addCommentOnPost(self.url, emojize(random.choice(self.facebook.comments_data), use_aliases=True))
                    self.facebook.logout()
                    counter +=1
                    self.passed_acc_counter.emit(counter)

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
            
                self.facebook.driver.delete_all_cookies()
            
                self.facebook.driver.execute_script("""window.open("https://www.facebook.com/","_blank")""")              
                self.facebook.driver.close()
                self.facebook.driver.switch_to_window(self.facebook.driver.window_handles[0])

            
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(row['Id'], row['Full name'])
        
        else:
            self.settings.setValue('current_acc_ind', 1)
            self.facebook.driver.close()
            
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()
            
class AddMulitpleFriendsWorker(QThread):
    """Add many persons among each others at the same group"""

    run_error = pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, parent, method = 'all') :
        """method : as default 'enhance'
            we can use ('enhanced2', 'all')
            enhanced2 -> it uses combinations to select available accounts for adding for each individual account
            all -> can implement add person or response to received friendship request 
        """
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.method = method
        self.settings = QSettings('Viral Co.', 'Viral app')

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
                        
                        new_mac_address = changeMac(self.facebook, data.loc[key-1,'Mac address'])
                
                        self.facebook.sheet.cell(key + 1, 13).value = new_mac_address if(new_mac_address != None) else ''

                        self.facebook.login(email=data.loc[key-1,'Email'], password=data.loc[key-1,'Facebook password'])
                        
                        if(self.facebook.isAccountActive()):
                            self.facebook.sheet.cell(key + 1, 8).value = 'Active'
                            self.facebook.sheet.cell(key + 1, 6).value = self.facebook.getProfileLink()
                            
                            # Store all previouse accounts' ids and add new one to them
                            ids = [int(val) for val in indices_prev[key] if (not isnan(val))]
                            for val in indices_avaiable[key]:
                                self.facebook.addPerson(profile_path=data.loc[val - 1,'Profile path'])
                                self.facebook.acceptPerson(profile_path=data.loc[val - 1,'Profile path'])

                                ids.append(data.loc[val - 1, 'Id'])
                                
                                self.facebook.sheet.cell(key + 1, 12).value = ','.join(list(map(str, ids)))

                            self.facebook.logout()
                                                        
                        else:
                            self.facebook.sheet.cell(key + 2, 8).value = 'Inactive'
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
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()

class AcceptMulitpleFriendsWorker(QThread): 

    run_error = pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, comments_type, url, parent) :
       
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.comments_data = comments_data[comments_data['Type']==comments_type].loc[:, 'Comments'].values
        self.settings = QSettings('Viral Co.', 'Viral app')

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
                        self.facebook.sheet.cell(key + 2, 8).value = 'Active'
                        self.facebook.sheet.cell(key + 2, 6).value = self.facebook.getProfileLink()
                    
                        for val in indices[key]:
                            self.facebook._logger.info(f"add person {val}")
                            self.facebook.acceptPerson(profile_path=data.loc[val,'Profile path'])
                    
                        self.facebook._logger.info(f"""Logout from {key}""")
                        self.facebook.logout()

                    else:
                        self.facebook.sheet.cell(key + 2, 8).value = 'Inactive'
                        self.facebook.logout(active_acc=False)

        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(key + 1, self.facebook.accounts_data.loc[key, 'Full name'])
    
        else:
            self.facebook.driver.close()
            
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()
     
class Likes_CommentsOnFriendPostWorker(QThread):
    """A thread responsible for putting likes and comments on the friend post"""
    
    
    ### Signals to be emited if there any error occures
    # Sends the account name and his index 
    run_error = pyqtSignal(int, str)
    
    # Sends number of passed accounts that work
    passed_acc_counter = pyqtSignal(int)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data, comments_data)
        self.url = url
        self.settings = QSettings('Viral Co.', 'Viral app')

    def run(self):
        try:
            counter = 0
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = perf_counter()

                new_mac_address = changeMac(self.facebook, row['Mac address'])
                
                self.facebook.sheet.cell(ind + 2, 13).value = new_mac_address if(new_mac_address != None) else ''

                self.facebook.login(email=row['Email'], password=row['Facebook password'])

                self.settings.setValue('current_acc_ind', ind+1)

                # Check if the account is active
                if(self.facebook.isAccountActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.addCommentOnPost(self.url, emojize(self.facebook.comments_data.sample(1)['Comments'].values[0], use_aliases=True))
                    self.facebook.logout()
                    counter +=1
                    self.passed_acc_counter.emit(counter)
                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
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
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()
            


