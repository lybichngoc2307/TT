from selenium.webdriver.chrome.options import Options
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from PIL import Image
import requests
import base64
import io
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import env
import create_profiles 


def login_tiktok(driver):
    username = "user6762240292153"
    password = "@K4ay%7H022X"
    try:
        username_field = driver.find_element(By.XPATH, env.login.username)
        username_field.send_keys(username)
        
        password_field = driver.find_element(By.XPATH, env.login.password)
       
        password_field.send_keys(password)
        
        #login
        login_button = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button' ) #"//button[@type='submit']"
        login_button.click()
        time.sleep(10)
    except Exception as e:
        print(e)