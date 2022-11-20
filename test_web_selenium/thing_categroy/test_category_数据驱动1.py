import time

import pytest

from test_web_selenium.common.basepage import BasePage

items=[
    {"category_name":"驱动1搞得","category_code":"eam_code","expected":"新增成功"},
    {"category_name":"","category_code":"eam_code","expected":"新增成功"},

]

#单个可以，后面的元素就不符合，不适用

@pytest.mark.parametrize('item',items)
def test_ddt_created(browser,item):

    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys(item['category_name'])
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(item['category_code'])
    category.get_element(('xpath', '//button[text()="确定"]')).click()
    category.show_wait_element(browser,('xpath', '//div[text()="新增成功"]'))
    actual=category.get_element(('xpath', '//div[text()="新增成功"]')).text
    expected=item['expected']

    assert expected == actual
    time.sleep(2)

