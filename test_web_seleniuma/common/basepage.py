import time

import faker
import keyboard
from selenium.common import InvalidArgumentException
from selenium.webdriver import Chrome, ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT=10

class BasePage:

    """浏览器通用操作  Chrome的类，浏览器driver对象"""
    def __init__(self,driver:Chrome):

        self.driver= driver

    def get_element(self,locator):
        """定位元素"""
        return self.driver.find_element(*locator)  # 直接传元组，通过*解包,传的不用这里已经加了

    def get_url(self,url):
        #访问网页
        self.driver.get(url)

        return self  #返回对象本身，可以不


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



    def click(self,locator):
        """click点击"""
        el=self.get_element(locator)
        el.click()
        try:
            el.click()

        except InvalidArgumentException as e:   #try,click点击不了，捕获异常，满足InvalidArgumentException错误类型
                #通过action方法点击
             ActionChains(self.driver).click(el).perform()  #初始化action对象
        return self

    def action_click(self,locator):
        """actionChains点击"""
        action=ActionChains(self.driver)   #传入driver
        action.click(locator).perform()   #click元素 +perform
        return self


    def send_keys(self,locator,word):
        """输入"""
        el=self.get_element(locator)
        try:
            el.send_keys(word)
        except:
            ActionChains(self.driver).send_keys_to_element(el,word).perform()
                                                #先移动定位光标元素，再输入内容
        return self

    def double_click(self,locator):
        """双击"""
        el=self.get_element(locator)
        ActionChains(self.driver).double_click(el).perform()   #action方法双击
        return self

    def drag_and_drop(self,start_locator,end_locator):
        """拖动"""
        start_el=self.get_element(start_locator)  #拖动前元素
        end_el=self.get_element(end_locator)  #拖动后元素

        ActionChains(self.driver).drag_and_drop(start_el,end_el).perform()   #传入拖到前和拖到后元素
        return self

    def move_to(self,locator):
        """移动某个元素"""
        el=self.get_element(locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return self

    def press_enter(self):
        """按下回车键"""
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        return self

    def copy(self):
        """复制"""
        action=ActionChains(self.driver).key_down(Keys.CONTROL)   #先按下CTRL
        action.send_keys('c').key_up(Keys.CONTROL).perform()   #再输入c，再把CTRL松开，点击perform
        return self

    def paster(self):
        """粘贴"""
        action=ActionChains(self.driver).key_down(Keys.CONTROL)  #先按下CTRL
        action.send_keys('v').key_up(Keys.CONTROL).perform()   #再输入v，把ctrl松开 ，点击perform
        return self

    def show_wait_el_clickable(self,locator):
        """显性等待，某个元素被点击"""
        wait=WebDriverWait(driver=self.driver,timeout=6)   #要传入driver 和默认等待时间
        el=wait.until(expected_conditions.element_to_be_clickable(locator))  #使用expected_conditions的clickable，并传入元素
        return el

    def show_wait_el_visible(self,locator):
        """等待某个元素被看到"""
        wait=WebDriverWait(driver=self.driver,timeout=6)
        el=wait.until(expected_conditions.visibility_of_element_located(locator))
        return el

    def switch_to_iframe(self,locator=None):
        """切换某个iframe"""
        if locator is None:  #如果没传去哪个页面元素，默认去主页面
            self.driver.switch_to.default_content()
            return self
        el=self.get_element(locator)
        self.driver.switch_to.frame(el)
        return self

    def switch_to_window(self,locator=None):
        """切换某个窗口"""
        if locator is None:  #没传新窗口元素，默认去主页面
            self.driver.switch_to.default_content()
        el=self.get_element(locator)
        self.driver.switch_to.window(el)
        return self

    def scroll_to_bottom(self):
        """滚动到窗口底部"""
        js='window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        return self

    def update_value(self,locator,value):
        """修改元素value属性"""
        el=self.get_element(locator)
        js="""
        Arguments[0].readOnly=false;
        Arguments[0].value = '{}'
        """.format(value)
        self.driver.execute_script(js,el)
        return self

    def asser_el_text_equal(self,locator,expected):
            #断言，传元素吗，和预期加个
        el=self.get_element(locator)
        assert expected ==el.text   #等于获得的元素的文本
