from selenium import webdriver
from credentials import login, password
from pageobjects.campaigns_page import CampaignsPage
from pageobjects.main_page import MainPage
from pageobjects.new_campaign_page import NewCampaignPage


def setup_module():
    global driver
    global main_page
    global campaigns_page
    global new_campaign_page
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    main_page = MainPage(driver)
    campaigns_page = CampaignsPage(driver)
    new_campaign_page = NewCampaignPage(driver)


def test_create_campaign():
    driver.get('https://target-sandbox.my.com/')
    assert main_page.is_page_opened()
    main_page.wait_and_click('enter')
    main_page.wait_and_send_text('input login', login)
    main_page.wait_and_send_text('input password', password)
    main_page.wait_and_click('submit')
    assert campaigns_page.is_page_opened()
    campaigns_page.wait_and_click('new campaign')
    assert new_campaign_page.is_page_opened()
    new_campaign_page.wait_and_click('mobile')
    new_campaign_page.wait_and_send_text('input link', 'https://play.google.com/store/apps/details?id=ru.mail.mailapp')
    new_campaign_page.wait_and_click('mobile ads')
    new_campaign_page.wait_and_send_text('input title', 'Тестовая кампания')
    new_campaign_page.wait_and_click('open sex checkboxes')
    new_campaign_page.wait_and_click('uncheck female')
    new_campaign_page.wait_and_click('open devices checkboxes')
    new_campaign_page.wait_and_click('check apple')
    new_campaign_page.wait_and_click('open budget limit')
    new_campaign_page.wait_and_send_text('input budget limit per day', '1500')
    new_campaign_page.wait_and_click('open when show')
    new_campaign_page.wait_and_click('choose only working time')
    new_campaign_page.deselect_time_not_in_10to17()

