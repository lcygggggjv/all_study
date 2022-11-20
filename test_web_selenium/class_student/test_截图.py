import time

#  selenium自带方法， driver.save_screenshot()
from test_web_selenium.common.basepage import BasePage
import allure


def test_002(browser):
    """新增必填"""
    category=BasePage(browser)
    category.category_login()

    category.get_element(('xpath','//span[@aria-label="新增下属类别"]//*[name()="svg"]')).click()
    category.get_element(('xpath', '//input[@name="name"]')).send_keys('')
    category.get_element(('xpath', '//input[@name="code"]')).send_keys(category.fk_word())
    category.get_element(('xpath', '//button[text()="确定"]')).click()

    actual=category.get_element(('xpath', '//p[text()="请输入该必填项"]')).text
    expected='请输入该必填项1'

    #这个是把图片存到文件里
    # browser.save_screenshot('jie_shot.png')
    # assert expected == actual

    #断言前进行截图,把传进来的browser当driver，使用这个方法，传进文件名称，失败截图，断言后
    #try ，失败进行截图，最后抛出异常
    try:
        assert expected == actual
    except Exception as e:
        # browser.save_screenshot('jie_shot.png')
        img=browser.get_screenshot_as_png()   #获取到二进制信息，到变量img里
        allure.attach(img,name='失败用例截图',attachment_type=allure.attachment_type.PNG)  #失败用例就会放到这里
        raise e     #通过allure。attch方法，传入变量img，并取名，以及图片的格式
    time.sleep(2)
