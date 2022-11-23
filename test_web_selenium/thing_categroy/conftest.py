
from selenium import webdriver
import pytest


#浏览器的对象
@pytest.fixture()
def browser():

    driver=webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()



# @pytest.fixture()
# def logins_page(browser):
#
#     page=login_page(browser1)
#
#     return page