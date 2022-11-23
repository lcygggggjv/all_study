import time

import keyboard
from selenium.webdriver import Chrome, ActionChains

from selenium.webdriver.support import expected_conditions
from  selenium.webdriver.support.wait import WebDriverWait
import faker

DEFAULT_TIMEOUT=10

class ideas:


    def created_faker(self):

        self.fk=faker.Faker()  #生成英语单词
        word=self.fk.word()
        return word


    def show_wait_element(self,driver,locator,timeout=DEFAULT_TIMEOUT):   #超时时间写一个默认参数5

        wait=WebDriverWait(driver=driver,timeout=timeout)  #调用wait方法

        el=wait.until(expected_conditions.element_to_be_clickable(locator))  #直到被点击

        return el


    def keyboard_file(self,driver,files,fspath,locator="enter"):


        action=ActionChains(driver)   #初始化action方法，传入driver

        action.click(files).perform()  #传入点击文件定位元素

        time.sleep(3)  #等待一下
        keyboard.write(fspath)   #写入附件地址

        # self.show_wait_element(driver,locator)

        keyboard.press('enter')   #按下enter

        time.sleep(3)  #按下enter，有一定缓冲时间才能上传成功


if __name__ == '__main__':

    a=ideas()
    b=a.created_faker()
    print(b)


