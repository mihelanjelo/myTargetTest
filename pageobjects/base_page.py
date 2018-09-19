import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    LOCATORS = {}

    def wait_and_click(self, locator_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOCATORS[locator_name])))
        time.sleep(2)
        element.click()

    def wait_and_send_text(self, locator_name, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOCATORS[locator_name])))
        time.sleep(2)
        element.clear()
        element.send_keys(text)