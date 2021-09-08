"""
This file is reponsible for autmating many facebook website.
A file should be used to store facebook accounts (email, password) and use them to login.
"""

from pandas.core.frame import DataFrame
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from Automator.WebAutomation import WbAutomator

import re
import logging
import time
import openpyxl
import random
from datetime import datetime
from itertools import combinations, groupby, permutations
from operator import itemgetter
import emoji

class Facebook(WbAutomator):
    """Chiled class automator"""

    class Inner():
        def __init__(self,func):
            self.func = func

            # # Edit accounts file
            # self.accounts_file_path = accounts_file_path
            # self.worker_book = openpyxl.load_workbook(self.accounts_file_path)
            # self.sheet =  self.worker_book.active
        
        def __call__(self, *args, **kwargs):
            face = Facebook(args[0])
            for ind, row in args[1].iterrows():
            
                face.login(email=row['Email'], password=row['Facebook password'])

                if(face.isAccountActive()):
                    self.func(*args, **kwargs)
                    face.logout()

                else:
                    face.logout2()

            # self.worker_book.save(self.accounts_file_path)
            # self.worker_book.close()


    def __init__(self, driver_type : str, accounts_file_path : str, accounts_data : DataFrame, comments_data : DataFrame = None) :
        super().__init__(driver_type=driver_type, website="https://www.facebook.com/", logfile_path="./logs/Facebook accounts logout info.log")

        self._NEW_ACCOUNT_BUTTON_XPTH = "//a[@role='button' and @class= '_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']"

        self._LOGIN_EMAIL_TEXTBOX_XPATH = "//input[@name = 'email']"
        self._LOGIN_PASSOWRD_TEXTBOX_XPATH = "//input[@name = 'pass']"
        self._LOGIN_BUTTON_XPATH = "//button[@name='login']"

        self._SIGNUP_FIRST_NAME_TEXTBOX_XPATH = "//input[@name = 'firstname']"
        self._SIGNUP_LAST_NAME_TEXTBOX_XPATH = "//input[@name = 'lastname']"
        self._SIGNUP_EMAIL_TEXTBOX_XPATH = "//input[@name = 'reg_email__']"
        self._SIGNUP_EMAIL_CONFIRMATION_TEXTBOX_XPATH = "//input[@name = 'reg_email_confirmation__']"
        self._SIGNUP_PASSWORD_TEXTBOX_XPATH = "//input[@name = 'reg_passwd__']"
        self._SIGNUP_BDAY_TEXTBOX_XPATH = "//select[@name = 'birthday_day']"
        self._SIGNUP_BMONTH_TEXTBOX_XPATH = "//select[@name = 'birthday_month']"
        self._SIGNUP_BYEAR_TEXTBOX_XPATH = "//select[@name = 'birthday_year']"
        self._SIGNUP_GENDER_COMBOBOX_XPATH = "//input[@value = '{}']"
        self._SIGNUP_BUTTON_XPATH = "//button[@type = 'submit' and @name = 'websubmit']"

        self._MENU_BUTTON_XPATH = "//div[@aria-label='Account' or @aria-label='More options' or @aria-label='الحساب' or @aria-label='خيارات إضافية']"
        self._LOUTGOUT_BUTTON1_XPATH = "//span[contains(text(),'Log Out') or contains(text(),'تسجيل الخروج')]"                      
        self._LOUTGOUT_BUTTON2_XPATH = "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div/span/span[contains(text(),'Log Out') or contains(text(),'تسجيل الخروج')]"
        
        self._MESSAGE_BUTTON_XPATH = "//div[@aria-label='Message' or @aria-label='مراسلة']"
        self._MESSAGE_TEXTBOX_XPATH = "//div[@aria-label='Aa']"

        # self._COMMENT_TEXTBOX_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div"
        self._COMMENT_TEXTBOX_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/form/div/div/div[1]"
        # self._COMMENT_TEXTBOX_XPATH = "//div[@aria-label='Write a comment' or @aria-label='كتابة تعليق'][@role='textbox']"


        self._LIKE_BUTTON_XPATH1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/span"
        self._LIKE_BUTTON_XPATH2 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/span/span"
        # self._LIKE_BUTTON_XPATH = "//div[@aria-label='Like' or @aria-label='أعجبني'][@role='button']"
                                    
        # self._PAGE_FOLLOW_BUTTON_XPATH = "//span[contains(text(),'Like') or contains(text(),'أعجبني')]"
        self._PAGE_FOLLOW_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div/span/div"
        self._PAGE_LIKE_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[1]"
                                            
                                            
        
        self._ADD_PERSON_BUTTON_XPATH = "//span[contains(text(),'Add Friend') or contains(text(),'إضافة صديق')]"
        self._ACCEPT_PERSON_BUTTON_XPATH1 = "//span[contains(text(),'Respond') or contains(text(),'تأكيد الطلب')]"
        self._ACCEPT_PERSON_BUTTON_XPATH2 = "//span[contains(text(),'Confirm') or contains(text(),'تأكيد')]"

        self._VIEW_ALL_COMMETNS_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span/span[matches(text(), 'View \w* more comments']"

        self._NUM_OF_FRIENDS1_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]/div[1]/span/span[2]"
        self._NUM_OF_FRIENDS2_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a"  
        
        self._PROFILE_LINK_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a"

        self._LOCKED_PROFILE_TEXT_XPATH = "/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/span"


        self.accounts_file_path = accounts_file_path
        self.accounts_data = accounts_data
        self.comments_data = comments_data

        # Edit accounts file
        self.worker_book = openpyxl.load_workbook(self.accounts_file_path)
        self.sheet =  self.worker_book.active

    def signUp(self, first_name:str, last_name:str, email:str, password:str, date_of_birth, gender):
        """Sign up for new facebook account"""
        try:
            create_new_account_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._NEW_ACCOUNT_BUTTON_XPTH)))
            create_new_account_button.click()

            first_name_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_FIRST_NAME_TEXTBOX_XPATH)))
            last_name_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_LAST_NAME_TEXTBOX_XPATH)))
            email_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_EMAIL_TEXTBOX_XPATH)))
            email_confirmation_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_EMAIL_CONFIRMATION_TEXTBOX_XPATH)))
            password_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_PASSWORD_TEXTBOX_XPATH)))
            
            date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            birth_day_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_BDAY_TEXTBOX_XPATH)))
            Select(birth_day_list).select_by_index(date.day)

            birth_month_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_BMONTH_TEXTBOX_XPATH)))
            Select(birth_month_list).select_by_index(date.month)
            
            birth_year_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_BYEAR_TEXTBOX_XPATH)))
            Select(birth_year_list).select_by_visible_text(str(date.year))

            dic = {'Female':'1', 'Male':'2'}
            gender_comboBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_GENDER_COMBOBOX_XPATH.format(dic[gender.capitalize()]))))

            sign_up_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_BUTTON_XPATH)))

            first_name_textBox.send_keys(first_name)
            last_name_textBox.send_keys(last_name)
            email_textBox.send_keys(email)
            email_confirmation_textBox.send_keys(email)
            password_textBox.send_keys(password)
            gender_comboBox.click()
            sign_up_button.click()
            
            time.sleep(40)
        except TimeoutException as e:
            pass

    def login(self, email, password):
        super().login(email, password, self._LOGIN_EMAIL_TEXTBOX_XPATH, self._LOGIN_PASSOWRD_TEXTBOX_XPATH, self._LOGIN_BUTTON_XPATH)
            
    def logout(self, active_acc = True):
        if(active_acc):
            return super().logout(self._MENU_BUTTON_XPATH, self._LOUTGOUT_BUTTON1_XPATH)
        else:
            return super().logout(self._MENU_BUTTON_XPATH, self._LOUTGOUT_BUTTON1_XPATH, self._LOUTGOUT_BUTTON2_XPATH)
        
    
    def chat(self, message:str, profile_path:str):
        return super().chat( message, profile_path, self._MESSAGE_BUTTON_XPATH, self._MESSAGE_TEXTBOX_XPATH)
        
    def addCommentOnPost(self, post_path, comment):
        return super().addCommentOnPost(post_path, comment, self._COMMENT_TEXTBOX_XPATH)

  
    def addLikeOnComment(self, post_path:str):
        return super().addLikeOnComment(post_path, self._VIEW_ALL_COMMETNS_XPATH)

    
    def addLikeOnPost(self, post_path:str):
        return super().addLikeOnPost(post_path, self._LIKE_BUTTON_XPATH1, self._LIKE_BUTTON_XPATH2)        
        

    def addPageFollowing(self, page_path:str):
        return super().addPageFollowing(page_path, self._PAGE_LIKE_BUTTON_XPATH, self._PAGE_FOLLOW_BUTTON_XPATH)        

    def addPerson(self, profile_path:str):
        return super().addPerson(profile_path, self._ADD_PERSON_BUTTON_XPATH)
    
    def acceptPerson(self, profile_path:str):
        return super().acceptPerson(profile_path, self._ACCEPT_PERSON_BUTTON_XPATH1, self._ACCEPT_PERSON_BUTTON_XPATH2)


    def countNFreinds(self, profile_path:str):
        """Calculate the number of friends for specific profile"""
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))  
        self.driver.get(profile_path)
        
        try:
            num_of_friends = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self._NUM_OF_FRIENDS1_XPATH)))
        
        except TimeoutException: 
            try:
                num_of_friends2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self._NUM_OF_FRIENDS2_XPATH)))
            
            except TimeoutException: 
                pass 
            else: 
                return re.findall(pattern=r'\d+', string=num_of_friends2.text)[0]
            
        else: 
            return num_of_friends.text

        
            
        return 0 

    def getProfileLink(self):
        """Obtain profile link(path) after login into it"""
        try:
            profile_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self._PROFILE_LINK_XPATH)))
            return profile_link.get_attribute('href')
        except TimeoutException:
            pass
        
    def isAccountActive(self):
        """Check if the specific profile is disable"""
        try:
            
            label = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self._LOCKED_PROFILE_TEXT_XPATH)))
            if(label.text in ("تم تعطيل حسابك", "Your account has been disabled")):
                return False

        except TimeoutException:
            return True

    
    ############################################################
    ### Some workers to be using throught threads techniques ###
    ############################################################
    def addPageFollowingWorker(self, page_path):
        
        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()
            
            self.login(email=row['Email'], password=row['Facebook password'])

            if(self.isAccountActive()):
                self.sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 6).value = self.getProfileLink()
                self.addPageFollowing(page_path=page_path)
                self.logout()

            else:
                self.sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)

        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()
            
            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")

    def addLikeOnCommentWorker(self, post_path):
        

        worker_book = openpyxl.load_workbook(self.accounts_file_path)
        sheet =  worker_book.active

        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])

            if(self.isAccountActive()):
                sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 6).value = self.getProfileLink()
                self.addLikeOnComment(post_path=post_path)
                self.logout()

            else:
                sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)
                
        
            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
     
        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()
    
    def addCommentOnPostWorker(self, post_path):
        
        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])


            if(self.isAccountActive()):
                self.sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 6).value = self.getProfileLink()
                self.addCommentOnPost(post_path=post_path, comment='...')
                self.logout()

            else:
                self.sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)

            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")

        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()
    
    def addLikeOnPostWorker(self, post_path):
        
        
        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])


            if(self.isAccountActive()):
                self.sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 6).value = self.getProfileLink()
                self.addLikeOnPost(post_path=post_path)
                self.logout()

            else:
                self.sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)

            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")

        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()

    def addLike_CommentOnPostWorker(self,post_path):
        
        # comments = ['.','..','....','السعر','سعر','السعر لو سمحت','عنوان','مقاسات']
        # weights = [0.3, 0.5, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1]
       
        commments = [
            'واااوheart:',
            ':heart::heart::heart:',
            ':heart::heart:',
            ':heart::heart:',
            ':heart::heart::heart:',
            'واااو :heart::heart:',
            'يسلم ايديك',
            'شغل روعة',
            'فخامة',
            'ممتاااااز',
            'برافوو' ,
            'عظيم',
            'الله يقويك :heart::heart:',
            'شغل ممتاز ولله',
            'من نجاح لنجاح دكتورنا',
            'ماشالله :heart::heart:',
            'اي هك شغل يابلا :heart::heart::heart::heart:',
            'بالتوفيق يارب',
            'احلى دكتور',
            'موفق دكتورنا',
            'مبدع',
            'دكتورنا:heart::heart::heart::heart:',
            'يسلم هالايدين',
            'موقق عطول :heart::heart:',
            'شغل روعة :heart::heart:',
            'ممتاز',
            'شي فخم',
            'نتائج رائعة',
            'بالتوفيييق دكتورنا الغالي',
            'بالتوفيق دكتورنا',
            'بالتوفييق دكتورنا',
            ':heart::heart::heart:',
            ':heart:',
            'دكتورنا الراقي',
            'مافي منك دكتور',
            'دكتورنا المذوق :heart:',
            'شغلك بيحكي عنك:heart:',
            'ماشالله ع هالشغل الحلو',
            'شغلك ممتاز ع طول :heart::heart:',
            'متألق:heart::heart:',
            ':heart::heart::heart:',
            'برافو عنجد:heart::heart:',
            'ممتاز',
        ]
        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])

            if(self.isAccountActive()):
                self.sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 6).value = self.getProfileLink()
                self.addLikeOnPost(post_path)
                # self.addCommentOnPost(post_path, random.choices(comments, weights, k=1)[0])
                self.addCommentOnPost(post_path, emoji.emojize(random.choice(commments), use_aliases=True))
                
                self.logout()
            else:
                self.sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)


            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
        
        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()

    def countNFreindsWorker(self):
        
        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])

            if(self.isAccountActive()):
                self.sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 7).value = self.countNFreinds(profile_path=row['Profile path'])
                self.logout()

            else:
                self.sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)


            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
        
        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()

    def getProfileLinkWorker(self):

        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])

            if(self.isAccountActive()):
                self.sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 6).value = self.getProfileLink()

                self.logout()
            else:
                self.sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)

            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['Full name']}" in {round(finish-start,2)} second(s)""")

        self.worker_book.save(self.accounts_file_path)
        self.worker_book.close()

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
                    
                    if(self.isAccountActive()):
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
                    
                    if(self.isAccountActive()):
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
                    
                    if(self.isAccountActive()):
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

    def addOnePersonWorker(self, profile_path):
        
        worker_book = openpyxl.load_workbook(self.accounts_file_path)
        sheet =  worker_book.active

        for ind, row in self.accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])

            if(self.isAccountActive()):
                sheet.cell(ind + 2, 8).value = 'Active'
                self.sheet.cell(ind + 2, 6).value = self.getProfileLink()
                self.addPerson(profile_path=profile_path)
                self.logout()

            else:
                sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout(active_acc=False)
        
            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
        
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
                
                if(self.isAccountActive()):
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