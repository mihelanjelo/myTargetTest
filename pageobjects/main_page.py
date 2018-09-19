from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATORS = {
        "enter": '//span[contains(text(), "Войти")]',
        "input login": '//input[@name="login"]',
        "input password": '//input[@name="password"]',
        "submit": '//button[@data-class-name="Submit"]',
    }