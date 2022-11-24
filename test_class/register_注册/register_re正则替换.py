
import json
import time

import requests
from unittestreport import ddt,list_data
import unittest

from test_class.test_正则表达式.test_封装正则表达式 import Data, replace_data
from test_project_6.common.get_mobile import get_mobile
from test_project_6.config.configs import config
from test_project_6.read_excel.read_excel1 import read_excel
from test_project_6.common.seetting import logger
from test_project_6.common.test_adminlogin import adminlogin

from test_class.register_注册.register_注册s import gets_sms_code,check_sms_code
from test_project_6.test_API.test_API import API

cases=read_excel(config.prod_file,sheetname='register')

@ddt

class test_registers(unittest.TestCase,API):  #多重继承 API 类的方法调用

    def setUp(self) -> None:
        # print(self.__dict__)
        # print(dir(self))
        #前置生成验证码
        self.__class__.mobile=self.get_mobile()  #调用api类的self调用         传入手机号.调用生成手机号函数

        #__class  设置类属性

        code=self.gets_sms_code(self.mobile)   ###通过self.调用api类的方法!!,相当于api类里面之间调用

        self.__class__.smsflag=self.check_sms_code(self.mobile,code)     #通过self.使用api类        传手机号，验证码校验

        self.__class__.username=self.__class__.mobile


            #实例属性  #这里返回的code需要转成字符串类型，

        # #设置临时变量属性
        # Data.smsflag=self.sms_flag   #实例smsflag  函数
        # Data.mobile=self.mobile
        # Data.username=self.mobile   #用户名实例，用手机号


    @list_data(cases)

    def test_register(self,item):

        data1=item['data']  #用例里获得是个是有#号

        #
        # data1=data1.replace('#smsflag#',self.sms_flag) #替换对应用例数据
        #
        # data1=data1.replace('#mobile#',self.mobile)  #替换对应用例数据
        # data1 = data1.replace('#username#', self.mobile)  #替换usname和手机号一致
        #
        data1=self.replace_data(data1)   #通过api类，self使用

        data=json.loads(data1)  #字符串转字典

        url=config.front_host+ item['url']   #注册用的是前台接口8107

        # headers={"Authorization":self.token}   #token，加上标头  authorization

        resa=requests.request(method=item['method'],
                              url=url,
                              # headers=headers, 注册不需要请求头
                              json=data)

        # print(resa.text)
        try:
            actual=resa.json()

        except Exception as e:
            actual=resa.text
            actual={"msg":actual}

        print(f'实际{actual}')
        expected=json.loads(item['expected'])  #字符串转字典
        print(f'预期{expected}')

        for k,v in  expected.items():
            self.assertIn(actual[k],v)
