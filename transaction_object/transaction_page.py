from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_login = (By.XPATH, "//button[normalize-space()='Masuk']")
        self.username = (By.ID, "email-phone")
        self.btn_next_login = (By.XPATH, "//button[@type='submit']")
        self.send_otp = (By.XPATH, "//div[@aria-label='sms']")
        self.search = (By.XPATH, "//input[@placeholder='Cari di Tokopedia']")

    def click_close_pop_up(self):
        x_offset = 50
        y_offset = 50

        actions = ActionChains(self.driver)
        actions.move_by_offset(x_offset, y_offset).click().perform()
        actions.move_by_offset(-x_offset, -y_offset).perform()

    def click_btn_login(self):
        self.driver.find_element(*self.btn_login).click()

    def fill_login(self, username):
        wait = WebDriverWait(self.driver, 10)
        input_login = wait.until(
            EC.visibility_of_element_located(self.username)
        )
        input_login.send_keys(username)
    
        self.driver.find_element(*self.btn_next_login).click()

    def click_send_otp(self):
        wait = WebDriverWait(self.driver, 10)
        click_otp = wait.until(EC.element_to_be_clickable(self.send_otp))
        click_otp.click()

    def fill_search(self, search):
        self.driver.find_element(*self.search).send_keys(search)
        