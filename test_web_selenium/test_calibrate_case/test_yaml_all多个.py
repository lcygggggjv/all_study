

"""
关键字驱动实现
1，读取yaml当中的测试步骤

"""
import time

import pytest
import yaml

from test_web_selenium.common.basepage import BasePage
from test_web_selenium.test_calibrate_case.conftest import browser

with open('logins.yaml',encoding='utf-8') as f:

    cases=list(yaml.safe_load_all(f))  #safe.load读取yaml文件数据,all 全部  ,转换列表



@pytest.mark.parametrize('steps',cases)   #数据驱动，pytest的，cases是文件 ,steps是字符串
#要再方法里先添加browser
def test_yaml(browser,steps):   #传入steps数据
    # steps列表嵌套字典
    #初始化basepage
    page=BasePage(browser)

    for step in steps:
        action_name=step['action']  #action_name＝step里的action的操作名称，字符串
        params=step['params']  #同样取数据内容，{"locator":{}}yaml取出字典类型
        method=getattr(page,action_name)  #getattr方法，通过page得到acion——name的方法,变成method方法调用
        #method=getattr(page,action_name)=  page       变量 action=字符串'get_url'
        #method（）获取对象method获取对象+（）
        method(**params)   #字典拆包 2个星号
                   #加了断言，直接在yaml文件里，方法和数值要对应
        time.sleep(1)

