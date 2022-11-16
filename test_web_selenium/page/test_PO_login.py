
from test_web_selenium.page.login_page import login_page


#po模式导入对应页面类的函数方法，使用函数调用
def test_001(browser1):

    login=login_page(browser1)
    login.login_thingList()

