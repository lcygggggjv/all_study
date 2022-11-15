import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options




#访问百度首页
# drivers.get("http://www.baidu.com/")
#
# #设置浏览器大小；全屏
#
# drivers.maximize_window()
# time.sleep(2)

#设置分辨率 500*500
# drivers.set_window_size(500,500)
# time.sleep(2)


#

#截图预览
# drivers.get_screenshot_as_file('截图.png')
#
# drivers.get(r'https://www.taobao.com')
# time.sleep(2)


#后退操作
# drivers.back()
# time.sleep(2)

#刷新页面


# try:
#     #刷新页面
#     drivers.refresh()
#     print('刷新页面')
# except Exception as e:
#
#     print('刷新失败')
#
# time.sleep(3)
#
# drivers.quit()

# 网页标题
# print(drivers.title)
#
# #当前网址
#
# print(drivers.current_url)
#
# #浏览器名称
# print(drivers.name)
#
# #网页源码
# print(drivers.page_source)




# drivers.get("http://www.baidu.com/")
#
# #智能等待时间
#
# drivers.implicitly_wait(10)

# 在搜索框输入  python
# send_keys('hello')

# 点击  click

#  获取文本   text

#   attribute---id  属性

#id  定位
# drivers.find_element(By.ID,'kw').send_keys('python')

#name  定位
# drivers.find_element(By.NAME,'wd').send_keys('c罗')

#class定位
#
# drivers.find_element(By.CLASS_NAME,'s_ipt').send_keys('qq')
#
# drivers.find_element(By.ID,'su').click()

#   文本链接 选择链接里，选择文本
# drivers.find_element(By.LINK_TEXT,'新闻').click()

# drivers.find_element(By.XPATH,'//div [@has-tts="false"]//a/em').click()

 #代码运行速度太快  需要页面元素等待


#获取页面属性  y有变量logo接收

# logo=drivers.find_element(By.XPATH,'//span[@class="c-img-border c-img-radius-large"]')
#
# print(logo)
# print(logo.get_attribute('src'))   #获取属性
# # #

#
# driver=drivers.find_element(By.LINK_TEXT,"QQ").click()
# print(driver)

# drivers.find_element(By.XPATH,'//h3[@class="c-title t t tts-title"]//a').click()



# print(texts.text)
# print(texts.get_attribute('href'))   #获取属性，要输入对应的href值


# drivers.quit()



# 页面定位不到元素；
# 1  元素定位表达式错误
#
# 2 没有时间等待
#
# 3  有多个窗口，或iframe，有再alert
#
# 窗口切换   switch_to.window
# 当点击某按钮，切换页面  ，进行
#
# 1多窗口 switch_to.window
# 先点击切换前的窗口，打印当前窗口driver.current_window_handle。然后点击操作，在打印所有窗口，之后切换窗口到自己想要的
# driver.switch_to.window(driver.window_handles[-1])
#
#
# 2网页嵌套另一个网页  iframe
# switch_to.ifram（）  括号填写iframe的名称  1name，2索引 有几个 从0开始 不用写[]    iframe   3先找到iframe 传进去
# 原因和多窗口一样，元素不在当前页面
#
#
# 如果切换子页面之后，再找主页面的元素，再切换主页面，才能定位
# 切换主页面 switch_to.default_content()


#导入actionchains方法


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')

driver.find_element('id','kw').send_keys('lcy')


action=ActionChains(driver)

#全选
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

#复制
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()


for i in range(5):  #for循环粘贴
    action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(3)

# control+shift+v

action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('v').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
