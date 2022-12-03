import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
print(EMAIL)

# Using this to check if its the first time of the day or not
# Default initiated with True.
# f = open("status_storage.txt", "r")
# status = f.read()

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"/chromedriver"
print(chrome_driver)

def keka_login():
    global f
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    print('Login Process Started: ')
    browser.get("https://lcx.keka.com/#/home")
    print('Website Opened')

    time.sleep(5)

    email = browser.find_element('id', "email")
    email.send_keys(EMAIL)
    print('Email Entered')


    password = browser.find_element('id', "password")
    password.send_keys(PASSWORD)
    print('Password Entered')


    time.sleep(5)

    login_button = browser.find_element('xpath', '//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button[1]')
    login_button.click()
    print('Login Button Clicked')


    time.sleep(15)

    web_clockin_button = browser.find_element('xpath', '/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/div/div[2]/div/div[5]/div[6]/home-attendance-clockin-widget/div/div[1]/div/div[2]/div/div[2]/div[1]/button')
    web_clockin_button.click()
    print('Clicked WebClock In')


    time.sleep(5)


    location_request_button = browser.find_element('xpath', '/html/body/modal-container/div/div/xhr-confirm-dialog/div[3]/button[1]')
    location_request_button.click()
    print('Location Request Declined')


    # if status == 'True':
    #     note_text_area = browser.find_element('xpath', '//*[@id="ng-app"]/body/div[1]/div/div/div[2]/form/div[1]/div/textarea')
    #     note_text_area.send_keys("Starting now")
    #     print('Entered Description')


    #     time.sleep(5)

    #     request_button = browser.find_element('xpath','//*[@id="ng-app"]/body/div[1]/div/div/div[2]/form/div[2]/div/div/input[1]')
    #     request_button.click()
    #     print('Clicked Request Button')


    time.sleep(5)
    print('Successfully logged in')
    # f.close()
    # f = open("status_storage.txt", "w")
    # f.write("False")
    # f.close()
    print(time.strftime("Cron Successfully ran last at: " + "%Y-%m-%d %H:%M"))
    browser.quit()

keka_login()
