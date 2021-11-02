
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.action_chains import ActionChains

from abc import ABC, abstractmethod

class CustomeWebDriver(ABC):
    @abstractmethod
    def init_driver(self):
        pass

class ChromeWebDriver(CustomeWebDriver):
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


class FirefoxWebDriver(CustomeWebDriver):
    def init_driver(self):            
        return webdriver.Firefox(executable_path='geckodriver.exe')

