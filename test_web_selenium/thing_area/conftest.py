import pytest
from selenium import webdriver



#pytes.fixture 夹具 #生成浏览器对象
@pytest.fixture
def area_browser():

    driver=webdriver.Chrome()  #初始化浏览器，前置

    driver.implicitly_wait(10)

    yield driver   #返回driver值

    driver.quit()  #后置