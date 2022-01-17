"""
This file is reponsible for autmating many facebook website.
A file should be used to store facebook accounts (email, password) and use them to login.
"""

import logging
from PyQt5 import QtCore

from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from Automation.core.website_automator import WebSiteAutomator
from selenium.webdriver.remote.webdriver import WebDriver

import re
import time
from datetime import datetime


class FacbookAutomator(WebSiteAutomator):
    """Parent class automator"""

    def __init__(self, driver: WebDriver) -> None:
 
        # create new logger for testing 
        # self._logger = self.init_logger()
        super().__init__(driver, "https://www.facebook.com/") 
    
    def init_logger(self) -> logging.Logger:
        """Intial new logger
        path: logger file path
        """
        
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(filename="Facebook.log", mode='w')
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(message)s"))
        logger.addHandler(handler)

        return logger

    def go_to(self, path) -> None:
        """Go to specific path"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
        if(self.driver.current_url != path):
            self.driver.get(path)

    def sign_up(self, first_name:str, last_name:str, email:str, password:str, date_of_birth, gender):
        """Sign up for new facebook account"""

        NEW_ACCOUNT_BUTTON_XPATH = "//a[@role='button' and @class= '_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']"

        SIGNUP_FIRST_NAME_TEXTBOX_XPATH = "//input[@name = 'firstname']"
        SIGNUP_LAST_NAME_TEXTBOX_XPATH = "//input[@name = 'lastname']"
        SIGNUP_EMAIL_TEXTBOX_XPATH = "//input[@name = 'reg_email__']"
        SIGNUP_EMAIL_CONFIRMATION_TEXTBOX_XPATH = "//input[@name = 'reg_email_confirmation__']"
        SIGNUP_PASSWORD_TEXTBOX_XPATH = "//input[@name = 'reg_passwd__']"
        SIGNUP_BDAY_TEXTBOX_XPATH = "//select[@name = 'birthday_day']"
        SIGNUP_BMONTH_TEXTBOX_XPATH = "//select[@name = 'birthday_month']"
        SIGNUP_BYEAR_TEXTBOX_XPATH = "//select[@name = 'birthday_year']"
        SIGNUP_GENDER_COMBOBOX_XPATH = "//input[@value = '{}']"
        SIGNUP_BUTTON_XPATH = "//button[@type = 'submit' and @name = 'websubmit']"

        try:
            create_new_account_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, NEW_ACCOUNT_BUTTON_XPATH)))
            create_new_account_button.click()

            first_name_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_FIRST_NAME_TEXTBOX_XPATH)))
            last_name_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_LAST_NAME_TEXTBOX_XPATH)))
            email_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_EMAIL_TEXTBOX_XPATH)))
            email_confirmation_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_EMAIL_CONFIRMATION_TEXTBOX_XPATH)))
            password_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_PASSWORD_TEXTBOX_XPATH)))
            
            date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            birth_day_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_BDAY_TEXTBOX_XPATH)))
            Select(birth_day_list).select_by_index(date.day)

            birth_month_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_BMONTH_TEXTBOX_XPATH)))
            Select(birth_month_list).select_by_index(date.month)
            
            birth_year_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_BYEAR_TEXTBOX_XPATH)))
            Select(birth_year_list).select_by_visible_text(str(date.year))

            dic = {'Female':'1', 'Male':'2'}
            gender_comboBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_GENDER_COMBOBOX_XPATH.format(dic[gender.capitalize()]))))

            sign_up_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SIGNUP_BUTTON_XPATH)))

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
    
    def login(self, email:str, password:str):
        """Login into an account"""

        LOGIN_EMAIL_TEXTBOX_XPATH = "//input[@name = 'email']"
        LOGIN_PASSOWRD_TEXTBOX_XPATH = "//input[@name = 'pass']"
        LOGIN_BUTTON_XPATH = "//button[@name='login']"

        connected_state = self.is_connnected()
        
        self.driver.get(self.website_url)
        
        reachable_state = self.is_reachable()

        # Search for email textBox, password textBox, and login button
        try:
            email_textBox = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, LOGIN_EMAIL_TEXTBOX_XPATH)))
            password_textBox = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, LOGIN_PASSOWRD_TEXTBOX_XPATH)))
            login_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, LOGIN_BUTTON_XPATH)))

            email_textBox.send_keys(email)
            password_textBox.send_keys(password)
            login_button.click()
            

        except TimeoutException as e:
            self.logger_wrt_error(f"Can't find login web elements{e}")
    
    def dir_login(self, email:str, password:str, url:str):
        """Login into an account directly throught page"""

        GO_LOGIN_BUTTON_XPATH = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/a"
        
        LOGIN_EMAIL_TEXTBOX_XPATH = "//input[@name = 'email']"
        LOGIN_PASSOWRD_TEXTBOX_XPATH = "//input[@name = 'pass']"
        LOGIN_BUTTON_XPATH = "//button[@name='login']"

        self.driver.get(url)

        # Search for email textBox, password textBox, and login button
        try:
            go_login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, GO_LOGIN_BUTTON_XPATH))) 
            go_login_button.click()

            email_textBox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, LOGIN_EMAIL_TEXTBOX_XPATH)))
            password_textBox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, LOGIN_PASSOWRD_TEXTBOX_XPATH)))
            login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, LOGIN_BUTTON_XPATH)))

            email_textBox.send_keys(email)
            password_textBox.send_keys(password)
            login_button.click()
            

        except (TimeoutException or ElementNotInteractableException) as e:
            print(e)

    def logout(self, logout_button_xpath2=None):
        """Logout from account"""

        MENU_BUTTON_XPATH = "//div[@aria-label='Account' or @aria-label='More options' or @aria-label='الحساب' or @aria-label='خيارات إضافية']"
        LOUTGOUT_BUTTON1_XPATH = "//span[contains(text(),'Log Out') or contains(text(),'تسجيل الخروج')]"                      
        LOUTGOUT_BUTTON2_XPATH = "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div/span/span[contains(text(),'Log Out') or contains(text(),'تسجيل الخروج')]"
        
        # Search for the menu button and logout button    
        try: 
            menu_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, MENU_BUTTON_XPATH)))
            menu_button.click() 

            logout_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, LOUTGOUT_BUTTON1_XPATH)))
            logout_button.click()

            if(logout_button_xpath2 != None):
                logout_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, LOUTGOUT_BUTTON2_XPATH)))
                logout_button.click()


        except (WebDriverException, TimeoutException, NoSuchElementException) as e:
            pass
    
    def chat(self, message:str, profile_path:str):
        """Chat with a person"""

          
        MESSAGE_BUTTON_XPATH = "//div[@aria-label='Message' or @aria-label='مراسلة']"
        MESSAGE_TEXTBOX_XPATH = "//div[@aria-label='Aa']"

        # Search for message button and send a message
        try:
            self.go_to(profile_path)
            
            message_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, MESSAGE_BUTTON_XPATH)))
            message_button.click()

            message_text_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, MESSAGE_TEXTBOX_XPATH)))
            message_text_box.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
            message_text_box.send_keys(message)
            message_text_box.send_keys(Keys.ENTER)

        except TimeoutException as e:
            pass
    
    def add_comment_on_post(self, post_path:str, comment:str):
        """Add comment on a post"""

        COMMENT_TEXTBOX_XPATH = "//div[@aria-label='Write a comment' or @aria-label='كتابة تعليق'][@role='textbox']"


        try:
            self.go_to(post_path)

            post_comment_box = WebDriverWait(self.driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, COMMENT_TEXTBOX_XPATH)))[0]
            post_comment_box.send_keys(comment)
            post_comment_box.send_keys(Keys.ENTER)
            
        except (TimeoutException or ElementClickInterceptedException or ElementNotInteractableException) as e:
            self.logger_wrt_error(f"Can't find comment box web elements{e}")
         
    def add_like_on_post(self, post_path:str):
        """Add like to a post"""

        LIKE_BUTTON_XPATH = "//div[@aria-label='Like' or @aria-label='أعجبني'][@role='button']"
        
        try:
            self.go_to(post_path)

            
            like_button = WebDriverWait(self.driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, LIKE_BUTTON_XPATH)))[1]
            like_button.click()

        except TimeoutException as e:
            self.logger_wrt_error(f"Can't find post's like button web element{e}")

    def add_page_following(self, page_path:str):
        """Add following for a page"""

        PAGE_FOLLOW_BUTTON_XPATH = "//div[@aria-label='Follow' or @aria-label='متابعة'][@role='button']"
                                
        try:
            
            self.go_to(page_path)
            
            follow_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, PAGE_FOLLOW_BUTTON_XPATH)))
            follow_button.click()

        except TimeoutException as e:
            self.logger_wrt_error(f"Can't find page following button web element{e}")

    def add_like_on_page(self, page_path:str):
        """Add like on a page"""

        PAGE_LIKE_BUTTON_XPATH = "//div[@aria-label='Like' or @aria-label='أعجبني'][@role='button']"

        try:
            self.go_to(page_path)

            like_button = WebDriverWait(self.driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, PAGE_LIKE_BUTTON_XPATH)))[0]
            like_button.click()    
        except TimeoutException as e:
            self.logger_wrt_error(f"Can't find page like button web element{e}")

    def add_person(self, profile_path:str,):
        """Add person"""

        ADD_PERSON_BUTTON_XPATH = "//span[contains(text(),'Add Friend') or contains(text(),'إضافة صديق')]"
       

        try:
            
            self.go_to(profile_path)
            
            add_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, ADD_PERSON_BUTTON_XPATH)))
            add_button.click()

        except TimeoutException as e:
            pass
    
    def accept_person(self, profile_path:str):
        """Accept person"""

        ACCEPT_PERSON_BUTTON_XPATH1 = "//span[contains(text(),'Respond') or contains(text(),'تأكيد الطلب')]"
        ACCEPT_PERSON_BUTTON_XPATH2 = "//span[contains(text(),'Confirm') or contains(text(),'تأكيد')]"

        try:
            
            self.go_to(profile_path)
            
            add_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, ACCEPT_PERSON_BUTTON_XPATH1)))
            add_button.click()

            add_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, ACCEPT_PERSON_BUTTON_XPATH2)))
            add_button.click()

        except TimeoutException as e:
            pass

    def get_num_of_friends(self, profile_path:str):
        """Calculate the number of friends for specific profile"""

        NUM_OF_FRIENDS1_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]/div[1]/span/span[2]"
        NUM_OF_FRIENDS2_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a"  
        

        self.go_to(profile_path)
        
        try:
            num_of_friends = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, NUM_OF_FRIENDS1_XPATH)))
        
        except TimeoutException: 
            try:
                num_of_friends2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, NUM_OF_FRIENDS2_XPATH)))
            
            except TimeoutException: 
                pass 
            else: 
                return re.findall(pattern=r'\d+', string=num_of_friends2.text)[0]
            
        else: 
            return num_of_friends.text

        return 0 

    def get_profile_link(self):
        """Obtain profile link(path) after login into it"""

        PROFILE_LINK_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a"

        try:
            profile_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, PROFILE_LINK_XPATH)))
            return profile_link.get_attribute('href')
        except TimeoutException:
            pass
        
    def is_account_active(self):
        """Check if an account is active"""
    
        pat = QtCore.QRegularExpression(r'/checkpoint/')
        return not pat.match(self.driver.current_url).hasMatch()

