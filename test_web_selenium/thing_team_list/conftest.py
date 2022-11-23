import pytest
from selenium import webdriver



@pytest.fixture()
def  browser():

    driver=webdriver.Chrome()   #前置，初始化浏览器对象
    driver.implicitly_wait(10)

    yield driver  #返回driver值
    driver.quit()   #后置，退出
