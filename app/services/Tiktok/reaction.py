from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import env


def like(browser):
    try:
        time.sleep(10)
        like_button = browser.find_element(By.XPATH, env.auto.like)
        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(10)
        like_button.click()
        print("Like done!")
        time.sleep(5)
    except NoSuchElementException:
        print("Like button not found.")
    except Exception as e:
        print(f"An error occurred in like: {e}")

def comment(browser, cmt):
    try:
        comment_text = browser.find_element(By.XPATH, env.auto.cmt_text)
        browser.execute_script("arguments[0].scrollIntoView(false);", comment_text)
        time.sleep(10)
        comment_text.send_keys(cmt)
        print("sent!!!")
        post_button = browser.find_element(By.XPATH, env.auto.cmt_post)
        print("post")
        post_button.click()
        print("Comment done!")
    # except NoSuchElementException:
    #     print("Comment field or post button not found.")
    except Exception as e:
        print(f"An error occurred in comment: {e}")

def save(browser):
    try:
        browser.execute_script("window.scrollTo(0, 0);")
        save_button = browser.find_element(By.XPATH, env.auto.save)
        time.sleep(10)
        
        if save_button:
            save_button.click()
            time.sleep(2)
            print("Save done!")
        else:
            print("Save button not found.")
    
    except Exception as e:
        print(f"An error occurred in save: {e}")

def share(browser):
    try:
        wait = WebDriverWait(browser, 10)
        share_button = wait.until(EC.presence_of_element_located((By.XPATH, env.auto.share)))
        actions = ActionChains(browser)
        actions.move_to_element(share_button).perform()
        time.sleep(5)
        
        repost_option = wait.until(EC.element_to_be_clickable((By.XPATH, env.auto.repost)))
        repost_option.click()
        print("Share done!")
    
    except Exception as e:
        print(f"An error occurred in share: {e}")

def report(browser):
    try:
        wait = WebDriverWait(browser, 10)
        report_button = wait.until(EC.presence_of_element_located((By.XPATH, env.auto.report_ops)))
        actions = ActionChains(browser)
        time.sleep(10) 
        actions.move_to_element(report_button).perform()
        time.sleep(10)
        
        report_option = browser.find_element(By.XPATH, env.auto.report)
        report_option.click()
        time.sleep(5)
        
        reason1 = browser.find_element(By.XPATH, env.auto.reason1)
        reason1.click()
        time.sleep(5)
        
        reason2 = browser.find_element(By.XPATH, env.auto.reason2)
        reason2.click()
        time.sleep(5)
        
        submit_button = browser.find_element(By.XPATH, env.auto.submit_report)
        submit_button.click()
        time.sleep(5)
        print("Report submitted successfully!")
    
    except Exception as e:
        print(f"An error occurred in report: {e}")