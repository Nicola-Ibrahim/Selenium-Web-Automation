from selenium.common.exceptions import TimeoutException
from ..WebAutomation import WbAutomator 

import logging
from time import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class Instagram(WbAutomator):
    def __init__(self, website) :
        super().__init__(website=website)

        self._MENU_BUTTON_XPATH = "//div[@aria-label='Account' or @aria-label='الحساب']"
        self._LOUTGOUT_BUTTON_XPATH = "//span[contains(text(),'Log Out') or contains(text(),'تسجيل الخروج')]"


        self._LOGIN_USERNAME_TEXTBOX_XPATH = "//input[@name = 'username']"
        self._LOGIN_PASSOWRD_TEXTBOX_XPATH = "//input[@name = 'password']"
        self._LOGIN_BUTTON_XPATH = "//button[@type = 'submit']"

        self._SIGNUP_EMAIL_TEXTBOX_XPATH = "//input[@name = 'emailOrPhone']"
        self._SIGNUP_NAME_TEXTBOX_XPATH = "//input[@name = 'fullName']"
        self._SIGNUP_USERNAME_TEXTBOX_XPATH = "//input[@name = 'username']"
        self._SIGNUP_PASSWORD_TEXTBOX_XPATH = "//input[@name = 'password']"
        self._SIGNUP_BUTTON_XPATH = "//button[@type = 'submit']"
        
        
        self._MESSAGE_BUTTON_XPATH = "//div[@aria-label='Message' or @aria-label='مراسلة']"
        self._MESSAGE_TEXTBOX_XPATH = "//div[@aria-label='Aa']"

        self._COMMENT_TEXTBOX_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/div/div/div/form/div/div/div[2]/div/div/div/div"
        self._LIKE_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]"

        self._FOLLOW_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/span/span[contains(text(),'Like') or contains(text(),'أعجبني')]"

        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler("/logs/Instagram accounts logout info.log", mode='w')
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(message)s"))
        
        self._logger.addHandler(handler)

    def signUp(self, email, full_name, username, password):
        try:
            email_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_EMAIL_TEXTBOX_XPATH)))
            name_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_NAME_TEXTBOX_XPATH)))
            username_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_USERNAME_TEXTBOX_XPATH)))
            password_textBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_PASSWORD_TEXTBOX_XPATH)))
            logut_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._SIGNUP_BUTTON_XPATH)))

            email_textBox.send_keys(email)
            name_textBox.send_keys(full_name)
            username_textBox.send_keys(username)
            password_textBox.send_keys(password)
            logut_button.click()
            
        except TimeoutException as e:
            pass

    def login(self, email, password):
        return super().login(email, password, self._LOGIN_USERNAME_TEXTBOX_XPATH, self._LOGIN_PASSOWRD_TEXTBOX_XPATH, self._LOGIN_BUTTON_XPATH)
            
    def logout(self):
        return super().logout(self._MENU_BUTTON_XPATH, self._LOUTGOUT_BUTTON_XPATH)
        
    def addComment(self, post_path, comment):
        return super().addComment(post_path, comment, self._COMMENT_TEXTBOX_XPATH)


    def addLikeOnPost(self, post_path):
        return super().addLikeOnPost(post_path, self._LIKE_BUTTON_XPATH)        

    def addPageFollowing(self, page_path):
        return super().addPageFollowing(page_path, self._FOLLOW_BUTTON_XPATH)        


    def addPageFollowingWorker(self, accounts_data, page_path):
        
        for _, row in accounts_data.iterrows():
            start = time.perf_counter()

            self.login(email=row['email'], password=row['password2'])
            self.addPageFollowing(page_path=page_path)
            self.logout()
            finish = time.perf_counter()
            self._logger.info(f"""Logout from "{row['name']}" in {round(finish-start,2)} second(s)""")
