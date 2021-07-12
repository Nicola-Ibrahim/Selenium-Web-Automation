"""
This file is reponsible for autmating many facebook website.
A file should be used to store facebook accounts (email, password) and use them to login.
"""
from datetime import datetime
import numpy as np
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ..WebAutomation import WbAutomator

import re
import logging
import time
import openpyxl
import random

class Facebook(WbAutomator):
    """Chile class automator"""
    def __init__(self, website) :
        super().__init__(website=website)

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

        self._COMMENT_TEXTBOX_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div"
        self._LIKE_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]"

        self._PAGE_FOLLOW_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/span/span[contains(text(),'Like') or contains(text(),'أعجبني')]"
        self._ADD_PERSON_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/span/span[contains(text(),'Add Friend') or contains(text(),'إضافة صديق')]"

        self._VIEW_ALL_COMMETNS_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span/span[matches(text(), 'View \w* more comments']"

        self._NUM_OF_FRIENDS1_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]/div[1]/span/span[2]"
        self._NUM_OF_FRIENDS2_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a"  
        
        self._PROFILE_LINK_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a"

        self._LOCKED_PROFILE_TEXT_XPATH = "/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/span"

        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler("./logs/Facebook accounts logout info.log", mode='w')
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(message)s"))
        
        self._logger.addHandler(handler)

    def signUp(self, first_name, last_name, email, password, date_of_birth, gender):
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
            
    def logout(self):
        return super().logout(self._MENU_BUTTON_XPATH, self._LOUTGOUT_BUTTON1_XPATH)
    
    def logout2(self, menu_xpath, logout_button1_xpath, logout_button2_xpath):
        """Logout from account"""
        # Search for the menu button and logout button    
        try: 
            menu_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, menu_xpath)))
            menu_button.click() 

            logout_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, logout_button1_xpath)))
            logout_button.click()

            logout_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, logout_button2_xpath)))
            logout_button.click()

            self.driver.get(self.website)

        except (TimeoutException) as e:
            pass
    
    def chat(self, message, profile_path):
        return super().chat( message, profile_path, self._MESSAGE_BUTTON_XPATH, self._MESSAGE_TEXTBOX_XPATH)
        
    def addCommentOnPost(self, post_path, comment):
        return super().addCommentOnPost(post_path, comment, self._COMMENT_TEXTBOX_XPATH)

    def addCommentOnPost2(self, comment):
        """Add comment on a post"""
        try:
            
            post_comment_box = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self._COMMENT_TEXTBOX_XPATH)))
            post_comment_box.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
            post_comment_box.send_keys(comment)

            post_comment_box.send_keys(Keys.ENTER)

            

        except TimeoutException as e:
            pass 

    def addLikeOnComment(self, post_path):
        return super().addLikeOnComment(post_path, self._VIEW_ALL_COMMETNS_XPATH)

    def addLikeOnPost(self, post_path):
        return super().addLikeOnPost(post_path, self._LIKE_BUTTON_XPATH)        

    def addPageFollowing(self, page_path):
        return super().addPageFollowing(page_path, self._PAGE_FOLLOW_BUTTON_XPATH)        

    def addPerson(self, profile_path):
        return super().addPerson(profile_path, self._ADD_PERSON_BUTTON_XPATH)


    def countNFreinds(self, profile_path):
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
        
    def isProfileActive(self):
        """Check if the specific profile is disable"""
        try:
            
            label = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self._LOCKED_PROFILE_TEXT_XPATH)))
            if(label.text in ("تم تعطيل حسابك", "Your account has been disabled")):
                return False

        except TimeoutException:
            return True


    ############################################################
    ### Some workers to be using throught threads techniques ###
    ############################################################
    def addPageFollowingWorker(self, accounts_data, page_path):
        
        for _, row in accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['email'], password=row['password2'])
            self.addPageFollowing(page_path=page_path)
            self.logout()
            
            
            
            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")

    def addPersonWorker(self, accounts_data, profile_path):
        
        for _, row in accounts_data.iterrows():
            start = time.perf_counter()

            self.login(email=row['email'], password=row['password2'])
            self.addPerson(profile_path=profile_path)
            self.logout()
            finish = time.perf_counter()
            self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")

    def addLikeOnCommentWorker(self, accounts_data, post_path):
        
        for _, row in accounts_data.iterrows():
            start = time.perf_counter()

            self.login(email=row['email'], password=row['password2'])
            # self.addLikeOnComment(post_path=post_path)
            # self.logout()
            finish = time.perf_counter()
            self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
    
    def addCommentOnPostWorker(self, accounts_data, post_path):
        
        for _, row in accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])
            self.addCommentOnPost(post_path=post_path, comment='...')
            self.logout()
            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
    
    def addLikeOnPostWorker(self, accounts_file, accounts_data, post_path):
        
        worker_book = openpyxl.load_workbook(accounts_file)
        sheet =  worker_book.active

        for ind, row in accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])

            ret = self.isProfileActive()
            if(ret == False):
                sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout2(self._MENU_BUTTON_XPATH, self._LOUTGOUT_BUTTON1_XPATH, self._LOUTGOUT_BUTTON2_XPATH)

            elif(ret == True):
                sheet.cell(ind + 2, 8).value = 'Active'
                self.addLikeOnPost(post_path=post_path)
                self.logout()

            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
    
    def addLike_CommentOnPostWorker(self, accounts_file, accounts_data, post_path):
        
        worker_book = openpyxl.load_workbook(accounts_file)
        sheet =  worker_book.active

        comments = ['..','....','السعر',' سعر','السعر لو سمحت','عنوان','مقاسات']
        for ind, row in accounts_data.iterrows():
            # start = time.perf_counter()

            self.login(email=row['Email'], password=row['Facebook password'])

            ret = self.isProfileActive()
            if(ret == False):
                sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout2(self._MENU_BUTTON_XPATH, self._LOUTGOUT_BUTTON1_XPATH, self._LOUTGOUT_BUTTON2_XPATH)

            elif(ret == True):
                sheet.cell(ind + 2, 8).value = 'Active'
                self.addLikeOnPost(post_path=post_path)
                self.addCommentOnPost2("السعر")
                self.logout()

            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
    

    def countNFreindsWorker(self,accounts_file, accounts_data):
        
        worker_book = openpyxl.load_workbook(accounts_file)
        sheet =  worker_book.active

        for ind, row in accounts_data.iterrows():
            if(row['Account status']=='Active'):
                # start = time.perf_counter()
                self.login(email=row['Email'], password=row['Facebook password'])
                sheet.cell(ind + 2, 7).value = self.countNFreinds(profile_path=row['Profile path'])

                self.logout()

                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['Full name']}" in {round(finish-start,2)} second(s)""")

        worker_book.save(accounts_file)
        worker_book.close()

    def getProfileLinkWorker(self, accounts_file, accounts_data):

        worker_book = openpyxl.load_workbook(accounts_file)
        sheet =  worker_book.active

        for ind, row in accounts_data.iterrows():
            if(row['Profile path'] in (np.nan, 'nan') and row['Account status']=='Active'):
                # start = time.perf_counter()
                self.login(email=row['Email'], password=row['Facebook password'])
                sheet.cell(ind + 2, 6).value = self.getProfileLink()
                self.logout()

                # finish = time.perf_counter()
                # self._logger.info(f"""Logout from "{row['Full name']}" in {round(finish-start,2)} second(s)""")

        worker_book.save(accounts_file)
        worker_book.close()

    def checkAccountsWorker(self, accounts_file, accounts_data):

        worker_book = openpyxl.load_workbook(accounts_file)
        sheet =  worker_book.active

        for ind, row in accounts_data.iterrows():
            # start = time.perf_counter()
            self.login(email=row['Email'], password=row['Facebook password'])

            ret = self.isProfileActive()
            if(ret == False):
                sheet.cell(ind + 2, 8).value = 'Inactive'
                self.logout2(self._MENU_BUTTON_XPATH, self._LOUTGOUT_BUTTON1_XPATH, self._LOUTGOUT_BUTTON2_XPATH)

            elif(ret == True):
                sheet.cell(ind + 2, 8).value = 'Active'
                self.logout()

            # finish = time.perf_counter()
            # self._logger.info(f"""Logout from "{row['Full name']}" in {round(finish-start,2)} second(s)""")

        worker_book.save(accounts_file)
        worker_book.close()
   

