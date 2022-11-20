

"""
关键字驱动实现
1，读取yaml当中的测试步骤

"""
import time

import pytest
import yaml
from test_web_selenium.common.basepage import BasePage


# with open('category.yaml',encoding='utf-8') as f:
#
#         steps=yaml.safe_load(f)  #，从yaml取出是字典
#
#
#
# def test_category(browser):
#
#     category=BasePage(browser)
#     # category.category_login()  不能直接调用，通过yaml，获取关键字，到对应方法里调用
#
#     for  step  in steps:
#         print(step)
#         action_name=step['action']   #这里是yaml文件对应的名称action=click或其他
#         params=step['params']  #这里是yaml数据，同上
#         method=getattr(category,action_name)  #通过getattr获取，方法里的操作
#         method(**params)  #方法有了，字典解包
#         time.sleep(2)



with open('cate_de_seach_replace.yaml',encoding='utf-8') as  f:

    cases=list(yaml.safe_load_all(f))

@pytest.mark.parametrize('steps',cases)
def test_update_clear(browser,steps):

    cate=BasePage(browser)

    for step in steps:

        action_name=step['action']
        params=step['params']

        method=getattr(cate,action_name)
        method(**params)







