
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver
import time

class CustomeWebDriver(ABC):
    """Custome driver class"""
    def __init__(self) -> None:
        self.driver: WebDriver = None
        

    
    def get_rquest_header(self):
        """Get the request information"""

        headers = self.driver.execute_script(
            """var req = new XMLHttpRequest();
            req.open('GET', document.location, false);
            req.send(null);
            return req.getAllResponseHeaders()"""
            )
        headers = headers.splitlines()
        print(headers)

        ##  Print request headers
        for request in self.driver.requests:
            print(
                request.url,
                request.params,
                request.querystring,
                sep='\n'+'-'*40
            )
    
    def delete_data(driver):
        """Clear driver data and cash"""
        driver.execute_script("window.open('');")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        driver.get('chrome://settings/clearBrowserData')
        time.sleep(1)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
        actions.perform()
        time.sleep(1)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
        actions.perform()
        time.sleep(1) # wait some time to finish
        driver.close() # close this tab
        driver.switch_to.window(driver.window_handles[0]) # switch back
     
    def open_new_tab(self):
        """Open a new tab with deleting all cookies"""
        # Delete all cookies
        self.driver.delete_all_cookies()

        # Delete session storage
        self.driver.execute_script("window.sessionStorage.clear()")
        # self.driver.execute_script(f"""window.open("{self.facebook.website_url}","_blank")""")              

        # Open a new blank window
        self.driver.execute_script(f"""window.open("","_blank")""")              

        # Close current window
        self.driver.close()

        # Switch to focuse to the new created win
        self.driver.switch_to_window(self.driver.window_handles[0])

    def close(self):
        self.driver.close()

    @abstractmethod
    def init_driver(self):
        """initial a new driver with desire optinons and capabilities"""


class ChromeWebDriver(CustomeWebDriver):
    """Chrome driver class with desired options"""
    
    def init_driver(self):
        # capa = DesiredCapabilities.CHROME
        # capa["pageLoadStrategy"] = "none"
        
        options = Options()
        # options.add_argument('--headless')
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications" : 2})
        options.add_experimental_option("prefs", {"enable_do_not_track": True})
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation" :2})
        options.add_experimental_option("prefs", {"enable_do_not_track": True})
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        # return driver


class FirefoxWebDriver(CustomeWebDriver):
    """Firefox driver class with desired options"""
    def init_driver(self):            
        self.driver =  webdriver.Firefox(executable_path='geckodriver.exe')
        # return driver

