import pytest
from selenium import webdriver
from credentials import login, password
from pageobjects.campaigns_page import CampaignsPage
from pageobjects.main_page import MainPage
from pageobjects.new_campaign_page import NewCampaignPage


def on(page_name):
    return {'main_page': MainPage,
            'campaigns_page': CampaignsPage,
            'new_campaign_page': NewCampaignPage
            }[page_name](pytest.driver)


def setup_module():
    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(3)


def test_create_campaign():
    pytest.driver.get('https://target-sandbox.my.com/')
    assert on('main_page').is_page_opened()
    on('main_page').wait_and_click('enter')
    on('main_page').wait_and_send_text('input login', login)
    on('main_page').wait_and_send_text('input password', password)
    on('main_page').wait_and_click('submit')
    assert on('campaigns_page').is_page_opened()
    on('campaigns_page').wait_and_click('new campaign')
    assert on('new_campaign_page').is_page_opened()
    on('new_campaign_page').wait_and_click('mobile')
    on('new_campaign_page').wait_and_send_text('input link', 'https://play.google.com/store/apps/details?id=ru.mail.mailapp')
    on('new_campaign_page').wait_and_click('mobile ads')
    on('new_campaign_page').wait_and_send_text('input title', 'Тестовая кампания')
    on('new_campaign_page').wait_and_click('open sex checkboxes')
    on('new_campaign_page').wait_and_click('uncheck female')
    on('new_campaign_page').wait_and_click('open devices checkboxes')
    on('new_campaign_page').wait_and_click('check apple')
    on('new_campaign_page').wait_and_click('open budget limit')
    on('new_campaign_page').wait_and_send_text('input budget limit per day', '1500')
    on('new_campaign_page').wait_and_click('open when show')
    on('new_campaign_page').wait_and_click('choose only working time')
    on('new_campaign_page').deselect_time_not_in_10to17()



