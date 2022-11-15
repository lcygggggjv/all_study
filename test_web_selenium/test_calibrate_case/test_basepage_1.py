import time

from selenium.webdriver.common.by import By

from test_web_selenium.common.basepage import BasePage
from test_web_selenium.config.config import config


def test_01_basepage(browser):

    page=BasePage(browser)  #初始化，传入browser

    page.get_url("http://teamsit.teletraan.io")

    tentcode = (By.NAME, 'tenantCode')
    account = (By.NAME, 'account')
    password = (By.NAME, 'password')
    submit=(By.XPATH, "//button[@type='submit']")
    eamicon = (By.XPATH, '//div[@class="css-q37yd2"]//img')

    page.get_element(tentcode).send_keys(config.tenantCode)
    page.get_element(account).send_keys(config.account)
    page.get_element(password).send_keys(config.password)
    page.get_element(submit).click()
    page.get_element(eamicon).click()

    time.sleep(2)
