import time

from test_web_selenium.page.login_page import login_page
from test_web_selenium.common.basepage import BasePage
from test_web_selenium.config.config import config
from selenium import webdriver

def test_001(browser):
    """新增成功"""

    category=BasePage(browser)
    category.login_thingList()

    category.get_element(('xpath','//p[text()="基础配置"]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//button[text()="确定"]')).click()
    category.show_wait_element(browser,('xpath', '//div[text()="新增成功"]'))
    actual=category.get_element(('xpath', '//div[text()="新增成功"]')).text
    expected='新增成功'

    assert expected == actual
    time.sleep(2)

def test_002(browser):
    """新增必填"""
    category=BasePage(browser)
    category.login_thingList()

    category.get_element(('xpath','//p[text()="基础配置"]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys('')
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//button[text()="确定"]')).click()
    category.show_wait_element(browser,('xpath', '//p[text()="请输入该必填项"]'))
    actual=category.get_element(('xpath', '//p[text()="请输入该必填项"]')).text
    expected='请输入该必填项'

    assert expected == actual
    time.sleep(2)


def test_003(browser):

    """编码规范汉字"""
    category=BasePage(browser)
    category.login_thingList()

    category.get_element(('xpath','//p[text()="基础配置"]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_china())
    category.get_element(('xpath', '//button[text()="确定"]')).click()
    category.show_wait_element(browser,('xpath', '//p[text()="请输入由大小写英文字母、数字、及特殊符号组成的字符串(特殊符号包括 - ~ · / \ | _ ),比如:Abc123、A-123"]'))
    actual=category.get_element(('xpath', '//p[text()="请输入由大小写英文字母、数字、及特殊符号组成的字符串(特殊符号包括 - ~ · / \ | _ ),比如:Abc123、A-123"]')).text
    expected='请输入由大小写英文字母、数字、及特殊符号组成的字符串(特殊符号包括 - ~ · / \ | _ ),比如:Abc123、A-123'

    assert expected == actual
    time.sleep(2)


def test_004(browser):
    """编辑成功"""

    category=BasePage(browser)
    category.login_thingList()

    category.get_element(('xpath','//p[text()="基础配置"]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath', '//p[text()="22222"]')).click()
    category.get_element(('xpath','//span[@aria-label="修改类别名称"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).clear()
    category.get_element(('xpath', '//input[@name="code"]')).clear()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//button[text()="确定"]')).click()
    category.show_wait_element(browser,('xpath', '//div[text()="编辑成功"]'))
    actual=category.get_element(('xpath', '//div[text()="编辑成功"]')).text
    expected='编辑成功'

    assert expected == actual
    time.sleep(2)

def test_005(browser):
    """编辑必填"""
    category=BasePage(browser)
    category.login_thingList()

    category.get_element(('xpath','//p[text()="基础配置"]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath', '//p[text()="2323"]')).click()
    category.get_element(('xpath','(//span[@aria-label="修改类别名称"]//*[name()="svg"])[2]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).clear()
    category.get_element(('xpath', '//input[@name="code"]')).clear()
    category.get_element(('xpath', '//button[text()="确定"]')).click()
    category.show_wait_element(browser,('xpath', '//p[text()="请输入该必填项"]'))
    actual=category.get_element(('xpath', '//p[text()="请输入该必填项"]')).text
    expected='请输入该必填项'

    assert expected == actual
    time.sleep(2)

def test_006(browser):
    """删除"""
    category=BasePage(browser)
    category.login_thingList()

    category.get_element(('xpath','//p[text()="基础配置"]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath', '//p[text()="122"]')).click()
    category.get_element(('xpath','(//button[@aria-label="删除该类别"]//*[name()="svg"])[2]')).click()
    category.get_element(('xpath', '//button[text()="删除"]')).click()
    category.show_wait_element(browser,('xpath', '//div[text()="删除成功"]'))
    actual=category.get_element(('xpath', '//div[text()="删除成功"]')).text
    expected='删除成功'

    assert expected == actual
    time.sleep(2)


def test_007(browser):
    """替换表单"""
    category=BasePage(browser)
    category.login_thingList()

    category.get_element(('xpath','//p[text()="基础配置"]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath', '//p[text()="token"]')).click()
    category.get_element(('xpath','//button[text()="替换关联表单"]')).click()
    category.get_element(('xpath', '//div[@name="form"]//*[name()="svg"][@data-testid="ArrowDropDownIcon"]')).click()
    category.get_element(('xpath', '//li[text()="默认表单"]')).click()
    category.get_element(('xpath', '//button[text()="确定"]')).click()
    category.show_wait_element(browser,('xpath', '//div[text()="替换成功"]'))
    actual=category.get_element(('xpath', '//div[text()="替换成功"]')).text
    expected='替换成功'

    assert expected == actual
    time.sleep(2)
