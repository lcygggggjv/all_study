import time

import faker
import keyboard
from selenium.webdriver import Chrome, ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_selenium.config.config import config
from test_web_selenium.page.conftest import browser1
DEFAULT_TIMEOUT=10

# PO模式
class login_page:

    #元素类属性
    tentcode=(By.NAME, 'tenantCode')
    account=(By.NAME, 'account')
    password=(By.NAME, 'password')
    submit=(By.XPATH, "//button[@type='submit']")
    eamicon=(By.XPATH, '//div[@class="css-q37yd2"]//img')


    def __init__(self,driver:Chrome):   #声明driver为浏览器对象/类

        self.driver=driver

    def login_thingList(self):

        # self.driver=webdriver.Chrome()
        self.driver.get(config.sit_url)
        self.driver.implicitly_wait(10)  # 智能等待

        self.driver.find_element(*self.tentcode).send_keys(config.tenantCode)  #加个*号，元组解包
        self.driver.find_element(*self.account).send_keys(config.account)
        self.driver.find_element(*self.password).send_keys(config.password)
        self.driver.find_element(*self.submit).click()

        # driver.find_element(By.XPATH,'//div[@class="css-q37yd2"][3]//img').click()  #前面有管理中心的
        self.driver.find_element(*self.eamicon).click()

        return self

    def created_faker(self):

        fk=faker.Faker()  #生成英语单词
        word=fk.word()
        return word


    def show_wait_element(self,driver,locator,timeout=DEFAULT_TIMEOUT):   #超时时间写一个默认参数5

        wait=WebDriverWait(driver=driver,timeout=timeout)  #调用wait方法

        el=wait.until(expected_conditions.element_to_be_clickable(locator))  #直到被点击

        return el


    def keyboard_file(self,driver,files,fspath,locator="enter"):


        action=ActionChains(driver)   #初始化action方法，传入driver

        action.click(files).perform()  #传入点击文件定位元素

        time.sleep(3)  #等待一下
        keyboard.write(fspath)   #写入附件地址

        # self.show_wait_element(driver,locator)

        keyboard.press('enter')   #按下enter

        time.sleep(3)  #按下enter，有一定缓冲时间才能上传成功

