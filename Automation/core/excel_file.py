from abc import ABC
import openpyxl
import pandas as pd
from pandas.core.frame import DataFrame 


class ExcelFile:    
    """Class is responssible for opening an Excel file to read and edit"""

    def __init__(self, file_path) -> None:
        self.file_path:str = file_path
        self.worker_book = openpyxl.load_workbook(self.file_path)
        self.sheet =  self.worker_book.active  
        self.data:DataFrame = self.read_data()

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
        self.accounts_file:ExcelFile = accounts_file
        self.desire_accounts_data:DataFrame = self.accounts_file.data[start:end]


        # self.num_of_workers:int = num_of_workers
        # self.accounts_data_splits = {}
        
        # accounts_data_splits = self.splitting_fn(self.selected_data.accounts_data, num_of_workers)

class SelectedDataWithoutComments(SelectedData):
    """Class is responsible for holding only selected accounts data"""
        

class SelectedDataWithComments(SelectedData):
    """Class is responsible for holding only selected accounts and comments data"""

    def __init__(self, accounts_file: ExcelFile, start: int, end: int, comments_file: ExcelFile, comments_type:str) -> None:
        super().__init__(accounts_file, start, end)
        self.comments_file:ExcelFile  = comments_file
        self.desire_comments_data:DataFrame = self.comments_file.data[self.comments_file.data['Type'] == comments_type]
