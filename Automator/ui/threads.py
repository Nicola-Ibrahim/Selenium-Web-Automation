from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from PyQt5 import QtCore
from Automator.Facebook.facebook import Facebook

import random
import emoji

class LikesOnPostUIWorker(QtCore.QThread):
    
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


                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.logout()

                else:
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Inactive'
                    self.facebook.logout(active_acc=False)

                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
                self.settings.setValue('start_count', ind+1)
            
            self.settings.setValue('start_count', 1)
                 
        except (NoSuchWindowException,  WebDriverException) as e:
            self.run_error.emit(ind, row['Full name'])
        
        else:
            try:
                self.facebook.driver.close()
            except WebDriverException as e:
                pass

        finally:
            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            self.finished.emit()

class PageFollowingUIWorker(QtCore.QThread):

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

            self.facebook.worker_book.save(self.facebook.accounts_file_path)
            self.facebook.worker_book.close()
            
        except (NoSuchWindowException, WebDriverException) as e:
            return
        finally:
            try:
                self.facebook.driver.close()
            except WebDriverException as e:
                pass
            self.finished.emit()

class CommentsOnPostWorker(QtCore.QThread):
    

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, comments_type, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.comments_data = comments_data[comments_data['Type']==comments_type].loc[:, 'Comments'].values
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        try:
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = time.perf_counter()

                self.facebook.login(email=row['Email'], password=row['Facebook password'])


                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    # self.facebook.addCommentOnPost(self.url, emoji.emojize(random.choice(self.comments_data), use_aliases=True))
                    self.facebook.addCommentOnPost(self.url, emoji.emojize('رائع:heart_eyes::heart_eyes:', use_aliases=True))
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
            return
        finally:
            try:
                self.facebook.driver.close()
            except WebDriverException as e:
                pass
            self.finished.emit()
            
class Likes_CommentsOnPostWorker(QtCore.QThread):
    
   
    

    def __init__(self, driver_type, accounts_file_path, accounts_data, comments_data, comments_type, url, parent) :
        super().__init__(parent=parent)

        self.facebook = Facebook(driver_type, accounts_file_path, accounts_data)
        self.url = url
        self.comments_data = comments_data[comments_data['Type']==comments_type].loc[:, 'Comments'].values
        self.settings = QtCore.QSettings('BANG_team', 'WebAutomation')

    def run(self):
        try:
            for ind, row in self.facebook.accounts_data.iterrows():
                # start = time.perf_counter()

                self.facebook.login(email=row['Email'], password=row['Facebook password'])


                if(self.facebook.isProfileActive()):
                    self.facebook.sheet.cell(ind + 2, 8).value = 'Active'
                    self.facebook.sheet.cell(ind + 2, 6).value = self.facebook.getProfileLink()
                    self.facebook.addLikeOnPost(self.url)
                    self.facebook.addCommentOnPost(self.url, emoji.emojize(random.choice(self.comments_data), use_aliases=True))
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
            return
        finally:
            try:
                self.facebook.driver.close()
            except WebDriverException as e:
                pass
            self.finished.emit()
            

def addMulitplePersonsWorker(self, method = 'enhanced2'):
    """
    Add many persons from one account
    method : as default 'enhance'
            we can use ('simple', 'enhance', 'all')
            simple -> simplest algorithm that doesn't combrehend all conditions
            enhanced1 -> it is enhanced algorithm from simple algorithm
            enhanced2 -> it is enhanced algorithm from simple algorithm
            all -> can implement add person or response to received friendship request 
    """
    for group in self.accounts_data['group'].unique():
        data = self.accounts_data[self.accounts_data['group']==group].reset_index(drop=True)
        
        
        if(method == 'simple'):
            comb = list(combinations(data.index.values, r=2))
            k = 0    # saving current login account
            m = -1   # saving previous login account
            
            for i,j in comb:
                
                if(i > k):
                    self._logger.info(f"""Logout from {k}""")
                    self.logout()
                    k=i
                    
                elif(k > m):
                    self._logger.info(f"login to person {k}")
                    self.login(email=data.loc[k,'Email'], password=data.loc[k,'Facebook password'])
                    m = k
                
                    
                elif(i==k):
                    self._logger.info(f"add person {j}")
                    self.addPerson(profile_path=data.loc[j,'Profile path'])

        elif(method == 'enhanced1'):
            comb = list(combinations(data.index.values, r=2))
            keys = set(map(lambda item: item[0], comb))
            indices = {k:[y for x,y in comb if x==k] for k in keys}

            for key in indices.keys():
                self._logger.info(f"login to person {key}")
                self.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
                
                if(self.isProfileActive()):
                    self.sheet.cell(key + 2, 8).value = 'Active'
                    self.sheet.cell(key + 2, 6).value = self.getProfileLink()
                
                    for val in indices[key]:
                        self._logger.info(f"add person {val}")
                        self.addPerson(profile_path=data.loc[val,'Profile path'])
                
                    self._logger.info(f"""Logout from {key}""")
                    self.logout()

                else:
                    self.sheet.cell(key + 2, 8).value = 'Inactive'
                    self.logout(active_acc=False)

        elif(method == 'enhanced2'):
            comb = list(combinations(data.index.values, r=2))
            indices = {key: [val for _, val in values] for key, values in groupby(comb, itemgetter(0))}

            for key in indices.keys():
                self._logger.info(f"login to person {key}")
                self.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
                
                if(self.isProfileActive()):
                    self.sheet.cell(key + 2, 8).value = 'Active'
                    self.sheet.cell(key + 2, 6).value = self.getProfileLink()
                
                    for val in indices[key]:
                        self._logger.info(f"add person {val}")
                        self.addPerson(profile_path=data.loc[val,'Profile path'])
                
                    self._logger.info(f"""Logout from {key}""")
                    self.logout()

                else:
                    self.sheet.cell(key + 2, 8).value = 'Inactive'
                    self.logout(active_acc=False)

        elif(method == 'all'):
            perm = list(permutations(data.index.values, r=2))
            indices = {key: [val for _, val in values] for key, values in groupby(perm, itemgetter(0))}

            for key in indices.keys():
                self._logger.info(f"login to person {key}")
                self.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
                
                if(self.isProfileActive()):
                    self.sheet.cell(key + 2, 8).value = 'Active'
                    self.sheet.cell(key + 2, 6).value = self.getProfileLink()
                
                    for val in indices[key]:
                        self._logger.info(f"add person {val}")
                        self.addPerson(profile_path=data.loc[val,'Profile path'])
                        self.acceptPerson(profile_path=data.loc[val,'Profile path'])
                
                    self._logger.info(f"""Logout from {key}""")
                    self.logout()

                else:
                    self.sheet.cell(key + 2, 8).value = 'Inactive'
                    self.logout(active_acc=False)

    self.worker_book.save(self.accounts_file_path)
    self.worker_book.close()    

def acceptMulitplePersonsWorker(self): 
    for group in self.accounts_data['group'].unique():
        data = self.accounts_data[self.accounts_data['group']==group].reset_index(drop=True)
        comb = list(combinations(data.index.values[::-1], r=2))

        indices = {key: [val for _, val in values] for key, values in groupby(comb, itemgetter(0))}

        for key in indices.keys():
            self._logger.info(f"login to person {key}")
            self.login(email=data.loc[key,'Email'], password=data.loc[key,'Facebook password'])
            
            if(self.isProfileActive()):
                self.sheet.cell(key + 2, 8).value = 'Active'
                self.sheet.cell(key + 2, 6).value = self.getProfileLink()
            
                for val in indices[key]:
                    self._logger.info(f"add person {val}")
                    self.acceptPerson(profile_path=data.loc[val,'Profile path'])
            
                self._logger.info(f"""Logout from {key}""")
                self.logout()

            else:
                self.sheet.cell(key + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)

        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()  
