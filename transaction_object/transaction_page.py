from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_login = (By.XPATH, "//button[@type='button']")
        self.username = (By.ID, "nomor-hp-atau-email")
        self.btn_next_login = (By.XPATH, "//button[normalize-space()='Log in']")
        self.close_pop_up = (By.XPATH, "//span[@role='button']")
        self.input_otp = (By.CSS_SELECTOR, "input[data-testid^='otp-input']")
        self.search = (By.XPATH, "//input[@placeholder='Cari di Tokopedia']")

    def click_close_pop_up(self):
        wait = WebDriverWait(self.driver, 10)
        close = wait.until(
            EC.visibility_of_element_located(self.close_pop_up)
        )
        close.click()

    def click_btn_login(self):
        self.driver.find_element(*self.btn_login).click()

    def fill_login(self, username):
        wait = WebDriverWait(self.driver, 10)
        input_login = wait.until(
            EC.visibility_of_element_located(self.username)
        )
        input_login.send_keys(username)
    
        self.driver.find_element(*self.btn_next_login).click()
    
    def fill_otp(self, otp_code):  
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.input_otp)
        )
        otp_fields = self.driver.find_elements(*self.input_otp)

        if len(otp_fields) != len(otp_code):
            print(f"❌ Jumlah field OTP ({len(otp_fields)}) tidak sesuai dengan panjang kode ({len(otp_code)})")
            return  

        for i, digit in enumerate(otp_code):
            otp_fields[i].click()
            otp_fields[i].clear()
            otp_fields[i].send_keys(digit)
            time.sleep(0.5)

    def fill_search(self, search):
        self.driver.find_element(*self.search).send_keys(search)
        