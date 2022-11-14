

import unittest

import requests
import unittestreport

from unittestreport import ddt,list_data

from test_项目搭建3.test_读取excel.test_excel import read_book

from test_项目搭建3.config.Config import config
from test_项目搭建3.common.setting import logger
from test_项目搭建3.test_requests.test_request接口 import logings

cases=read_book(config.filename)

# print(cases)
class test_xx(unittest.TestCase):

    def test_k1(self):

        # logger.info("运行结果")
        data1=cases[0]["data"]  #取用例里的数据是字符串
        data=eval(data1)   #转换去掉字符串


        #发起请求
        response=requests.request(method=cases[0]["method"],
                              url=cases[0]["url"],

                              json=data
                              )
        actual=response.json()  #得到响应结果

        expected=cases[0]["expected"]
        expected=eval(expected)

        try:
            self.assertEqual(expected, actual)

        except AssertionError as e:
            logger.error(f"断言结果{e}")
            raise e








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