


from abc import ABC, abstractmethod
from typing import Callable

from pandas.core.frame import DataFrame

from Automation.core.drivers import CustomeWebDriver
from Automation.core.website_automator import enhanced_splitting
from Automation.facebook_automation.tasks import CommentOnPost, FacebookInteraction, LikeAndCommentOnPost, LikeOnPost, PageFollowing
from Automation.facebook_automation.view import FacebookView
from Automation.core.ChangeMac import MacChanger

class MainWorker(ABC):
    def __init__(self, num_of_workers:int, driver:CustomeWebDriver, mac_changer:MacChanger, accounts_file_path:str, accounts_data:DataFrame, url:str, parent:FacebookView) -> None:
        
        self.driver: CustomeWebDriver = driver
        self.mac_changer: MacChanger = mac_changer
        self.accounts_file_path: str = accounts_file_path
        self.accounts_data:DataFrame = accounts_data
        self.url: str = url
        self.view: FacebookView = parent
        self.worker: FacebookInteraction
        self.splitting_fn = enhanced_splitting

        self.create_workers(num_of_workers)
    
        
    def create_workers(self, num_of_workers):
        """Create workers depending on the number of desire workers"""

        # split accounts data frame into subsets depending on the number of threads
        accounts_data_splits = self.splitting_fn(self.accounts_data, num_of_workers)
        
        for i in range(num_of_workers):
            self.setup_worker(accounts_data_splits[i])

    @abstractmethod
    def setup_worker(self, acc_data):
        """Setup a new worker"""
    
    @abstractmethod
    def connect(self):
        """Connect worker signals to related function"""
    


class LikesOnPostWorker(MainWorker):


    def setup_worker(self, acc_data):
        self.worker = LikeOnPost(
            self.driver, 
            self.mac_changer, 
            self.accounts_file_path, 
            acc_data, 
            self.url, 
            self.view
        )
        self.connect()
        self.worker.start()

    def connect(self):
        self.worker.passed_acc_counter.connect(lambda count: self.view.comments_counter_lbl.setText(f"{count}"))
        self.worker.run_error.connect(lambda ind, name: self.view.run_error_lbl2.setStyleSheet("color: rgb(255,0,0);"))
        self.worker.run_error.connect(lambda ind, name: self.view.run_error_lbl2.setText(f"Error occured at -> {ind} : {name}"))
        self.worker.finished.connect(lambda: self.view.add_likes_run_btn.setEnabled(True))
        self.worker.finished.connect(lambda: self.view.likes_counter_lbl.setText('0'))
        self.worker.finished.connect(self.worker.deleteLater)

class CommentsOnPostWorker(MainWorker):
    
    def __init__(self, num_of_workers: int, driver: CustomeWebDriver, mac_changer: MacChanger, accounts_file_path: str, accounts_data: DataFrame, comments_data:DataFrame, url: str, parent: FacebookView) -> None:
        self.comments_data: DataFrame = comments_data
        super().__init__(num_of_workers, driver, mac_changer, accounts_file_path, accounts_data, url, parent)


    
    def setup_worker(self, acc_data):
        self.worker = CommentOnPost(
            self.driver, 
            self.mac_changer, 
            self.accounts_file_path, 
            acc_data, 
            self.comments_data, 
            self.url, 
            self.view
        )
        self.connect()
        self.worker.start()

    def connect(self):
        self.worker.passed_acc_counter.connect(lambda count: self.view.comments_counter_lbl.setText(f"{count}"))
        self.worker.run_error.connect(lambda ind, name: self.view.run_error_lbl1.setStyleSheet("color: rgb(255,0,0);"))
        self.worker.run_error.connect(lambda ind, name: self.view.run_error_lbl1.setText(f"Error occured at -> {ind} : {name}"))
        self.worker.finished.connect(lambda: self.view.add_comments_run_btn.setEnabled(True))
        self.worker.finished.connect(lambda: self.view.comments_counter_lbl.setText('0'))
        self.worker.finished.connect(self.worker.deleteLater)

class LikesAndCommentsOnPostWorker(MainWorker):

    def __init__(self, num_of_workers: int, driver: CustomeWebDriver, mac_changer: MacChanger, accounts_file_path: str, accounts_data: DataFrame, comments_data:DataFrame, url: str, parent: FacebookView) -> None:
        self.comments_data: DataFrame = comments_data
        super().__init__(num_of_workers, driver, mac_changer, accounts_file_path, accounts_data, url, parent)


    
    def setup_worker(self, acc_data):
        self.worker = LikeAndCommentOnPost(
            self.driver, 
            self.mac_changer, 
            self.accounts_file_path, 
            acc_data, 
            self.comments_data, 
            self.url, 
            self.view
        )
        self.connect()
        self.worker.start()

    def connect(self):
        self.worker.passed_acc_counter.connect(lambda count: self.view.comments_counter_lbl.setText(f"{count}"))
        self.worker.run_error.connect(lambda ind, name: self.view.run_error_lbl3.setStyleSheet("color: rgb(255,0,0);"))
        self.worker.run_error.connect(lambda ind, name: self.view.run_error_lbl3.setText(f"Error occured at -> {ind} : {name}"))
        self.worker.finished.connect(lambda: self.view.add_likes_comments_run_btn.setEnabled(True))
        self.worker.finished.connect(lambda: self.view.comments_likes_counter_lbl.setText('0'))
        self.worker.finished.connect(self.worker.deleteLater)

class PageFollowingWorker(MainWorker):


    def setup_worker(self, acc_data):
        self.worker = PageFollowing(
            self.driver, 
            self.mac_changer, 
            self.accounts_file_path, 
            acc_data, 
            self.url, 
            self.view
        )
        self.connect()
        self.worker.start()

    def connect(self):
        self.worker.passed_acc_counter.connect(lambda count: self.page_followings_counter_lbl.setText(f"{count}"))
        self.worker.run_error.connect(lambda ind, name : self.run_error_lbl4.setStyleSheet("color: rgb(255,0,0);"))
        self.worker.run_error.connect(lambda ind, name: self.run_error_lbl4.setText(f"Error occured at -> {ind} : {name}"))
        self.worker.finished.connect(lambda: self.view.add_likes_run_btn.setEnabled(True))
        self.worker.finished.connect(lambda: self.view.likes_counter_lbl.setText('0'))
        self.worker.finished.connect(lambda : self.add_page_followings_run_btn.setEnabled(True))
        self.worker.finished.connect(self.worker.deleteLater)
