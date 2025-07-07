from selenium import webdriver
from transaction_object.transaction_page import TransactionPage
from selenium.webdriver.chrome.service import Service
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

    driver.get("https://www.tokopedia.com/")

    transaction_page = TransactionPage(driver)
    transaction_page.click_close_pop_up()
    transaction_page.click_btn_login()

    transaction_page.fill_login(config.PHONE_NUMBER)
    transaction_page.click_send_otp()
    #transaction_page.fill_login(config.PIN)

    transaction_page.fill_search(
        data['search']
    )
    driver.quit()