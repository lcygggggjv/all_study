import pytest
from selenium import webdriver



def brw():

    driver=webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()