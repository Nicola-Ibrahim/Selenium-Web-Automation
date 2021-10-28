"""
This the parent class that can be inherited to automate any website_url. 
If some forms as (login or logout ets...) have different shape then the method that responsiable about 
that should be overriden.  
"""
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.action_chains import ActionChains


from abc import ABC, abstractmethod
from typing import NewType
import numpy as np
import logging



type = NewType('type', )

class WebDriver(ABC):
    @abstractmethod
    def init_driver(self):
        pass

class ChromeWebDriver(WebDriver):
    def init_driver(self):
        # capa = DesiredCapabilities.CHROME
        # capa["pageLoadStrategy"] = "none"
        
        options = Options()
        # options.add_argument('--headless')
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications" : 2})
        options.add_experimental_option("prefs", {"enable_do_not_track": True})
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        options.add_argument("--incognito")
        return webdriver.Chrome(executable_path='chromedriver.exe', options=options)


class FirefoxWebDriver(WebDriver):
    def init_driver(self):            
        return webdriver.Firefox(executable_path='geckodriver.exe')


class WebSiteAutomator(ABC):
    def __init__(self, driver: WebDriver, website_url:str) -> None:
        self.website_url = website_url
        self.driver: webdriver = driver.init_driver()

        # Navigate to specific website_url
        self.driver.get(self.website_url)

    def init_logger(self, path:str):
        """Intial new logger
        path: logger file path
        """
        
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(filename=path, mode='w')
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(message)s"))
        logger.addHandler(handler)

        return logger
    
    @abstractmethod
    def sign_up(self):
        pass

    @abstractmethod
    def login(self):
        """Login into an account"""
        pass
            
    @abstractmethod
    def logout(self):
        """Logout from account"""
        pass

    
    @abstractmethod
    def add_comment_on_post(self):
        """Add comment on a post"""
        pass
        
    @abstractmethod
    def add_like_on_post(self):
        """Add like to a post"""
        pass

    @abstractmethod
    def add_page_following(self):
        """Add following for a page"""
        pass
        
    @abstractmethod
    def add_person(self):
        """Add person"""
        pass

    @abstractmethod
    def accept_person(self):
        """Accept person"""
        pass

    @staticmethod
    def simple_splitting(accounts_data, num_of_splits):
        """ Splitting data frame into multiple frames depending on the number of threads"""

        # Get thee df index 
        df_indices = accounts_data.index.values

        # Calculate the number of items in each splitted group
        number_of_elements_each_group  = int(np.ceil(len(df_indices) / num_of_splits))

        # Gettign indices for each group
        groups_indices = [group for group in np.split(df_indices, df_indices[0::number_of_elements_each_group]) if group.size != 0]

        # Getting df groups
        groups_items_df = [accounts_data.iloc[indx, :] for indx in groups_indices]

        return groups_items_df

    @staticmethod
    def enhanced_splitting(accounts_data, num_of_splits):
        """ Splitting data frame into multiple frames depending on the number of threads"""
        return np.array_split(accounts_data, num_of_splits)

        