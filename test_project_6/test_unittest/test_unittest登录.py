import json
import unittest

import requests
import unittestreport

from test_project_6.config.configs import config
from test_project_6.read_excel.read_excel1 import read_excel
from test_project_6.common.seetting import logger
from unittestreport import ddt,list_data


cases=read_excel(config.excel_file)  #先导入文件，读取数据

@ddt       #数据驱动

class testlog(unittest.TestCase):   #继承unittest。testcase类

    @classmethod

    def setUpClass(cls) -> None:
        print("每次运行testlog类前，执行一次用例")

    @classmethod

    def tearDownClass(cls) -> None:
        print("每次运行testlog类后，执行一次用例")

    def setUp(self) -> None:
        print("每次运行一次函数前，执行一次用例")

    def tearDown(self) -> None:
        print("每次运行一次函数后，执行一次用例")

    @list_data(cases)  #数据驱动，获取里面的数据

    def test_loginY(self,item):   #item是cases里每一个用例


        logger.info("运行结果")
        data1=item['data']    #取item里的data  请求参数

        data=json.loads(data1)   #利用json。loads  转换成字典

        url='http://mall.lemonban.com:8108/adminLogin'   #登录地址


        response=requests.request(method='post',   #使用requests方法登录，传请求方法，url地址，输出格式
                                  url=url,
                                  json=data)

        try:
            actual=response.json()   #使用捕获异常；如果上面的请求返回值是json格式，正确

        except Exception as e:

            actual=response.text   #如果返回不是json格式，则使用text格式
            actual={"msg":actual}   #因为这里返回的是一串字符串，所以补成字典格式，方便和用例的预期结果对比

        expected=json.loads(item['expected'])  #用json。loads方法转成字典格式，item里取的是expected，不是data

        for k,v in expected.items():  #使用for循环，取预期结果的key，value，

            self.assertEqual(actual[k],v)  #使用self。assertequal断言相同 ；实际结果取所有的key的value值，对比预期结果的所有value值


