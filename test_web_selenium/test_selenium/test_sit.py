import unittest

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

import time
from test_web_selenium.config.config import config
import faker

from test_web_selenium.test_selenium.conftest import brw
from test_web_selenium.test_selenium.field_api import fields
import unittestreport
import pytest


# @pytest.fixture(scope='class')
class Test_created_filed():

    def setup(self):

        ds=fields(brw())
        self.created_fd()

        name=self.mock_field_name()   #实例调用mock方法
        self.name=name  #实例name属性，下面有用到

        yield

    def test_created_TextField(self):   #文本输入

        # name = self.mock_field_name()  # 实例调用mock方法
        # self.name = name   # 实例name属性，下面有用到
        # # self.driver = webdriver.Chrome()  #不需要写因为下面那个已经有了
        # self.created_fd()

        # driver.find_element(By.XPATH,'//button[text()="新增字段"]').click()
        # driver.find_element(By.XPATH, '//input[@name="suffix"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//input[@name="placeholder"]').send_keys(self.name)
        self.driver.find_element(By.XPATH, '//input[@name="defaultString"]').send_keys(self.name)

        self.submits()   #调用复用的函数

    def test_created_numfield(self):    #数值输入

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="number"]').click()

        self.driver.find_element(By.XPATH, '//input[@name="min"]').send_keys('1')
        self.driver.find_element(By.XPATH, '//input[@name="max"]').send_keys('10')
        self.driver.find_element(By.XPATH, '//input[@name="unit"]').send_keys(self.name)
        self.driver.find_element(By.XPATH, '//input[@name="placeholder"]').send_keys(self.name)
        self.driver.find_element(By.XPATH, '//input[@name="defaultNumber"]').send_keys('6')

        self.submits()

    def test_created_numrange(self):    #数值范围

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="range"]').click()

        self.driver.find_element(By.XPATH, '//input[@name="unit"]').send_keys('元')
        self.driver.find_element(By.XPATH, '//input[@name="minRange.min"]').send_keys('1')
        self.driver.find_element(By.XPATH, '//input[@name="minRange.max"]').send_keys('10')
        self.driver.find_element(By.XPATH, '//input[@name="minRange.placeholder"]').send_keys(self.name)
        self.driver.find_element(By.XPATH, '//input[@name="minRange.defaultNumber"]').send_keys('6')
        self.driver.find_element(By.XPATH, '//input[@name="maxRange.min"]').send_keys('3')

        self.driver.find_element(By.XPATH, '//input[@name="maxRange.max"]').send_keys('15')
        self.driver.find_element(By.XPATH, '//input[@name="maxRange.placeholder"]').send_keys(self.name)
        self.driver.find_element(By.XPATH, '//input[@name="maxRange.defaultNumber"]').send_keys('3')

        self.submits()

    def test_created_down_select(self):   #下拉单项

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="select"]').click()

        # self.driver.find_element(By.XPATH, '//input[@name="field"][@value="select"]').click()
        self.driver.find_element(By.XPATH, '(//input[@autocomplete="off"])[3]').send_keys(self.name,Keys.ENTER)

        self.driver.find_element(By.XPATH, '(//input[@autocomplete="off"])[3]').send_keys('张三',Keys.ENTER)
        self.driver.find_element(By.XPATH, '(//input[@autocomplete="off"])[3]').send_keys('劳拉',Keys.ENTER)
        self.driver.find_element(By.XPATH, '//input[@name="placeholder"]').send_keys(self.name)
        self.driver.find_element(By.XPATH, '//div[@name="defaultString"]').click()

        self.driver.find_element(By.XPATH, '(//li[@role="option"])[1]').click()

        self.submits()

    def test_created_date_selection(self):   #日期选择

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="date"]').click()

        self.driver.find_element(By.XPATH, '//div[@name="format"]//input[@autocomplete="off"]').click()

        self.driver.find_element(By.XPATH, '//li[text()="yyyy-mm-dd hh:mm"]').click()

        self.driver.find_element(By.XPATH, '// input[@name="defaultBoolean"][@value="true"]').click()

        self.driver.find_element(By.XPATH, '//input[@name="placeholder"]').send_keys(self.name)

        self.submits()

    def test_created_date_range(self):   #日期范围

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="date-set"]').click()

        self.driver.find_element(By.XPATH, '//div[@name=".fields.0.format"]//input[@autocomplete="off"]').click()

        self.driver.find_element(By.XPATH, '//li[text()="yyyy-mm"]').click()

        self.driver.find_element(By.XPATH, '//input[@name=".fields.0.defaultBoolean"][@value="true"]').click()

        self.driver.find_element(By.XPATH, '//input[@name=".fields.0.placeholder"]').send_keys(self.name)

        self.driver.find_element(By.XPATH, '//input[@name=".fields.1.defaultBoolean"][@value="true"]').click()

        self.driver.find_element(By.XPATH, '//input[@name=".fields.1.placeholder"]').send_keys(self.name)

        self.submits()

    def test_created_text_trips(self):   #提示文本

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="label"]').click()

        self.driver.find_element(By.XPATH, '//input[@name="defaultString"]').send_keys(self.name)

        self.submits()

    def test_created_one_radio(self):   #单项选择

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="radio"]').click()

        # self.driver.find_element(By.XPATH, '//input[@name="field"][@value="select"]').click()
        self.driver.find_element(By.XPATH, '//div[@name="options"]//input[@autocomplete="off"]').send_keys(self.name,Keys.ENTER)

        self.driver.find_element(By.XPATH, '//div[@name="options"]//input[@autocomplete="off"]').send_keys("张三",Keys.ENTER)
        self.driver.find_element(By.XPATH, '//div[@name="options"]//input[@autocomplete="off"]').send_keys("劳拉",Keys.ENTER)
        self.driver.find_element(By.XPATH, '//div[@name="defaultString"]//input').click()


        self.driver.find_element(By.XPATH, '(//li[@role="option"])[1]').click()

        self.submits()

    def test_created_checkbox(self):  # 多项选择

        # name = self.mock_field_name()
        #
        # self.name = name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="checkbox"]').click()

        # self.driver.find_element(By.XPATH, '//input[@name="field"][@value="select"]').click()
        self.driver.find_element(By.XPATH, '//div[@name="options"]//input[@autocomplete="off"]').send_keys(self.name,
                                                                                                           Keys.ENTER)

        self.driver.find_element(By.XPATH, '//div[@name="options"]//input[@autocomplete="off"]').send_keys("张三",
                                                                                                           Keys.ENTER)
        self.driver.find_element(By.XPATH, '//div[@name="options"]//input[@autocomplete="off"]').send_keys("劳拉",
                                                                                                           Keys.ENTER)
        self.driver.find_element(By.XPATH, '//div[@name="defaultStringArray"]//input').click()

        self.driver.find_element(By.XPATH, '(//li[@role="option"])[1]').click()
        self.driver.find_element(By.XPATH, '(//li[@role="option"])[2]').click()

        self.submits()


    def test_created_attachment(self):   #上传附件，自定义；txt，jpg，xlsx

        # name=self.mock_field_name()
        #
        # self.name=name
        #
        # self.created_fd()

        self.driver.find_element(By.XPATH, '//input[@name="field"][@value="attachment"]').click()

        self.driver.find_element(By.XPATH, '//input[@name="hint"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="maxSize"]').send_keys('5')
        self.driver.find_element(By.XPATH, '//input[@name="maxCount"]').send_keys('3')
        self.driver.find_element(By.XPATH, '//input[@name="attachmentType"][@value="CUSTOM"]').click()
        self.driver.find_element(By.XPATH, '//div[@name="extension"]//input').send_keys('txt',Keys.ENTER)
        self.driver.find_element(By.XPATH, '//div[@name="extension"]//input').send_keys('jpg',Keys.ENTER)

        self.driver.find_element(By.XPATH, '//div[@name="extension"]//input').send_keys('xlsx',Keys.ENTER)

        self.submits()

if __name__ == '__main__':

    cre=Test_created_filed()
    # ces = cre.test_created_TextField()
    # ces=cre.test_created_numfield()
    # ces=cre.test_created_numrange()
    # ces=cre.test_created_down_select()
    # ces = cre.test_created_date_selection()
    # ces = cre.test_created_date_range()
    # ces = cre.test_created_text_trips()
    # ces = cre.test_created_one_radio()
    # ces = cre.test_created_checkbox()
    ces = cre.test_created_attachment()
    print(ces)
