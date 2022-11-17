import faker
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver import Chrome
from test_web_selenium.config.config import config


class fields:

    def __init__(self,driver:Chrome):

        self.driver=driver

    def created_fd(self):

        name=self.mock_field_name()

        self.name=name
        self.driver = webdriver.Chrome()
        self.driver.get(config.sit_url)
        # driver.maximize_window()
        self.driver.implicitly_wait(10)  # 智能等待

        self.driver.find_element(By.NAME, 'tenantCode').send_keys(config.tenantCode)
        self.driver.find_element(By.NAME, 'account').send_keys(config.account)
        self.driver.find_element(By.NAME, 'password').send_keys(config.password)

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # driver.find_element(By.XPATH,'//div[@class="css-q37yd2"][3]//img').click()  #前面有管理中心的

        self.driver.find_element(By.XPATH, '//div[@class="css-q37yd2"]//img').click()
        self.driver.find_element(By.XPATH, '//span[text()="基础配置"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="字段配置"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="新增字段"]').click()
        self.driver.find_element(By.XPATH,'//input[@name="name"]').send_keys(self.name)
        self.driver.find_element(By.XPATH,'(//div[@name="group"])[2]').click()

        self.driver.find_element(By.XPATH,'//li[text()="基础信息"]').click()
        # driver.find_element(By.XPATH,'//button[text()="新增字段"]').click()  (//input[@name="_role"])[2]

        self.driver.find_element(By.XPATH, '//input[@name="desc"]').send_keys(self.name)

    def submits(self):

        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()

        self.driver.find_element(By.XPATH, '//div[@name="form"]').click()

        try:
            self.driver.find_element(By.XPATH, '//li[text()="自定义表单"]').click()

            self.driver.find_element(By.XPATH, '//div[text()="关联表单"]').click()

            self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()

            drivers = self.driver.find_element(By.XPATH, '//div[text() = "关联成功"]').text

            return drivers

        except Exception as e:
            self.driver.find_element(By.XPATH, '//div[text()="关联表单"]').click()
            self.driver.find_element(By.XPATH, '//button[text()="跳过"]').click()

            return




    def mock_field_name(self):
        fk = faker.Faker(locale=['zh_CN'])

        filed_name = fk.word()

        return filed_name

    def mock_number(self):
        fk = faker.Faker(locale=['zh_CN'])

        filed_name = fk.number()

        return filed_name



cre=fields()
