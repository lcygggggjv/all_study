
from test_web_selenium.page.login_page import login_page
from selenium import webdriver

def test_002():

    login=login_page()

    login.login_thingList()

