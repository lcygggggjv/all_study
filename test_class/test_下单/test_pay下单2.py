import json
import unittest

import jsonpath
import requests
from unittestreport import ddt,list_data

from test_项目搭建5.test_API.test_API import API

from test_项目搭建5.read_excel.read_excel1 import read_excel
from test_项目搭建5.config.configs import config

cases=read_excel(config.pay,sheetname='order_flow')

@ddt
class test_pay(unittest.TestCase,API):


    @list_data(cases)
    def test_pay(self,item):    #每个用例变量
        #下单接口
        #  json测试数据处理
        #json数据  里面 #  占位符要替换
        json_data=item['json']
        json_data=self.replace_data(json_data)  #替换的是类方法调用，替换  一次性

        json_dict=json.loads(json_data)  #转成字典类型

        #请求头处理

        headers=item['headers']  #获取用例的请求头

        if headers:     #如果没有请求头，直接跳过，有请求头，就进行替换
            headers = self.replace_data(headers)  # 替换的是类方法调用，替换  一次性

            headers = json.loads(headers)



        res=requests.request(method=item['method'],
                             url=config.front_host +item['url'],
                             json=json_dict,  #转换成字典的值
                             headers=headers)  #从用例中获取方法

        try:
            content=res.json()
        except:
               content={"msg":res.text}

        #数据提取
        #设置一个变量保存access——token 的值，然后传递第二个用例取使用

        #获取用例写的extract——token

        extract_data=item['extract_data']

        if extract_data:

            extract_data=json.loads(extract_data)

            for prop_name,jsonpath_expr  in extract_data.items():
                #{"access_token":"$..access_token"}  access_token==prop_name

                #value==获取到的token
                value=jsonpath.jsonpath(content,jsonpath_expr)[0]   #jsonpath 表达式。content是文件，后面是取得字段名

                #设置类属性 保存token  传到下个接口
                #设置 类当中的accesstoken属性  ，propnametoken

                setattr(API,prop_name,value)   #设置类属性 不需要加字符串。 和  API.ACCESS_TOKEN=VALUE
                # api类  prop_name—— 属性  value 属性值




        # try:
        #     actual= res.json()
        #
        # except Exception as e:
        #     actual=res.text
        #     actual={"msg":actual}
        #
        # expected=item['expected']  #取用例里的预期结果
        #
        # expected=json.loads(expected)  #转换成字符串
        #
        # for k ,v  in  expected.items():  #for循环取预期结果里的，key 和value
        #
        #     self.assertEqual(actual[k],v)  #断言  实际结果的值和预期结果的值