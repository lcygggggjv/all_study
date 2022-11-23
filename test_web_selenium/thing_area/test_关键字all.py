import time

import pytest

from test_web_selenium.common.basepage import BasePage

import yaml

with open('created_area.yaml',encoding='utf-8') as f:

    case=yaml.safe_load(f)




def test_001(area_browser):

    area=BasePage(area_browser)  #初始化浏览器

    for step  in case:  #循环

        action_name=step['action']  #取对应方法里的acttion操作
        params=step['params']

        method=getattr(area,action_name)  #通过getattr方法，前面是方法
        method(**params)  #字典解包



with open('created_area.yaml',encoding='utf-8') as f:

    cases=list(yaml.safe_load_all(f))  #转成列表




@pytest.mark.parametrize('steps',cases)   #使用pytest驱动
def test_002(area_browser,steps):

    area=BasePage(area_browser)

    for  step  in steps:

        action_name=step['action']
        params=step['params']

        method=getattr(area,action_name)
        method(**params)
        time.sleep(1)




with open('update_area.yaml',encoding='utf-8') as f:

    case_2=list(yaml.safe_load_all(f))


@pytest.mark.parametrize('steps',case_2)
def test_7(area_browser,steps):

    area=BasePage(area_browser)

    for step  in steps:

        action_name=step['action']
        params=step['params']

        method=getattr(area,action_name)

        method(**params)
        time.sleep(2)


