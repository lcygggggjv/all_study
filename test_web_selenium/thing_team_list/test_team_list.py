import time

from selenium import webdriver
from test_web_selenium.common.basepage import BasePage



def test_01(browser):
    """新增班组"""
    team=BasePage(browser)
    team.team_login()
        #locator=('xpath','//button[text()="新增班组"]')
    team.get_element(('xpath','//button[text()="新增班组"]')).click()
    team.get_element(('xpath','//input[@name="name"]')).send_keys(team.fk_word())
    team.get_element(('xpath', '//div[@name="leader"]//input[@autocomplete="off"]')).click()
            #这里是输入下拉框形式，暂选择点击下拉选项，
    team.get_element(('xpath','//p[text()="12312/普通1"]')).click()
    team.get_element(('xpath','//div[@name="member"]//input[@autocomplete="off"]')).click()
    team.get_element(('xpath','//p[text()="eam110/企管"]')).click()
    team.get_element(('xpath','//div[text()="新增班组"]')).click()
    team.get_element(('xpath','//button[text()="确定"]')).click()

    actual=team.get_element(('xpath','//div[text()="新增成功"]')).text
    expected='新增成功'

    assert expected == actual
    time.sleep(1)


def test_02(browser):
    """新增必填"""
    team=BasePage(browser)
    team.team_login()

    team.get_element(('xpath','//button[text()="新增班组"]')).click()
    team.get_element(('xpath','//button[text()="确定"]')).click()

    actual=team.get_element(('xpath','//p[text()="请输入该必填项"]')).text
    expected='请输入该必填项'

    assert expected == actual
    time.sleep(1)


def test_03(browser):
    """新增唯一"""
    team=BasePage(browser)
    team.team_login()

    team.get_element(('xpath','//button[text()="新增班组"]')).click()
    team.get_element(('xpath', '//input[@name="name"]')).send_keys('1133')
    team.get_element(('xpath','//button[text()="确定"]')).click()

    actual=team.get_element(('xpath','//p[text()="该班组名称已存在，请重新输入"]')).text
    expected='该班组名称已存在，请重新输入'

    assert expected == actual
    time.sleep(1)


def test_05(browser):
    """编辑"""
    team=BasePage(browser)
    team.team_login()

    team.get_element(('xpath','(//span[@aria-label="编辑"]//*[name()="svg"])[1]')).click()
    team.get_element(('xpath', '//input[@name="name"]')).clear()
    team.move_to(('xpath','(//div[@name="leader"]//*[name()="svg"])[1]'))
    team.get_element(('xpath', '(//div[@name="leader"]//*[name()="svg"])[1]')).click()
    team.move_to(('xpath', '(//div[@name="member"]//*[name()="svg"])[2]'))
    team.get_element(('xpath','(//div[@name="member"]//*[name()="svg"])[2]')).click()
    team.get_element(('xpath', '//input[@name="name"]')).send_keys(team.fk_word())
    team.get_element(('xpath', '//div[@name="leader"]//input[@autocomplete="off"]')).click()
    team.get_element(('xpath', '//p[text()="213/普通5"]')).click()
    team.get_element(('xpath', '//div[@name="member"]//input[@autocomplete="off"]')).click()
    team.get_element(('xpath', '//p[text()="12253421/普通6"]')).click()
    team.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=team.get_element(('xpath','//div[text()="编辑成功"]')).text
    expected='编辑成功'

    assert expected == actual
    time.sleep(2)