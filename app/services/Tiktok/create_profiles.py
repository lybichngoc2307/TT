from os import path
from time import sleep
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.options import Options
import random
from module_tool import get_folder_profile_path
import login
import reaction
from selenium.common.exceptions import WebDriverException
import time
import os
import threading
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
            login.login_tiktok(driver)            
            print("login done!")
            login.select_two_obj(driver)
            print("bypass done!")
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
            driver = Chrome(options=options, use_subprocess=True)
            driver.get("https://tiktok.com")
            driver.get("https://www.tiktok.com/@tamsucungnguoila788/video/7399509306426526977")
            print("opened!!!")
            return driver
             
        except WebDriverException as e:
            print(f"Error while opening Chrome: {e}")
        except Exception as e:
            print(f"lỗi: {e}")


def perform_like(driver):
    reaction.like(driver)

def perform_save(driver):
    reaction.save(driver)

def perform_share(driver):
    reaction.share(driver)

def perform_report(driver):
    reaction.report(driver)

def perform_comment(driver,cmt):
    reaction.comment(driver,cmt)

def perform_exit(driver):
    driver.quit()

''' def perform_action(drivers):
    while True:  
        choice = int(input("1: Like\n2: Save\n3: Comment\n4: Share\n5: Report\n6: Exit\n==>>"))

        if choice == 1:
            threads = []
            for driver in drivers:
                thread = threading.Thread(target=perform_like, args=(driver,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()  # Đảm bảo tất cả các luồng đã hoàn thành
        elif choice == 2:
            threads = []
            for driver in drivers:
                thread = threading.Thread(target=perform_save, args=(driver,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()  # Đảm bảo tất cả các luồng đã hoàn thành
        elif choice == 3:
            cmt = input("Enter your comment text: ")
            threads = []
            for driver in drivers:
                thread = threading.Thread(target=perform_comment, args=(driver,cmt,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()  # Đảm bảo tất cả các luồng đã hoàn thành
        elif choice == 4:
            threads = []
            for driver in drivers:
                thread = threading.Thread(target=perform_share, args=(driver,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()  # Đảm bảo tất cả các luồng đã hoàn thành
        elif choice == 5:
            threads = []
            for driver in drivers:
                thread = threading.Thread(target=perform_report, args=(driver,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()  # Đảm bảo tất cả các luồng đã hoàn thành
        elif choice == 6:
            print("Exiting...")
            for driver in drivers:
                driver.quit()  # Đóng tất cả các trình duyệt
            break  # Thoát khỏi vòng lặp
        else:
            print("Invalid choice. Please choose again.")
'''

def perform_action(drivers, actions):
    threads = []
    drivers_to_remove = []

    for driver, action in zip(drivers, actions):
        if action == 'like':
            thread = threading.Thread(target=perform_like, args=(driver,))
        elif action == 'save':
            thread = threading.Thread(target=perform_save, args=(driver,))
        elif action == 'comment':
            cmt = input(f"Enter your comment text for profile {drivers.index(driver)+1}: ")
            thread = threading.Thread(target=perform_comment, args=(driver, cmt,))
        elif action == 'share':
            thread = threading.Thread(target=perform_share, args=(driver,))
        elif action == 'report':
            thread = threading.Thread(target=perform_report, args=(driver,))
        elif action == 'exit':
                thread = threading.Thread(target=perform_exit, args=(driver,))
                drivers_to_remove.append(driver)
        else:
            print(f"Invalid action for profile {drivers.index(driver)+1}.")
            continue

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()  # Đảm bảo tất cả các luồng đã hoàn thành

    # Loại bỏ các profile đã chọn "exit"
    for driver in drivers_to_remove:
        drivers.remove(driver)

    if not drivers:  # Nếu tất cả các profile đã được đóng, thoát khỏi vòng lặp
        print("All profiles have been closed.")
