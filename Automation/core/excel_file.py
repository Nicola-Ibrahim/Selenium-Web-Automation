from abc import ABC
from typing import Dict, List
import openpyxl
import pandas as pd
from pandas.core.frame import DataFrame 

class ExcelFile():
    """Class is responssible for opening an Excel file for reading and editing"""
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        
        # For editing
        self.worker_book = openpyxl.load_workbook(file_path)
        self.sheet =  self.worker_book.active  

        # For reading
        # self.data: DataFrame = self.read_data()
        self.data: Dict
        self.headers: List


    
    
class FacebookAccountsExcelFile(ExcelFile):
    def read_data(self):
        data = pd.read_excel(self.file_path, usecols=['Id', 'Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name', 'Group', 'Added Friends', 'Mac address'])
        data.dropna(thresh=4, inplace=True)
        return data
    
    

        
class FacebookCommentsExcelFile(ExcelFile):
    def read_data(self):
        data = pd.read_excel(self.file_path, usecols=['Comments', 'Type'])
        data.dropna(inplace=True)
        return data

class SelectedData(ABC):
    """Class is responsible for holding only desire accounts and comments data from the client"""
    def __init__(self, accounts_file: ExcelFile , start:int , end:int) -> None:
        """"""
        self.accounts_file = accounts_file
        self.desire_accounts_data = self.accounts_file.data[start:end]


        # self.num_of_workers:int = num_of_workers
        # self.accounts_data_splits = {}
        
        # accounts_data_splits = self.splitting_fn(self.selected_data.accounts_data, num_of_workers)

class SelectedDataWithoutComments(SelectedData):
    """"""
        

class SelectedDataWithComments(SelectedData):
    def __init__(self, accounts_file: ExcelFile, start: int, end: int, comments_file: ExcelFile, comments_type:str) -> None:
        super().__init__(accounts_file, start, end)
        self.comments_file  = comments_file
        self.desire_comments_data = self.comments_file.data[self.comments_file.data['Type'] == comments_type]
