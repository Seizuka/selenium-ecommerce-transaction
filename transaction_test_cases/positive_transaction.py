from selenium import webdriver
from transaction_object.transaction_page import TransactionPage
from selenium.webdriver.chrome.service import Service
from utils.gmail_utils import get_otp_from_gmail_imap
import time
import json
import config
import undetected_chromedriver as uc



def run():
    with open('data/transaction_data.json', 'r') as f:
        data = json.load(f)

    service = Service(executable_path="chromedriver.exe")
    driver = uc.Chrome(service=service)
    driver.maximize_window()

    driver.get("https://www.blibli.com/")

    transaction_page = TransactionPage(driver)
    transaction_page.click_btn_login()

    transaction_page.fill_login(config.EMAIL)
    transaction_page.click_close_pop_up()
    time.sleep(3)

    otp_code = get_otp_from_gmail_imap(config.EMAIL, config.APP_PASSWORD)
    print("OTP Retrieved:", otp_code)

    if otp_code:
        transaction_page.fill_otp(otp_code)
        # transaction_page.fill_search(data['search'])
    else:
        print("OTP not found.")
    
    time.sleep(10)
    driver.quit()