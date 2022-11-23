import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_selenium.config.config import config

from pykeyboard import PyKeyboard
from pymouse import PyMouse


def login_thingList2(self):

    driver = webdriver.Chrome()
    driver.get(config.sit_url)
    driver.implicitly_wait(10)  # 智能等待
    word = self.test_word()

    driver.find_element(*self.tentcode).send_keys(config.tenantCode)  # 加个*号，元组解包
    driver.find_element(*self.account).send_keys(config.account)
    driver.find_element(*self.password).send_keys(config.password)
    driver.find_element(*self.submit).click()

    # driver.find_element(By.XPATH,'//div[@class="css-q37yd2"][3]//img').click()  #前面有管理中心的
    driver.find_element(*self.eamicon).click()
    driver.find_element(By.XPATH, '//button[text()="新增资产"]').click()
    driver.find_element(By.XPATH, '//div[@name="category"]//input').click()
    driver.find_element(By.XPATH, '//span[text()="121212"]').click()
    driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(self.word)
    driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(self.word)
    driver.find_element(By.XPATH, '//input[@name="specification"]').send_keys(self.word)
    driver.find_element(By.XPATH, '//input[@name="modelNum"]').send_keys(self.word)

    driver.find_element(By.XPATH, '//div[@name="department"]//input').click()
    driver.find_element(By.XPATH, '//span[text()="tc"]').click()
    driver.find_element(By.XPATH, '//div[@name="manager"]//input').click()
    driver.find_element(By.XPATH, '//p[text()="12312/普通1"]').click()
    # mac
    # 初始化action方法，传入driver

    pyautogui.write('/Users/bbt/Desktop/3.jpeg')
    pyautogui.press('enter', 3)
    time.sleep(2)
    pyautogui.moveTo(1230, 610, duration=1)
    pyautogui.click()





    self.driver.find_element(By.XPATH, '//span[text()="点击上传文件"]').click()  # 不带任何方法


    # self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()

    # return self
