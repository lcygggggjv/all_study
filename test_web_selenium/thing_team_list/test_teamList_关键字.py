import time

import pytest
import yaml

from test_web_selenium.common.basepage import BasePage


# with open('team_list.yaml',encoding='utf-8') as f:
#
#     cases=yaml.safe_load(f)
#
#
#
# def test_001(browser):
#
#     team=BasePage(browser)
#
#     for step  in  cases:
#
#         action_name=step['action']
#         params=step['params']
#
#         method=getattr(team,action_name)
#         method(**params)


with open('team_list.yaml',encoding='utf-8') as f:

    cases=list(yaml.safe_load_all(f))


@pytest.mark.parametrize('steps',cases)
def test_02(browser,steps):

    team=BasePage(browser)

    for step  in steps:
        action_name=step['action']
        params=step['params']

        method=getattr(team,action_name)   #先得到对应的方法  getattr(action,'action=click') =action，click的方法
         #  等于baseage里的click方法，method获取click的方法
        method(**params)  #再用函数加括号（）调用  再对应方法里需要的参数，params **字典解包
        time.sleep(1)