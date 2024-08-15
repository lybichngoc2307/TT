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

def login_tiktok(driver):
    username = "user6762240292153"
    password = "@K4ay%7H022X"
    try:
        username_field = driver.find_element(By.XPATH, env.login.username)
        username_field.send_keys(username)
        
        password_field = driver.find_element(By.XPATH, env.login.password)     
        password_field.send_keys(password)
        
        #login
        login_button = driver.find_element(By.XPATH, env.login.login_button ) #"//button[@type='submit']"
        login_button.click()
        time.sleep(10)
    except Exception as e:
        print(e)

def select_two_obj(browser):          
    try:
        image_captcha_element = browser.find_element(By.XPATH, env.captcha.captcha_image )
        captcha_src = image_captcha_element.get_attribute("src")
        folder_path = "./captcha_images"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        response = requests.get(captcha_src)
        image = Image.open(io.BytesIO(response.content))
        image.save(os.path.join(folder_path, "captcha_image.png"))
        image_path = os.path.join(folder_path, "captcha_image.png")
        # Đọc ảnh CAPTCHA và mã hóa base64
        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

        # Tạo yêu cầu POST để tạo job
        create_job_url = "https://omocaptcha.com/api/createJob"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "api_token": env.captcha.api,
            "data": {
                "type_job_id": "22",
                "image_base64": image_base64,
                "width_view": 340,
                "height_view": 212
            }
        }

        response = requests.post(create_job_url, headers=headers, json=data)
        result = response.json()

        if result['success']:
            job_id = result['job_id']
            print(f"Job created successfully with job_id: {job_id}")
        else:
            print("Failed to create job")

        # Gửi yêu cầu POST để nhận kết quả
        get_result_url = "https://omocaptcha.com/api/getJobResult"
        data = {
            "api_token": "apitoken8t6x9z5xxy6l8mysc0gqst6mutasthtpuw5q2i5nsy2yxmrnmjijmbl4rlnkg31722476177",
            "job_id": job_id
        }

        time.sleep(10) 

        response = requests.post(get_result_url, headers=headers, json=data)
        result = response.json()

        if result['success'] and result['status'] == 'success':
            coordinates = result['result']
            print(f"Coordinates received: {coordinates}")
        else:
            print("Failed to get result")


        image_captcha_element = browser.find_element(By.XPATH, env.captcha.captcha_image )

        # Giải mã tọa độ từ kết quả nhận được
        coords = coordinates.split('|')
        x1, y1, x2, y2 = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])
        print(f"Coordinates: ({x1}, {y1}), ({x2}, {y2})")

        # Chạy đoạn mã JavaScript để click vào tọa độ trên ảnh CAPTCHA
        simulate_click_script = f"""
        function simulateClick(element, offsetX, offsetY) {{
            var rect = element.getBoundingClientRect();
            var clientX = rect.left + offsetX;
            var clientY = rect.top + offsetY;
            var clickEvent = new MouseEvent('click', {{ bubbles: true, clientX: clientX, clientY: clientY }});
            element.dispatchEvent(clickEvent);
        }}

        var imageCaptcha = document.querySelector("#captcha-verify-image");
        simulateClick(imageCaptcha, {x1}, {y1});
        simulateClick(imageCaptcha, {x2}, {y2});
        """
        browser.execute_script(simulate_click_script)

        time.sleep(5)

        # Click nút submit CAPTCHA
        submit_button_script = """
        try {
            var submitButton = document.evaluate('//*[@id="captcha_container"]/div/div[3]/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            submitButton.click();
            return "Clicked submit button successfully";
        } catch (error) {
            return `Error clicking submit button: ${error}`;
        }
        """
        try:
            result = browser.execute_script(submit_button_script)
            print(result)
        except Exception as e:
            print(f"Error executing script for clicking submit button: {e}")


        time.sleep(15)
        post = "https://www.tiktok.com/@tamsucungnguoila788/video/7399509306426526977"
        browser.get(post)
    except:
        post = "https://www.tiktok.com/@tamsucungnguoila788/video/7399509306426526977"
        browser.get(post)
