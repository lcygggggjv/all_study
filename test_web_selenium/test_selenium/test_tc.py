
from selenium import webdriver

from selenium.webdriver.common.by import By

import time
from test_web_selenium.config.config import config
import faker

def mock_field_name():

    fk=faker.Faker(locale=['zh_CN'])

    filed_name=fk.name()

    return filed_name



def created_TextField(name):

    driver = webdriver.Chrome()
    driver.get(config.sit_url)
    # driver.maximize_window()
    driver.implicitly_wait(10)  #智能等待

    driver.find_element(By.NAME,'tenantCode').send_keys(config.tenantCode)
    driver.find_element(By.NAME,'account').send_keys(config.account)
    driver.find_element(By.NAME,'password').send_keys(config.password)

    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    # driver.find_element(By.XPATH,'//div[@class="css-q37yd2"][3]//img').click()  #前面有管理中心的

    driver.find_element(By.XPATH,'//div[@class="css-q37yd2"]//img').click()
    driver.find_element(By.XPATH,'//span[text()="基础配置"]').click()

    driver.find_element(By.XPATH,'//span[text()="字段配置"]').click()
    driver.find_element(By.XPATH,'//button[text()="新增字段"]').click()
    #
    # driver.find_element(By.XPATH,'//button[text()="新增字段"]').click()

    driver.find_element(By.XPATH,'//input[@name="name"]').send_keys(name)
    driver.find_element(By.XPATH,'(//div[@name="group"])[2]').click()

    driver.find_element(By.XPATH,'//li[text()="基础信息"]').click()
    # driver.find_element(By.XPATH,'//button[text()="新增字段"]').click()  (//input[@name="_role"])[2]

    driver.find_element(By.XPATH, '//input[@name="desc"]').send_keys(name)

    driver.find_element(By.XPATH, '//input[@name="suffix"]').send_keys(name)
    driver.find_element(By.XPATH, '//input[@name="placeholder"]').send_keys(name)
    driver.find_element(By.XPATH, '//input[@name="defaultString"]').send_keys(name)

    driver.find_element(By.XPATH,'//button[text()="确定"]').click()
    # driver.find_element(By.XPATH,'(//input[@autocomplete="off"])[3]').click()


    driver.find_element(By.XPATH,'//div[@name="form"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//li[text()="表单33"]').click()
    driver.find_element(By.XPATH,'//div[text()="关联表单"]').click()


    driver.find_element(By.XPATH,'//button[text()="确定"]').click()

    driver=driver.quit()

    return driver


name=mock_field_name()
created_TextField(name)









#  切换页面  iframe方法，drive.switch_to.frame
#id 会变 _name
#元素定位
# 下标索引用的很少，无法判断顺序
#
#
# driver.quit()




