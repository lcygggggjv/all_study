

import unittest

import requests
import unittestreport

from unittestreport import ddt,list_data

from test_项目搭建3.test_读取excel.test_excel import read_book

from test_项目搭建3.config.Config import config
from test_项目搭建3.common.setting import logger
from test_项目搭建3.test_requests.test_request接口 import logings

import json

cases=read_book(config.filename)

@ddt

class test_xx(unittest.TestCase):


    @list_data(cases)

    def test_kk(self,item):

        # logger.info("运行结果")
        data1=item["data"]  #取用例里的数据是字符串
        data=json.loads(data1)   #转换去掉字符串

        #发起请求
        response=requests.request(method=item["method"],
                              url=item["url"],

                              json=data
                              )

        try:
            actual=response.json()  #得到响应结果  #捕获异常，不是json格式，就运行text文本，是不变

        except Exception as e:
            actual=response.text    #用不了json，用text
            actual={"msg":actual}    #用例是text文本，所以补缺，实际结果，补成json字典  里面的是对应预期，不能写死


        expected=json.loads(item["expected"])  # 转换成字典
            #用例预期结果{”token_type':bearer]
           #实际返回一堆包含{”token_type':bearer]

        for k,v in expected.items():     #key,value  ,循环预期结果字典的元素，每一次断言取里面的键值对

            self.assertEqual(actual[k],v)  #取实际结果的同名的k。actual的key值value，和v对应预期结果的value值









        # try:
        #     self.assertIn(expected, actual)   #单个文本校验，in  去掉eval
        #
        # except AssertionError as e:
        #     logger.error(f"断言结果{e}")
        #     raise e




    # @classmethod
    # def setUpClass(cls) -> None:   #每次testxx类前运行一次
    #     print("类前")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:   ##每次testxx类后运行一次
    #     print("类后")
    # def setUp(self) -> None:   #每次用例执行之前一次
    #     print("前置")
    #
    # def tearDown(self) -> None:   #每次用例执行之后
    #     print("后置")