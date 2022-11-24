
import json
import time

import requests
from unittestreport import ddt,list_data
import unittest

from test_project_6.common.get_mobile import get_mobile
from test_project_6.config.configs import config
from test_project_6.read_excel.read_excel1 import read_excel
from test_project_6.common.seetting import logger
from test_project_6.common.test_adminlogin import adminlogin

from test_class.register_注册.register_注册s import gets_sms_code,check_sms_code

from test_class.test_正则表达式.test_封装正则表达式 import replace_data,Data
   #使用两个，要有类的
cases=read_excel(config.prod_file,sheetname='register')

@ddt

class test_register(unittest.TestCase):

    def setUp(self) -> None:
        #前置生成验证码
        self.mobile='15675500781'  #传入手机号.调用生成手机号函数

        code=gets_sms_code(self.mobile)  #获得验证  码

        self.sms_flag=str(check_sms_code(self.mobile,code))     #传手机号，验证码校验
            #实例属性  #这里返回的code需要转成字符串类型，

        # Data.smsflag=self.sms_flag
        #
        # Data.mobile=self.mobile
        #
        # Data.username=self.mobile

    @list_data(cases)

    def test_register(self,item):

        data1=item['data']  #用例里获得是个是有#号

        data1=data1.replace('#smsflag#',self.sms_flag) #替换对应用例数据

        data1=data1.replace('#mobile#',self.mobile)  #替换对应用例数据
        data1 = data1.replace('#username#', self.mobile)  #替换usname和手机号一致
        data=json.loads(data1)  #字符串转字典


        url=config.front_host+ item['url']   #注册用的是前台接口8107

        # headers={"Authorization":self.token}   #token，加上标头  authorization

        resa=requests.request(method=item['method'],
                              url=url,
                              # headers=headers, 注册不需要请求头
                              json=data)

        print(resa.text)
        # try:
        #     actual=resa.json()
        #
        # except Exception as e:
        #
        #     actual=resa.text
        #     # actual={"msg":actual}
        # print(f'实际{actual}')
        # expected=json.loads(item['expected'])
        # print(f'预期{expected}')
