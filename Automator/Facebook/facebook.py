"""
This file is reponsible for autmating many facebook website.
A file should be used to store facebook accounts (email, password) and use them to login.
"""

import logging
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from Automator.Auto_Core.WebAutomation import WebDriver, WebSiteAutomator

import re
import time
import openpyxl
from datetime import datetime


class FacbookAutomator(WebSiteAutomator):
    """Parent class automator"""

    def __init__(self, driver: WebDriver, accounts_file_path, accounts_data, comments_data = None) -> None:
        
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
        self._COMMENT_TEXTBOX_XPATH1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/form/div/div/div[1]"
        self._COMMENT_TEXTBOX_XPATH2 =  "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/form/div/div/div[1]"
        # self._COMMENT_TEXTBOX_XPATH = "//div[@aria-label='Write a comment' or @aria-label='كتابة تعليق'][@role='textbox']"


        self._LIKE_BUTTON_XPATH1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/span"
        self._LIKE_BUTTON_XPATH2 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/span/span"
        self._LIKE_BUTTON_XPATH3 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]"
        self._LIKE_BUTTON_XPATH4 =   "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]"
                                    
        # self._LIKE_BUTTON_XPATH = "//div[@aria-label='Like' or @aria-label='أعجبني'][@role='button']"
                                    
        # self._PAGE_FOLLOW_BUTTON_XPATH = "//span[contains(text(),'Like') or contains(text(),'أعجبني')]"
        self._PAGE_FOLLOW_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div"
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


        # # create new logger for testing 
        # self._logger = self.init_logger("./logs/Facebook accounts logout info.log")

       
        # Edit accounts file
        self.worker_book = openpyxl.load_workbook(self.accounts_file_path)
        self.sheet =  self.worker_book.active  

        self.website_url = "https://www.facebook.com/"

        super().__init__(driver, self.website_url) 


    
    def sign_up(self, first_name:str, last_name:str, email:str, password:str, date_of_birth, gender):
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
    
    def login(self, email:str, password:str):
        """Login into an account"""

        self.driver.get(self.website_url)

        # Search for email textBox, password textBox, and login button
        try:
            email_textBox = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self._LOGIN_EMAIL_TEXTBOX_XPATH)))
            password_textBox = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self._LOGIN_PASSOWRD_TEXTBOX_XPATH)))
            login_button = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self._LOGIN_BUTTON_XPATH)))

            email_textBox.send_keys(email)
            password_textBox.send_keys(password)
            login_button.click()
            

        except TimeoutException as e:
            pass
    
    def logout(self, logout_button_xpath2=None):
        """Logout from account"""
        # Search for the menu button and logout button    
        try: 
            menu_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self._MENU_BUTTON_XPATH)))
            menu_button.click() 

            logout_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self._LOUTGOUT_BUTTON1_XPATH)))
            logout_button.click()

            if(logout_button_xpath2 != None):
                logout_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self._LOUTGOUT_BUTTON2_XPATH)))
                logout_button.click()


        except (WebDriverException, TimeoutException, NoSuchElementException) as e:
            pass
    
    def chat(self, message:str, profile_path:str):
        """Chat with a person"""

        # Search for message button and send a message
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            if(self.driver.current_url != profile_path):
                self.driver.get(profile_path)
            
            message_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._MESSAGE_BUTTON_XPATH)))
            message_button.click()

            message_text_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._MESSAGE_TEXTBOX_XPATH)))
            message_text_box.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
            message_text_box.send_keys(message)
            message_text_box.send_keys(Keys.ENTER)

        except TimeoutException as e:
            pass
    
    def add_comment_on_post(self, post_path:str, comment:str):
        """Add comment on a post"""

        try:
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            
            if(self.driver.current_url != post_path):
                self.driver.get(post_path)
            
            post_comment_box = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._COMMENT_TEXTBOX_XPATH1)))
            post_comment_box.send_keys(comment)
            post_comment_box.send_keys(Keys.ENTER)

        except (TimeoutException or ElementClickInterceptedException or ElementNotInteractableException) as e:
            try:
                post_comment_box = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._COMMENT_TEXTBOX_XPATH2)))
                post_comment_box.send_keys(comment)
                post_comment_box.send_keys(Keys.ENTER)
            
            except:
                pass
        
    def add_like_on_post(self, post_path:str):
        """Add like to a post"""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            if(self.driver.current_url != post_path):
                self.driver.get(post_path)

            
            like_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._LIKE_BUTTON_XPATH1)))
            like_button.click()
        
        except TimeoutException as e:
            try:
                like_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._LIKE_BUTTON_XPATH2)))
                like_button.click()
            except TimeoutException as e:
                    try:
                        like_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._LIKE_BUTTON_XPATH3)))
                        like_button.click()
                    except:
                        try:
                            like_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._LIKE_BUTTON_XPATH4)))
                            like_button.click()
                        except:
                            pass

    def add_page_following(self, page_path:str):
        """Add following for a page"""
        try:
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            if(self.driver.current_url != page_path):
                self.driver.get(page_path)
            
            follow_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._PAGE_FOLLOW_BUTTON_XPATH)))
            follow_button.click()
        except TimeoutException as e:
            try:
                
                like_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._PAGE_LIKE_BUTTON_XPATH)))
                like_button.click()    
            except:
                pass
        
    def add_person(self, profile_path:str,):
        """Add person"""
        try:
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//head")))
            if(self.driver.current_url != profile_path):
                self.driver.get(profile_path)
            
            add_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._ADD_PERSON_BUTTON_XPATH)))
            add_button.click()

        except TimeoutException as e:
            pass
    
    def accept_person(self, profile_path:str):
        """Accept person"""
        try:
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//head")))
            if(self.driver.current_url != profile_path):
                self.driver.get(profile_path)
            
            add_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._ACCEPT_PERSON_BUTTON_XPATH1)))
            add_button.click()

            add_button = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self._ACCEPT_PERSON_BUTTON_XPATH2)))
            add_button.click()

        except TimeoutException as e:
            pass

    def get_num_of_friends(self, profile_path:str):
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

    def get_profile_link(self):
        """Obtain profile link(path) after login into it"""
        try:
            profile_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self._PROFILE_LINK_XPATH)))
            return profile_link.get_attribute('href')
        except TimeoutException:
            pass
        
    def is_account_active(self):
        """Check if an account is active"""
        try:
            
            label = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self._LOCKED_PROFILE_TEXT_XPATH)))
            if(label.text in ("تم تعطيل حسابك", "Your account has been disabled")):
                return False

        except TimeoutException:
            return True
