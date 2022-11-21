import time

from test_web_selenium.common.basepage import BasePage



def test_01(area_browser):
    """新增区域"""

    area=BasePage(area_browser)
    area.area_login()

    area.get_element(('xpath','//span[@aria-label="新增下属区域"]//*[name()="svg"]')).click()
    area.get_element(('xpath','//input[@name="name"]')).send_keys(area.fk_word())
    area.get_element(('xpath','//input[@name="code"]')).send_keys(area.fk_word())
    area.get_element(('xpath', '//button[text()="确定"]')).click()
    # actual=('xpath','//div[text()="编辑成功"]')  传元素直接变量接收即可
    # area.asser_el_text_equal(expected, actual)
    actual=area.get_element(('xpath','//div[text()="新增成功"]')).text
    expected='新增成功'

    assert expected == actual    #有时弹框关闭太空，先等待一下,因为browser设置了quit

def test_02(area_browser):
    """新增必填"""

    area=BasePage(area_browser)
    area.area_login()

    area.get_element(('xpath','//span[@aria-label="新增下属区域"]//*[name()="svg"]')).click()
    area.get_element(('xpath', '//button[text()="确定"]')).click()
    actual=area.get_element(('xpath','//p[text()="请输入该必填项"]')).text
    expected='请输入该必填项'

    assert expected == actual


def test_03(area_browser):
    """新增区域唯一性"""

    area=BasePage(area_browser)
    area.area_login()

    area.get_element(('xpath','//span[@aria-label="新增下属区域"]//*[name()="svg"]')).click()
    area.get_element(('xpath','//input[@name="name"]')).send_keys('tc')
    area.get_element(('xpath', '//button[text()="确定"]')).click()
    actual=area.get_element(('xpath','//p[text()="区域名称已被使用"]')).text
    expected='区域名称已被使用'

    assert expected == actual


def test_05(area_browser):
    """区域编码格式校验"""

    area=BasePage(area_browser)
    area.area_login()

    area.get_element(('xpath','//span[@aria-label="新增下属区域"]//*[name()="svg"]')).click()
    area.get_element(('xpath','//input[@name="name"]')).send_keys(area.fk_word())
    area.get_element(('xpath','//input[@name="code"]')).send_keys(area.fk_china())
    area.get_element(('xpath', '//button[text()="确定"]')).click()
    actual=area.get_element(('xpath','//p[text()="请输入由大小写英文字母、数字、及特殊符号组成的字符串(特殊符号包括 - ~ · / \ | _ ),比如:Abc123、A-123"]')).text
    expected='请输入由大小写英文字母、数字、及特殊符号组成的字符串(特殊符号包括 - ~ · / \ | _ ),比如:Abc123、A-123'

    assert expected == actual


def test_06(area_browser):
    """区域编码格式校验"""

    area=BasePage(area_browser)
    area.area_login()

    area.get_element(('xpath','//span[@aria-label="新增下属区域"]//*[name()="svg"]')).click()
    area.get_element(('xpath','//input[@name="name"]')).send_keys(area.fk_word())
    area.get_element(('xpath','//input[@name="code"]')).send_keys('123')
    area.get_element(('xpath', '//button[text()="确定"]')).click()
    actual=area.get_element(('xpath','//p[text()="当前区域编码已被使用"]')).text
    expected='当前区域编码已被使用'

    assert expected == actual


def test_07(area_browser):
    """编辑区域"""

    area=BasePage(area_browser)
    area.area_login()

    # area.get_element(('xpath','//p[text()="best"]')).click()
    area.move_to(('xpath','(//span[@aria-label="修改区域名称"]//*[name()="svg"])[1]'))
    area.get_element(('xpath','(//span[@aria-label="修改区域名称"]//*[name()="svg"])[1]')).click()
    area.get_element(('xpath','//input[@name="name"]')).clear()
    area.get_element(('xpath','//input[@name="code"]')).clear()
    area.get_element(('xpath','//input[@name="name"]')).send_keys(area.fk_word())
    area.get_element(('xpath','//input[@name="code"]')).send_keys(area.fk_word())
    area.get_element(('xpath', '//button[text()="确定"]')).click()
    # actual=('xpath','//div[text()="编辑成功"]')  传元素直接变量接收即可
    # area.asser_el_text_equal(expected, actual)
    actual=area.get_element(('xpath','//div[text()="编辑成功"]')).text
    expected='编辑成功'

    assert expected == actual   #有时弹框关闭太空，先等待一下
    time.sleep(1)

def test_08(area_browser):
    """编辑区域"""

    area=BasePage(area_browser)
    area.area_login()
        #先移动到对应的元素，然后元素亮起，再点击
    area.move_to(('xpath','(//span[@aria-label="修改区域名称"]//*[name()="svg"])[2]'))
    area.get_element(('xpath','(//span[@aria-label="修改区域名称"]//*[name()="svg"])[2]')).click()
    area.get_element(('xpath','//input[@name="code"]')).clear()
    area.get_element(('xpath','//input[@name="code"]')).send_keys('123')
    area.get_element(('xpath', '//button[text()="确定"]')).click()
    # actual=('xpath','//div[text()="编辑成功"]')  传元素直接变量接收即可
    # area.asser_el_text_equal(expected, actual)
    actual=area.get_element(('xpath','//p[text()="当前区域编码已被使用"]')).text
    expected='当前区域编码已被使用'

    assert expected == actual   #有时弹框关闭太空，先等待一下


def test_09(area_browser):
    """删除区域"""

    area=BasePage(area_browser)
    area.area_login()
        #先移动到对应的元素，然后元素亮起，再点击
    area.move_to(('xpath','(//button[@aria-label="删除该区域"]//*[name()="svg"])[1]'))
    area.get_element(('xpath','(//button[@aria-label="删除该区域"]//*[name()="svg"])[1]')).click()
    area.get_element(('xpath', '//button[text()="删除"]')).click()
    actual=area.get_element(('xpath','//div[text()="删除成功"]')).text
    expected='删除成功'

    assert expected == actual   #有时弹框关闭太空，先等待一下
    time.sleep(2)


def test_10(area_browser):
    """搜索区域"""

    area=BasePage(area_browser)
    area.area_login()
        #先移动到对应的元素，然后元素亮起，再点击
    area.get_element(('xpath','//input[@placeholder="请搜索"][@aria-invalid="false"]')).send_keys('213')
    actual=area.get_element(('xpath','//p[text()="213"]')).text
    expected='213'

    assert expected == actual   #有时弹框关闭太空，先等待一下
    time.sleep(2)