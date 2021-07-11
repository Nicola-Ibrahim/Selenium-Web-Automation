from ..WebAutomation import splitting
import pandas as pd
from instagram import Instagram
import threading

def instagramMain():
    # Read accounts file
    accounts_file_path = "../Accounts/Instagram Accounts.xlsx"
    facebook_accounts_file = pd.read_excel(accounts_file_path, usecols=['Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name'])


    profile_path = """any profile path"""
    post_path = """https://www.facebook.com/MaakALBOT/posts/2825667517695375?__cft__[0]=AZV38cHmA9DsKX6BkuKqCm_QYT-q1eprjOJoNDNSIGb6mEVob8_KUcMR2scnVEN5sREtewf2G3DtqXqnid8p7mtBj-79ZzekTNtxX9_GGApwD748IpygFAx_uiILgxSqHrj_MiJW4w0en5SBgP1H8JZV&__tn__=%2CO%2CP-R"""
    page_path = """any page path"""


    # Number of threads to be run
    threads = []
    NUM_OF_WORKERS = 1
    groups_items_df = splitting(facebook_accounts_file, NUM_OF_WORKERS)

    # Creating threads
    for i in range(NUM_OF_WORKERS):

        # t = threading.Thread(target=Facebook("https://www.facebook.com/").countNFreindsWorker(accounts_file_path, groups_items_df[i][54:55]))
        # t = threading.Thread(target=Facebook("https://www.facebook.com/").checkAccountsWorker(accounts_file_path, groups_items_df[i][67:68]))
        t = threading.Thread(target=Instagram("https://www.facebook.com/").addLikeOnPostWorker(groups_items_df[i][11:20], post_path))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

