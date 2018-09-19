import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from exceptions.element_blocked_but_clickable import ElementBlockedButClickableException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    TITLE = 'BASE PAGE'

    LOCATORS = {}

    def wait_and_click(self, locator_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOCATORS[locator_name])))
        for i in range(5):
            try:
                element.click()
                break
            except WebDriverException:
                if i == 4:
                    raise ElementBlockedButClickableException
                else:
                    time.sleep(1)

    def wait_and_send_text(self, locator_name, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOCATORS[locator_name])))
        for i in range(5):
            try:
                element.clear()
                element.send_keys(text)
                break
            except WebDriverException:
                if i == 4:
                    raise ElementBlockedButClickableException
                else:
                    time.sleep(1)

    def is_page_opened(self):
        for i in range(11):
            if self.driver.title == self.TITLE:
                return True
            time.sleep(1)
        return False
