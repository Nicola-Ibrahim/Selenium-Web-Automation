from itertools import combinations, groupby, permutations
from operator import itemgetter
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from Automator.Facebook.facebook import Facebook
from PyQt5 import QtCore
import emoji

class LikesOnPostUIWorker(QtCore.QThread):
    """A thread responsible for putting likes of post"""

    
    # Signal to be emited if there any error
    # it sends the account name and his index
    run_error = QtCore.pyqtSignal(int, str)
    passed_acc_counter = QtCore.pyqtSignal(int)

    def __init__(self, driver_type, accounts_file_path, accounts_data, url,  parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        try:
            counter = 0
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = time.perf_counter()

                self.facebook.login(email=row['Email'], password=row['Facebook password'])


                # Check if the account is active
                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.logout()
                    counter +=1
                    self.passed_acc_counter.emit(counter)

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)


                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
                self.settings.setValue('start_count', ind+1)
            
            self.settings.setValue('start_count', 1)
                 
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(ind + 1, row['Full name'])
        
        else:
            self.facebook.driver.close()
            
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()

class PageFollowingUIWorker(QtCore.QThread):
    """A thread responsible for putting following for page"""

    # Signal to be emited if there any error
    # it sends the account name and his index
    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, url,  parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        try:
            
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = time.perf_counter()

                self.facebook.login(email=row['Email'], password=row['Facebook password'])


                # Check if the account is active
                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addPageFollowing(self.url)
                    self.facebook.logout()

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")

                self.settings.setValue('start_count', ind+1)
            
            self.settings.setValue('start_count', 1)

            
            
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(ind + 1, row['Full name'])
        
        else:
            self.facebook.driver.close()
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()

class CommentsOnPostWorker(QtCore.QThread):
    """A thread responsible for putting comments on post"""
    
    # Signal to be emited if there any error
    # it sends the account name and his index
    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data, comments_data)
        self.url = url
        # self.comments_data = 
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        try:
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = time.perf_counter()

                self.facebook.login(email=row['Email'], password=row['Facebook password'])


                # Check if the account is active
                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addCommentOnPost(self.url, emoji.emojize(self.facebook.comments_data.sample(1)['Comments'].values[0], use_aliases=True))
                    # self.facebook.addCommentOnPost(self.url, emoji.emojize('رائع:heart_eyes::heart_eyes:', use_aliases=True))
                    self.facebook.logout()

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
                self.settings.setValue('start_count', ind+1)
            
            self.settings.setValue('start_count', 1)

            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(ind + 1, row['Full name'])
        
        else:
            self.facebook.driver.close()
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()
            
class Likes_CommentsOnPostWorker(QtCore.QThread):
    """A thread responsible for putting likes and comments on post"""
    
    run_error = QtCore.pyqtSignal(int, str)
    
    # Signal to be emited if there any error
    # it sends the account name and his index
    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data, comments_data)
        self.url = url
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        try:
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = time.perf_counter()

                self.facebook.login(email=row['Email'], password=row['Facebook password'])


                # Check if the account is active
                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.addCommentOnPost(self.url, emoji.emojize(self.facebook.comments_data.sample(1)['Comments'].values[0], use_aliases=True))
                    self.facebook.logout()

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
                self.settings.setValue('start_count', ind+1)
            
            self.settings.setValue('start_count', 1)

            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(ind + 1, row['Full name'])
        
        else:
            self.facebook.driver.close()
            
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()
            
class AddMulitpleFriendsWorker(QtCore.QThread):
    """Add many persons among each others at the same group"""

    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, method, parent) :
        """method : as default 'enhance'
            we can use ('enhanced2', 'all')
            enhanced2 -> it uses combinations to select available accounts for adding for each individual account
            all -> can implement add person or response to received friendship request 
        """
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.method = method
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        
        try:
            for group in self.facebook.accounts_data['group'].unique():
                data = self.facebook.accounts_data[self.accounts_data['group']==group].reset_index(drop=True)

                if(self.method == 'enhanced2'):
                    comb = list(combinations(data.index.values, r=2))
                    indices = {key: [val for _, val in values] for key, values in groupby(comb, itemgetter(0))}

                    for key in indices.keys():
                        self.facebook.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
                        
                        if(self.facebook.isProfileActive()):
                            self.facebook.sheet.cell(key + 2, 8).value = 'Active'
                            self.facebook.sheet.cell(key + 2, 6).value = self.facebook.getProfileLink()
                        
                            for val in indices[key]:
                                self.facebook.addPerson(profile_path=data.loc[val,'Profile path'])
                        
                            self.facebook.logout()

                        else:
                            self.facebook.sheet.cell(key + 2, 8).value = 'Inactive'
                            self.facebook.logout(active_acc=False)

                elif(self.method == 'all'):
                    perm = list(permutations(data.index.values, r=2))
                    indices = {key: [val for _, val in values] for key, values in groupby(perm, itemgetter(0))}

                    for key in indices.keys():
                        self.facebook.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
                        
                        if(self.facebook.isProfileActive()):
                            self.facebook.sheet.cell(key + 2, data.columns.get_loc('Account status')+1).value = 'Active'
                            self.facebook.sheet.cell(key + 2, 6).value = self.facebook.getProfileLink()
                        
                            for val in indices[key]:
                                self.facebook.addPerson(profile_path=data.loc[val,'Profile path'])
                                self.facebook.acceptPerson(profile_path=data.loc[val,'Profile path'])
                        
                            self.facebook.logout()

                        else:
                            self.facebook.sheet.cell(key + 2, data.columns.get_loc('Account status')+1).value = 'Inactive'
                            self.facebook.logout(active_acc=False)

        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(key + 1, data.loc[key, 'Full name'])
        
        else:
            self.facebook.driver.close()
            
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()

class AcceptMulitpleFriendsWorker(QtCore.QThread): 

    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, comments_type, url, parent) :
       
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.comments_data = comments_data[comments_data['Type']==comments_type].loc[:, 'Comments'].values
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
    
        try:
            for group in self.facebook.accounts_data['group'].unique():
                data = self.facebook.accounts_data[self.facebook.accounts_data['group']==group].reset_index(drop=True)
                comb = list(combinations(data.index.values[::-1], r=2))

                indices = {key: [val for _, val in values] for key, values in groupby(comb, itemgetter(0))}

                for key in indices.keys():
                    self.facebook._logger.info(f"login to person {key}")
                    self.facebook.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
                    
                    if(self.facebook.isProfileActive()):
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
     
class Likes_CommentsOnFriendPostWorker(QtCore.QThread):
    """A thread responsible for putting likes and comments on the friend post"""
    
    
    # Signal to be emited if there any error
    # it sends the account name and his index
    run_error = QtCore.pyqtSignal(int, str)

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data, comments_data)
        self.url = url
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        try:
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = time.perf_counter()

                self.facebook.login(email=row['Email'], password=row['Facebook password'])


                # Check if the account is active
                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.addCommentOnPost(self.url, emoji.emojize(self.facebook.comments_data.sample(1)['Comments'].values[0], use_aliases=True))
                    self.facebook.logout()

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
                self.settings.setValue('start_count', ind+1)
            
            self.settings.setValue('start_count', 1)

            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            
        except (NoSuchWindowException, WebDriverException) as e:
            self.run_error.emit(ind + 1, row['Full name'])
        
        else:
            self.facebook.driver.close()
            
        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()
            


