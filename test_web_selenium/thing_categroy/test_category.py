import time

from test_web_selenium.page.login_page import login_page
from test_web_selenium.common.basepage import BasePage
from test_web_selenium.config.config import config
from selenium import webdriver


def test_001(browser):
    """新增成功"""

    category=BasePage(browser)
    category.category_login()   #类别登录到新增页面

    # category.get_element(('xpath','//p[text()="基础配置"]')).click()
    # category.get_element(('xpath','(//p[text()="资产类别"])[1]')).click()
    # category.get_element(('xpath','(//p[text()="资产类别"])[2]')).click()
    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//div[text()="新增成功"]')).text   #在断言里家里显性等待
    expected='新增成功'

    assert expected == actual
    time.sleep(2)

def test_002(browser):
    """新增必填"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//p[text()="请输入该必填项"]')).text
    expected='请输入该必填项'

    assert expected == actual
    time.sleep(2)

def test_009(browser):
    """类别唯一"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys('公司资产')
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//p[text()="当前类别名称已被使用"]')).text
    expected='当前类别名称已被使用'

    assert expected == actual
    time.sleep(2)

def test_010(browser):
    """编码唯一"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//input[@name="code"]')).send_keys('111')
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//p[text()="当前类别编码已被使用"]')).text
    expected='当前类别编码已被使用'

    assert expected == actual
    time.sleep(2)

def test_003(browser):

    """编码规范汉字"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_china())
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//p[text()="请输入由大小写英文字母、数字、及特殊符号组成的字符串(特殊符号包括 - ~ · / \ | _ ),比如:Abc123、A-123"]')).text
    expected='请输入由大小写英文字母、数字、及特殊符号组成的字符串(特殊符号包括 - ~ · / \ | _ ),比如:Abc123、A-123'

    assert expected == actual
    time.sleep(1)


def test_004(browser):
    """编辑成功"""

    category=BasePage(browser)
    category.category_login()
        #先移动到对应元素，等待亮起，再点击
    category.move_to(('xpath', '(//span[@aria-label="修改类别名称"]//*[name()="svg"])[1]'))
    category.get_element(('xpath','(//span[@aria-label="修改类别名称"]//*[name()="svg"])[1]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).clear()
    category.get_element(('xpath', '//input[@name="code"]')).clear()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//div[text()="编辑成功"]')).text
    expected='编辑成功'

    assert expected == actual
    time.sleep(1)

def test_005(browser):
    """编辑必填"""
    category=BasePage(browser)
    category.category_login()

    category.move_to(('xpath','(//span[@aria-label="修改类别名称"]//*[name()="svg"])[2]'))
    category.get_element(('xpath','(//span[@aria-label="修改类别名称"]//*[name()="svg"])[2]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).clear()
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//p[text()="请输入该必填项"]')).text
    expected='请输入该必填项'

    assert expected == actual
    time.sleep(1)


def test_13(browser):
    """编辑编码唯一必填"""
    category=BasePage(browser)
    category.category_login()

    category.move_to(('xpath','(//span[@aria-label="修改类别名称"]//*[name()="svg"])[2]'))
    category.get_element(('xpath','(//span[@aria-label="修改类别名称"]//*[name()="svg"])[2]')).click()
    category.get_element(('xpath', '//input[@name="code"]')).clear()
    category.get_element(('xpath', '//input[@name="code"]')).send_keys('111')
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//p[text()="当前类别编码已被使用"]')).text
    expected='当前类别编码已被使用'

    assert expected == actual
    time.sleep(1)

def test_006(browser):
    """删除"""
    category=BasePage(browser)
    category.category_login()
        #删除同理，先移动到对应元素，图标亮起,不需要加其他操作
    category.move_to(('xpath', '(//button[@aria-label="删除该类别"]//*[name()="svg"])[1]'))
    category.get_element(('xpath','(//button[@aria-label="删除该类别"]//*[name()="svg"])[1]')).click()
    category.get_element(('xpath', '//button[text()="删除"]')).click()

    actual=category.get_element(('xpath', '//div[text()="删除成功"]')).text
    expected='删除成功'

    assert expected == actual
    time.sleep(1)


def test_007(browser):
    """替换表单"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath', '//p[text()="token"]')).click()
    category.get_element(('xpath','//button[text()="替换关联表单"]')).click()
    category.get_element(('xpath', '//div[@name="form"]//*[name()="svg"][@data-testid="ArrowDropDownIcon"]')).click()
    category.get_element(('xpath', '//li[text()="默认表单"]')).click()
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//div[text()="替换成功"]')).text
    expected='替换成功'

    assert expected == actual
    time.sleep(2)


def test_008(browser):
    """替换表单详情页面"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath', '//p[text()="token"]')).click()
    category.get_element(('xpath','//a[text()="默认表单"]')).click()

    actual=category.get_element(('xpath', '//h6[text()="基础信息"]')).text
    expected='基础信息'

    assert expected == actual
    time.sleep(2)

def test_12(browser):
    """精确搜索"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath', '//input[@placeholder="请搜索资产类别"]')).send_keys('token')

    actual=category.get_element(('xpath', '//p[text()="token"]')).text
    expected='token'

    assert expected == actual
    time.sleep(2)
