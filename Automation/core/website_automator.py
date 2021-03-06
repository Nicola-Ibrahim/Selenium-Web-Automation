"""
This the parent class that can be inherited to automate any website_url. 
If some forms as (login or logout ets...) have different shape then the method that responsible about 
that should be overridden.  
"""

from logging import Logger
import requests
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from abc import ABC, abstractmethod


class WebSiteAutomator(ABC):
    """Main automator class that configs necessary functions to be inhereted"""
    def __init__(self, driver: WebDriver, website_url:str) -> None:
        self.driver: WebDriver = driver
        self.website_url = website_url
        
        self._logger:Logger = self.init_logger()
    
    def logger_wrt_error(self, msg) -> None:
        """Write an error in log file occures during execution"""
        self._logger.error(msg=msg)

    def logger_wrt_info(self, msg) -> None:
        """Write an information about execution process in log file"""
        self._logger.info(msg=msg)
        
    def is_connected(self):
        """Check if there is a connection to the internet"""

        
        while(not self.get_response(self.website_url)):
            # self.logger_wrt_error("Not connected to the enternet")
            pass
            
        self.logger_wrt_info("Connected to the enternet...!")
            
        return True
    
    def __is_reachable(self) -> bool:
        """Check if the website can be reached"""

        REACHABLE_XPATH = "//span[contains(text(),'This site can’t be reached') or contains(text(),'No internet') or contains(text(),'Your connection was interrupted')]"

        try:
            WebDriverWait(self.driver, 1).until_not(EC.presence_of_element_located((By.XPATH, REACHABLE_XPATH)))            
            
            
        except TimeoutException:
            # self.logger_wrt_error("The website is not reachable")
            return False
        
        else:
            # self.logger_wrt_info("The website is reachable")
            return True
    
    def is_reached(self) -> bool:
        if(self.is_connected()):
            self.driver.get(self.website_url)
    
            while(not self.__is_reachable()):
                self.driver.refresh()
                self.logger_wrt_error(f"The {self.website_url} website is not reachable")
                # self.logger_wrt_error(f"UnsuccessfulLy reach to the {self.website_url}")
            
            self.logger_wrt_info(f"The {self.website_url} website is reachable")
            # self.logger_wrt_info(f"Successfully reach to the {self.website_url}")
            return True
                    
            
    def get_response(self, url:str, timeout:int = 10) -> bool:
        """Get a response from the url to check if there is any connectino"""
        try:
            #r = requests.get(url, timeout=timeout)
            r = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError as ex:
            return False

    

    
    @abstractmethod
    def init_logger(self):
        """Intial new logger
        path: logger file path
        """
  
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



# def simple_splitting(data, num_of_splits):
#     """ Splitting data frame into multiple frames depending on the number of threads"""

#     # Get thee df index 
#     df_indices = data.index.values

#     # Calculate the number of items in each splitted group
#     number_of_elements_each_group  = int(np.ceil(len(df_indices) / num_of_splits))

#     # Gettign indices for each group
#     groups_indices = [group for group in np.split(df_indices, df_indices[0::number_of_elements_each_group]) if group.size != 0]

#     # Getting df groups
#     groups_items_df = [data.iloc[indx, :] for indx in groups_indices]

#     return groups_items_df

# def enhanced_splitting(data, num_of_splits):
#     """ Splitting data frame into multiple frames depending on the number of threads"""
#     return np.array_split(data, num_of_splits)

    