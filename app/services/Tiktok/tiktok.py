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

#undetected_chromedriver
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# # Thay đổi User-Agent 
# chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

username = "user6762240292153"
password = "@K4ay%7H022X"

browser = uc.Chrome(options=chrome_options)
browser.get('https://www.tiktok.com/login/phone-or-email/email')
time.sleep(5)

#us-pwd
username_field = browser.find_element(By.NAME, "username")
username_field.send_keys(username)
password_field = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]')
password_field.send_keys(password)

#login
login_button = browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
login_button.click()
time.sleep(10)

#Bypass captcha
try:

    image_captcha_element = browser.find_element(By.CSS_SELECTOR, "#captcha-verify-image")
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
        "api_token": "apitoken8t6x9z5xxy6l8mysc0gqst6mutasthtpuw5q2i5nsy2yxmrnmjijmbl4rlnkg31722476177",
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



    from selenium.webdriver.common.action_chains import ActionChains

    image_captcha_element = browser.find_element(By.XPATH, '//*[@id="captcha-verify-image"]')

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


#AUTO LIKE
time.sleep(10)
like_button = browser.find_element(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[1]')
browser.execute_script("window.scrollTo(0, 0);")
time.sleep(10)
like_button.click()
print("like, done!")
time.sleep(5)

#AUTO CMT
comment_text = browser.find_element(By.XPATH, '//div[@class="notranslate public-DraftEditor-content" and @contenteditable="true"]')
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.execute_script("arguments[0].scrollIntoView(false);", comment_text)
time.sleep(10)
#nội dung comment
comment_text.send_keys("hello")
#post
post_button = browser.find_element(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div/div[3]/div[1]/div/div/div[2]')
post_button.click()
print("cmt done!")
#AUTO SAVE
save_button = browser.find_element(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[3]')
#browser.execute_script("arguments[0].scrollIntoView(true);", luu_button)
browser.execute_script("window.scrollTo(0, 0);")
time.sleep(10)
save_button.click()
print("save, done!")

#AUTO SHARE
wait = WebDriverWait(browser, 10)
share_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/button[4]')))
# Di chuyển chuột 
actions = ActionChains(browser)
actions.move_to_element(share_button).perform()
time.sleep(5)
repost_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Repost")]')))
#REPOST - ĐĂNG LẠI 
repost_option.click()
print("share, done")

#AUTO REPORT
wait = WebDriverWait(browser, 10)
report_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[7]')))
# Di chuột đến
actions = ActionChains(browser)
time.sleep(10) 
actions.move_to_element(report_button).perform()
time.sleep(10) 
report_option = browser.find_element(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div/div[1]/div[1]/div[4]/div[2]/div[2]/div[7]/div/ul/li[1]')
report_option.click()
time.sleep(5) 
#rs1
rs = browser.find_element(By.XPATH, '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/label[1]')
rs.click()
time.sleep(10)
#rs2
rs_ = browser.find_element(By.XPATH, '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/label[1]')
rs_.click()
#SUBMIT
time.sleep(5)
submit = browser.find_element(By.XPATH, '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/div[3]/button')
submit.click()
time.sleep(5)
print("successfully!!!")


