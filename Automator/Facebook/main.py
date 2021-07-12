from ..WebAutomation import splitting
import pandas as pd
from .facebook import Facebook
import threading
import os

def facebookMain():
        
    # Read accounts file
    accounts_file_path = os.path.join(os.path.dirname(__file__), "Facebook Accounts.xlsx")
    facebook_accounts_file = pd.read_excel(accounts_file_path, usecols=['Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name'])


    profile_path = """any profile path"""
    post_path = """https://www.facebook.com/permalink.php?story_fbid=2924099864529968&id=2150524478554181"""
    page_path = """any page path"""


    # Number of threads to be run
    threads = []
    NUM_OF_WORKERS = 1
    groups_items_df = splitting(facebook_accounts_file, NUM_OF_WORKERS)

    # Creating threads
    for i in range(NUM_OF_WORKERS):

        # t = threading.Thread(target=Facebook("https://www.facebook.com/").countNFreindsWorker(accounts_file_path, groups_items_df[i][54:55]))
        # t = threading.Thread(target=Facebook("https://www.facebook.com/").checkAccountsWorker(accounts_file_path, groups_items_df[i][67:68]))
        t = threading.Thread(target=Facebook("https://www.facebook.com/").addLike_CommentOnPostWorker(accounts_file_path, groups_items_df[i][1:3], post_path))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

