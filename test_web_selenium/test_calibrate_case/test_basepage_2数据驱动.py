import time

import pytest
from selenium.webdriver.common.by import By

from test_web_selenium.common.basepage import BasePage
from test_web_selenium.config.config import config


items=[
    {"tentcode":"","account":"eam111","passwd":"teletraan","expected":"请填写该必填项"},
    {"tentcode":"error_tentcode","account":"eam111","passwd":"teletraan","expected":"企业标识符错误，请重新填写"},
    {"tentcode":"cr7","account":"error_acount","passwd":"teletraan","expected":"用户不存在"},
    {"tentcode":"cr7","account":"eam111","passwd":"error_pwd","expected":"密码错误，请重新输入"}
]
#pytest的数据驱动
@pytest.mark.parametrize('item',items)
def test_01_basepage(browser,item):

    page=BasePage(browser)  #初始化，传入browser

    page.get_url("http://teamsit.teletraan.io")

    tentcode = (By.NAME, 'tenantCode')
    account = (By.NAME, 'account')
    password = (By.NAME, 'password')
    submit=(By.XPATH, "//button[@type='submit']")
    # eamicon = (By.XPATH, '//div[@class="css-q37yd2"]//img')

    page.get_element(tentcode).send_keys(item['tentcode'])
    page.get_element(account).send_keys(item['account'])
    page.get_element(password).send_keys(item['passwd'])
    page.get_element(submit).click()
    locator=('xpath','(//p[text()="请填写该必填项"])[1]')
    page.show_wait_element(browser, locator)
    actual=page.get_element(locator).text
    expecetd=item['expected']

    assert expecetd == actual

    time.sleep(2)


def test_02_basepage(browser):

    page=BasePage(browser)  #初始化，传入browser

    page.get_url("http://teamsit.teletraan.io")

    tentcode = (By.NAME, 'tenantCode')
    account = (By.NAME, 'account')
    password = (By.NAME, 'password')
    submit=(By.XPATH, "//button[@type='submit']")
    # eamicon = (By.XPATH, '//div[@class="css-q37yd2"]//img')

    page.get_element(tentcode).send_keys('error_tentcode')
    page.get_element(account).send_keys(config.account)
    page.get_element(password).send_keys(config.password)
    page.get_element(submit).click()
    locator=('xpath','//div[text()="企业标识符错误，请重新填写"]')
    page.show_wait_element(browser, locator)
    actual=page.get_element(locator).text
    expecetd='企业标识符错误，请重新填写'

    assert expecetd == actual

    time.sleep(2)


def test_03_basepage(browser):

    page=BasePage(browser)  #初始化，传入browser

    page.get_url("http://teamsit.teletraan.io")

    tentcode = (By.NAME, 'tenantCode')
    account = (By.NAME, 'account')
    password = (By.NAME, 'password')
    submit=(By.XPATH, "//button[@type='submit']")
    # eamicon = (By.XPATH, '//div[@class="css-q37yd2"]//img')

    page.get_element(tentcode).send_keys(config.tenantCode)
    page.get_element(account).send_keys('error_acount')
    page.get_element(password).send_keys(config.password)
    page.get_element(submit).click()
    locator=('xpath','//div[text()="用户不存在"]')
    page.show_wait_element(browser,locator)

    actual=page.get_element(locator).text
    expecetd='用户不存在'

    assert expecetd == actual

    time.sleep(2)

def test_05_basepage(browser):

    page=BasePage(browser)  #初始化，传入browser

    page.get_url("http://teamsit.teletraan.io")

    tentcode = (By.NAME, 'tenantCode')
    account = (By.NAME, 'account')
    password = (By.NAME, 'password')
    submit=(By.XPATH, "//button[@type='submit']")
    # eamicon = (By.XPATH, '//div[@class="css-q37yd2"]//img')

    page.get_element(tentcode).send_keys(config.tenantCode)
    page.get_element(account).send_keys(config.account)
    page.get_element(password).send_keys('error_pwd')
    page.get_element(submit).click()
    locator=('xpath','//div[text()="密码错误，请重新输入"]')
    page.show_wait_element(browser,locator)

    actual=page.get_element(locator).text
    expecetd='密码错误，请重新输入'

    assert expecetd == actual

    time.sleep(2)