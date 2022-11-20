import time

import pytest
import yaml
from test_web_selenium.common.basepage import BasePage

# with open('category_created.yaml',encoding='utf-8') as f:
#
#     cases=list(yaml.safe_load_all(f))   #读取多个用例，转换成列表，类似于list——data
#
#
#
# @pytest.mark.parametrize('steps',cases)  #对应循环的名称
# def test_category2(browser,steps):
#
#     category=BasePage(browser)
#
#     for step  in   steps:   #这里的steps要对应，上面的字符串名称
#
#         action_name=step['action']
#
#         params=step['params']
#
#         method=getattr(category,action_name)
#
#         method(**params)
#         time.sleep(1)




with open('category_update.yaml',encoding='utf-8') as f:

    cases=list(yaml.safe_load_all(f))


@pytest.mark.parametrize('steps',cases)
def test_update(browser,steps):

    cate=BasePage(browser)

    for  step  in steps:

        action_name=step['action']

        params=step['params']

        method=getattr(cate,action_name)

        method(**params)  #传入数据
        time.sleep(1)








