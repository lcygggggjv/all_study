
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from test_web_selenium.config.config import config
import keyboard

from test_web_selenium.page.login_page import login_page
from test_web_selenium.setting_faker import test_idea
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_selenium.thing_list.conftest import logins_page, browser


class Test_thing_Page():

    @classmethod
    def setup_class(cls):
        ad=login_page(browser)
        driver = ad.driver

        ad.login_thingList() #实例继承的默认登录到台账

        test_word=ad.created_faker()  #继承faker函数，


    def created_Default_filed(self):

        self.driver.find_element(By.XPATH, '//button[text()="新增资产"]').click()
        self.driver.find_element(By.XPATH, '//div[@name="category"]//input').click()
        self.driver.find_element(By.XPATH, '//span[text()="121212"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(self.test_word)
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(self.test_word)
        self.driver.find_element(By.XPATH, '//input[@name="specification"]').send_keys(self.test_word)
        self.driver.find_element(By.XPATH, '//input[@name="modelNum"]').send_keys(self.test_word)

        self.driver.find_element(By.XPATH, '//div[@name="department"]//input').click()
        self.driver.find_element(By.XPATH, '//span[text()="tc"]').click()
        self.driver.find_element(By.XPATH, '//div[@name="manager"]//input').click()
        self.driver.find_element(By.XPATH, '//p[text()="12312/普通1"]').click()

        file=self.driver.find_element(By.XPATH, '//span[text()="点击上传文件"]')  #不带任何方法

        # action=ActionChains(self.driver)   #action方法
        # action.click(file).perform()  #点击文件地址元素，perform
        #
        # time.sleep(2)     #写前强制等待一下
        # keyboard.write(config.thing_file)  #keyboard写入文件地址
        #
        # keyboard.press('enter')  #输入enter热键

        self.keyboard_file(self.driver,file,config.thing_file)

        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()

        # wait = WebDriverWait(self.driver, 15)  # 等待被点击
        #
        # locator = ((By.XPATH,'//div[text()="新增成功!"]'))  # 传入定位元素带上括号，文本之间 ；'name','lcy'
        #
        # wait.until(expected_conditions.element_to_be_clickable(locator))
        self.show_wait_element(self.driver,((By.XPATH,'//div[text()="新增成功!"]')))

        actual=self.driver.find_element(By.XPATH,'//div[text()="新增成功!"]').text

        expected ='新增成功!'

        assert  expected == actual

        self.driver.quit()


    def test_update_thing(self):

        self.login_thingList()
        test_word=self.created_faker()  #继承faker函数，
        self.test_word=test_word  #实例，下面用到

        self.driver.find_element(By.XPATH, '//span[@aria-label="编辑"]//button').click()

        self.driver.find_element(By.XPATH, '//input[@name="name"]').clear()

        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(self.test_word)

        self.driver.find_element(By.XPATH, '//input[@name="specification"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="specification"]').send_keys(self.test_word)
        self.driver.find_element(By.XPATH, '//input[@name="modelNum"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="modelNum"]').send_keys(self.test_word)

        self.driver.find_element(By.XPATH, '//div[@name="department"]//input').click()
        self.driver.find_element(By.XPATH, '(//button[@title="Clear"])[2]').click()

        self.driver.find_element(By.XPATH, '//h6[text()="管理信息"]').click()
        self.driver.find_element(By.XPATH, '//div[@name="department"]//input').click()
        self.driver.find_element(By.XPATH, '//div[@class="MuiListItemIcon-root css-lsa572"]//button').click()

        self.driver.find_element(By.XPATH, '//span[text()="1212"]').click()

        self.driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-79elbk"]//*[name()="svg"]').click()

        files=self.driver.find_element(By.XPATH, '//span[text()="点击上传文件"]')

        self.keyboard_file(self.driver,files,config.thing_file)   #继承封装的传文件的方法

        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()

        # wait=WebDriverWait(self.driver,15)   #等待被点击
        #
        # locator =(((By.XPATH,'//div[text()="编辑成功!"]')))   #传入定位元素带上括号，文本之间 ；'name','lcy'
        #
        # wait.until(expected_conditions.element_to_be_clickable(locator))  #等待元素被点击

        self.show_wait_element(self.driver,(By.XPATH,'//div[text()="编辑成功!"]'))  #用实例方法传入driver，和元素，直接复制元组

        actual=self.driver.find_element(By.XPATH,'//div[text()="编辑成功!"]').text

        expected='编辑成功!'

        assert expected == actual

        self.driver.quit()

    def test_delete_thing(self):

        self.login_thingList()

        self.driver.find_element(By.XPATH, '//span[@aria-label="删除"]//button').click()

        self.driver.find_element(By.XPATH, '//button[text()="删除"][@tabindex="0"]').click()


        self.show_wait_element(self.driver,(By.XPATH, '//div[text()="删除成功"]'))

        actual=self.driver.find_element(By.XPATH, '//div[text()="删除成功"]').text

        expected='删除成功'

        assert expected == actual

        self.driver.quit()

if __name__ == '__main__':

        ad=Test_thing_Page()
    # ad.test_created_Default_filed()
    #     ad.test_update_thing()