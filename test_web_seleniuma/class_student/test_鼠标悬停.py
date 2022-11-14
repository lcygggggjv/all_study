import time

from selenium import webdriver
from selenium.webdriver import ActionChains


def test_1():

    driver=webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.get("https://www.runoob.com/html/html-tutorial.html")

    #找到悬停前的元素点击
    html=driver.find_element('xpath',' //a[text()=" HTML / CSS"]')

    #移动到html元素，使用actionCHAINS方法

    action=ActionChains(driver) #初始化action方法 driver对象

    action.move_to_element(html).perform()  #action使用move方法，输入元素，再加perform

    css3=driver.find_element('xpath','//a[text()="CSS3 教程"]') #继续点击元素
    action.click(css3).perform()
    time.sleep(2)
    driver.quit()

