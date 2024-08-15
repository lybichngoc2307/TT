from os import path
from time import sleep
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.options import Options
import random
from module_tool import get_folder_profile_path
import login
import reaction
#import main
def random_user_agent():
    us_agent_file = "./user-agents.txt"
    with open(us_agent_file, 'r') as f:
        user_agents = f.readlines()
        random_us = random.choice(user_agents).strip()
    return random_us

def create_profile(profile_name):
    profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    if path.exists(profile_path):
        print(f"Profile {profile_name} Exist !")
        sleep(3)
    else:
        us_agent = random_user_agent()
        proxy = ''
        #print(us_agent)
        options = Options()
        options.add_argument(f"--user-data-dir={profile_path}")
        options.add_argument(f"--user-agent={us_agent}")
        options.add_argument(f'--proxy-server={proxy}')
        try:
            driver = Chrome(options=options ,use_subprocess=True)
            print("created!")
            driver.get("https://www.tiktok.com/login/phone-or-email/email")
            #driver.quit()
            # login.login_tiktok(driver)            
            # print("login done!")
            # login.select_two_obj(driver)
            # print("bypass done!")
        except:
            if not path.exists(profile_path):
                print(f"Create Profile Fail: {profile_name}")


def manager_profiles(profile_name): 
    profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    # profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    if path.exists(profile_path):
        options = Options()
        options.add_argument(f"--user-data-dir={profile_path}")
        try:
            driver = Chrome(options=options ,use_subprocess=True)
            driver.get("https://tiktok.com")
        except:
            pass

