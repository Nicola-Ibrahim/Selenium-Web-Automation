from Automator.Facebook.facebook import Facebook
from Automator.WebAutomation import splitting
import pandas as pd
import threading

def facebookMain():
        
    # Read accounts file
    accounts_file_path = "Automator/Facebook/Facebook Accounts.xlsx"
    accounts_data = pd.read_excel(accounts_file_path, usecols=['Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name', 'group'])


    profile_path = """any profile path"""
    post_path = """any profile path"""
    page_path = """any page path"""


    # Number of threads to be run
    threads = []
    NUM_OF_WORKERS = 1
    groups_items_df = splitting(accounts_data, NUM_OF_WORKERS)

    # Creating threads
    for i in range(NUM_OF_WORKERS):

        t = threading.Thread(target=Facebook(accounts_file_path, groups_items_df[i]).addLike_CommentOnPostWorker(post_path))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()


