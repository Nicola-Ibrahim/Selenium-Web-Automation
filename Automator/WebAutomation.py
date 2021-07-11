"""
This the parent class that can be inherited to automate any website. 
If some forms as (login or logout ets...) have different shape then the method that responsiable about 
that should be overriden.  
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


import numpy as np


class WbAutomator():
    """Parent class automator"""
    def __init__(self, website):
        """Initial a Chrome driver"""

        # capa = DesiredCapabilities.CHROME
        # capa["pageLoadStrategy"] = "none"

        
        options = Options()
        # options.add_argument('--headless')
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications" : 2})
        options.add_experimental_option("excludeSwitches", ['enable-logging'])

        self.driver = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe', options=options)
        self.website = website
        self.waiting_time = 10

        # Change window size
        # self.driver.set_window_size(400,600)

        # Navigate to specific website
        self.driver.get(self.website)

    def signUp(self):
        pass

    def login(self, email, password, email_xpath, pass_xpath, login_button_xpath):
        """Login into an account"""
        # Search for email textBox, password textBox, and login button
        try:
            email_textBox = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, email_xpath)))
            password_textBox = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, pass_xpath)))
            login_button = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))

            email_textBox.send_keys(email)
            password_textBox.send_keys(password)
            login_button.click()
            

        except TimeoutException as e:
            pass
    
    def logout(self, menu_xpath, logout_button_xpath):
        """Logout from account"""
        # Search for the menu button and logout button    
        try: 
            menu_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, menu_xpath)))
            menu_button.click() 

            logout_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, logout_button_xpath)))
            logout_button.click()

            self.driver.get(self.website)

        except (TimeoutException, NoSuchElementException) as e:
            pass
    
    def chat(self, message, profile_path, message_button_xpath, message_box_xpath):
        """Chat with a person"""

        # Search for message button and send a message
        try:
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            self.driver.get(profile_path)
            
            message_button = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, message_button_xpath)))
            message_button.click()

            message_text_box = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, message_box_xpath)))
            message_text_box.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
            message_text_box.send_keys(message)
            message_text_box.send_keys(Keys.ENTER)

        except TimeoutException as e:
            pass
    
    def addComment(self, post_path, comment, comment_box_xpath):
        """Add comment on a post"""
        try:
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            self.driver.get(post_path)


            post_comment_box = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, comment_box_xpath)))
            post_comment_box.click()
            post_comment_box.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
            post_comment_box.send_keys(comment)
            post_comment_box.send_keys(Keys.CONTROL, 'a', Keys.DELETE)

        except TimeoutError as e:
            pass 
    
    def addLikeOnPost(self, post_path, like_button_xpath):
        """Add like to a post"""
        try:
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            self.driver.get(post_path)

            
            like_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, like_button_xpath)))
            like_button.click()
        
        except TimeoutError as e:
            pass

    def addPageFollowing(self, page_path, follow_button_xpath):
        """Add following for a page"""
        try:
            
            # //body[@class='_6s5d _71pn _-kb segoe']
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, "//html[@id='facebook']")))
            
            self.driver.get(page_path)
            
            follow_button = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, follow_button_xpath)))
            follow_button.click()

        except TimeoutError as e:
            pass
        
    def addPerson(self, profile_path, add_button_xpath):
        """Add person"""
        try:
            
            # //body[@class='_6s5d _71pn _-kb segoe']
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, "//head")))
            
            self.driver.get(profile_path)
            
            add_button = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, add_button_xpath)))
            add_button.click()

        except TimeoutError as e:
            pass

    # def __enter__(self):
    #     print('Start testing')
    #     return self
      
    # def __exit__(self, exc_type, exc_value, exc_traceback):
    #     print('End testing')
    #     self.driver.quit()
    
    

def splitting(data, num_of_splits):
    """Splitting data frame into multiple frames depending on the number of threads"""

    # Get thee dataFrame index 
    df_indices = data.index.values

    # Calculate the number of items in each splitted group
    number_of_elements_each_group  = int(np.ceil(len(df_indices) / num_of_splits))

    # Gettign indices for each group
    groups_indices = [group for group in np.split(df_indices, df_indices[0::number_of_elements_each_group]) if group.size != 0]

    # Getting df groups
    groups_items_df = [data.iloc[indx, :] for indx in groups_indices]

    return groups_items_df



    
