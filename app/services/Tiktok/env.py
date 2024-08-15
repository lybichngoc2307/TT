class login:
    login_button = '//*[@id="loginContainer"]/div[1]/form/button'
    #password = 'input[placeholder="Password"]'
    username = '//*[@id="loginContainer"]/div[1]/form/div[1]/input'
    password = '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input'
class captcha:
    captcha_image =  '//*[@id="captcha-verify-image"]' #"#captcha-verify-image"
    api = "apitoken8t6x9z5xxy6l8mysc0gqst6mutasthtpuw5q2i5nsy2yxmrnmjijmbl4rlnkg31722476177"
    drag_captcha = '//div[contains(text(),"Drag the slider to fit the puzzle")]'
    select_2obj = 'Select 2 objects that are the same shape:'
    #<div class="VerifyBar___StyledDiv-sc-12zaxoy-0 hRJhHT">Select 2 objects that are the same shape:</div>
class auto:
    like = '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[1]'
    
    cmt_text = '//div[@class="notranslate public-DraftEditor-content" and @contenteditable="true"]'
    cmt_post = '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]'
    #//*[@id="main-content-video_detail"]/div/div[2]/div/div[3]/div[1]/div/div/div[2]'
                
    save = '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[3]'

    share = '//*[@id="main-content-video_detail"]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/button[4]'
    repost = '//span[contains(text(),"Repost")]'

    report_ops = '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[7]'
    report = '//*[@id="main-content-video_detail"]/div/div[2]/div/div[1]/div[1]/div[4]/div[2]/div[2]/div[7]/div/ul/li[1]'
    reason1 = '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/label[1]'
    reason2 = '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/label[1]'
    submit_report = '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/div[3]/button'

