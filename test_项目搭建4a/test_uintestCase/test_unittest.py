

import unittest

from unittestreport import ddt,list_data

from test_项目搭建4.config.config import config

from test_项目搭建4.common.setting import logger

from test_项目搭建4.test_读取excel.test_excel import read_excels

import requests
import json

cases=read_excels(config.file_dir)    #读取用例的函数


@ddt  #数据驱动


class  test_logs(unittest.TestCase):


    @classmethod

    def setUpClass(cls) -> None:
        print("每次执行test_logs类之前运行一次")

    @classmethod

    def tearDownClass(cls) -> None:
        print("每次执行test_logs类之后运行一次")


    def setUp(self) -> None:
        print("每一次用例执行前运行一次")

    def tearDown(self) -> None:
        print("每一次用例执行后运行一次")




    @list_data(cases)  #驱动数据里的用例

    def test_01(self,item):


        logger.info("正确运行结果")
        data1=item["data"]   #取excel的每个data值

        data=json.loads(data1)   #转换成字典


        url=config.host + item["url"]   #导入配置里，固定的域名  然后拼接之后 + 用例里的剩下接口名
        response=requests.request(method=item["method"],   #发送结果
                                url=url,
                                json=data)

        try:
            actual=response.json()  #捕获异常，如果是json格式，继续，不是就text

        except Exception as e:

            actual=response.text   #用text文本格式，
            actual={"msg":actual}   #补全字典格式，不能写死，用对应的直接填写，对应改变

            # raise e
        expected=json.loads(item["expected"])  #取用例预期结果, #转换成字典

        for k,v in  expected.items():   #for循环预期结果，用key，value

            self.assertEqual(actual[k],v)  #取实际结果的key的value值，对应预期结果的value值 断言相同