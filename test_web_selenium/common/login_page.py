from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium import webdriver

from test_web_selenium.config.config import config


class login_page:

    tentcode=(By.NAME, 'tenantCode')
    account=(By.NAME, 'account')
    password=(By.NAME, 'password')
    submit=(By.XPATH, "//button[@type='submit']")
    eamicon=(By.XPATH, '//div[@class="css-q37yd2"]//img')

    # """浏览器通用操作  Chrome的类，浏览器driver对象"""
    def __init__(self,driver:Chrome):

        self.driver= driver


    def login_thingList(self):

        self.driver.get(config.sit_url)
        self.driver.implicitly_wait(10)  # 智能等待

        self.driver.find_element(*self.tentcode).send_keys(config.tenantCode)  #加个*号，元组解包
        self.driver.find_element(*self.account).send_keys(config.account)
        self.driver.find_element(*self.password).send_keys(config.password)
        self.driver.find_element(*self.submit).click()

        # driver.find_element(By.XPATH,'//div[@class="css-q37yd2"][3]//img').click()  #前面有管理中心的
        self.driver.find_element(*self.eamicon).click()

        return self






