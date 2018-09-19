from .base_page import BasePage
from selenium.webdriver.common.by import By


class NewCampaignPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATORS = {
        'mobile': '//div[@data-value="mobile"]',
        'input link': '//input[@placeholder="Введите ссылку на мобильное приложение"]',
        'mobile ads': '//div[@data-name="tt_mobile_app_multiformat_all_android_ocpm_production"]',
        'input title': '//input[@data-gtm-id="banner_form_title"]',
        'open sex checkboxes': '//div[.//span[text()="Пол:"]]',
        'uncheck female': '//input[@targeting="sex-F"]',
        'open devices checkboxes': '//div[.//span[text()="Мобильные устройства:"]]',
        'check apple': '//li[.//label[@title="Apple"]]/input',
        'open budget limit': '//div[.//span[text()="Ограничение бюджета:"]]',
        'input budget limit per day': '//input[@targeting="budget-per_day"]',
        'open when show': '//div[.//span[text()="Время и дни показа:"]]',
        'choose only working time': '//li[@data-name="workTime"]',
    }

    def deselect_time_not_in_10to17(self):
        elements = self.driver.find_elements(By.XPATH, '//li[@data-id="9"]')\
                   + self.driver.find_elements(By.XPATH, '//li[@data-id="18"]')\
                   + self.driver.find_elements(By.XPATH, '//li[@data-id="19"]')
        for element in elements:
            element.click()
