from .base_page import BasePage


class CampaignsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATORS = {
        'new campaign': '//a[@href="/campaigns/new"]'
    }