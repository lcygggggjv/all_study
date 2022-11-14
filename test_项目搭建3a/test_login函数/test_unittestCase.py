

import unittest

import requests
import unittestreport

from unittestreport import ddt,list_data

from test_项目搭建3.test_读取excel.test_excel import read_book

from test_项目搭建3.config.Config import config
from test_项目搭建3.common.setting import logger
from test_项目搭建3.test_requests.test_request接口 import logings

cases=read_book(config.filename)

@ddt

class test_xx(unittest.TestCase):


    @list_data(cases)

    def test_kk(self,item):

        # logger.info("运行结果")
        data1=item["data"]  #取用例里的数据是字符串
        data=eval(data1)   #转换去掉字符串

        #发起请求
        response=requests.request(method=item["method"],
                              url=item["url"],

                              json=data
                              )
        actual=response.text  #得到响应结果

        expected=item["expected"]




        try:
            self.assertIn(expected, actual)   #单个文本校验，in  去掉eval

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