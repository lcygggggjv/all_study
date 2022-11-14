import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium import webdriver

from test_web_selenium.config.config import config

import keyboard

def created_Default_filed():

    driver = webdriver.Chrome()
    driver.get(config.sit_url)
    driver.implicitly_wait(10)  # 智能等待

    driver.find_element(By.NAME, 'tenantCode').send_keys(config.tenantCode)
    driver.find_element(By.NAME, 'account').send_keys(config.account)
    driver.find_element(By.NAME, 'password').send_keys(config.password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # driver.find_element(By.XPATH,'//div[@class="css-q37yd2"][3]//img').click()  #前面有管理中心的

    driver.find_element(By.XPATH, '//div[@class="css-q37yd2"]//img').click()
    driver.find_element(By.XPATH, '//button[text()="新增资产"]').click()
    driver.find_element(By.XPATH, '//div[@name="category"]//input').click()
    driver.find_element(By.XPATH, '//span[text()="121212"]').click()
    driver.find_element(By.XPATH, '//input[@name="code"]').send_keys('sde')
    driver.find_element(By.XPATH, '//input[@name="name"]').send_keys('000')
    driver.find_element(By.XPATH, '//input[@name="specification"]').send_keys('000')
    driver.find_element(By.XPATH, '//input[@name="modelNum"]').send_keys('000')

    driver.find_element(By.XPATH, '//div[@name="department"]//input').click()
    driver.find_element(By.XPATH, '//span[text()="tc"]').click()
    driver.find_element(By.XPATH, '//div[@name="manager"]//input').click()
    driver.find_element(By.XPATH, '//p[text()="普通1"]').click()


    file=driver.find_element(By.XPATH, '//span[text()="点击上传文件"]')

    action=ActionChains(driver)
    action.click(file).perform()

    time.sleep(2)
    fspath=r'D:\pycharm-workspace\test_项目搭建5\test_cases用例\cases.xlsx'

    keyboard.write(fspath)

    keyboard.press('enter')
    driver.find_element(By.XPATH, '//button[text()="确定"]').click()

    driver=driver.find_element(By.XPATH,'//div[text()="新增成功!"]').text

    return driver


