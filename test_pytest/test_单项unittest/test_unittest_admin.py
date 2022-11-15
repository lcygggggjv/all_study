import json
import unittest

import requests
from unittestreport import list_data,ddt
from test_pytest.Config.config import Config
from test_pytest.test_API.test_api import read_excel
from test_pytest.setting.loginfo import logger


#获取用例 导入read——excel

cases=read_excel(Config.test_dir,'adminLogin')  #读取用例


#使用ddt

@ddt

class test_login(unittest.TestCase):   #继承unittest方法

    @classmethod

    def setUpClass(self) -> None:
        print("每次执行类前，执行用例一次")

    @classmethod
    def tearDownClass(cls) -> None:

        print("每执行类后。执行用例一次")

    def setUp(cls) -> None:
        print('没执行一次方法前，执行用例一次')



    def tearDown(self) -> None:

        print("每执行一次方法后，执行用例一次")

    @list_data(cases)  #数据驱动，获取里面的用例

    def test_001(self,item):   #item是里面的每个用例


        logger.info("运行结果")
        print(type(item))
        data1=item['json']  #取用例的json的值

        data=json.loads(data1)  #转成字典


        res=requests.request('post',
                             url=Config.host+'/adminLogin',
                             json=data,
                             headers={"content-type":"application/json"})

        try:
            actual=res.json()  #异常处理。是json，跳过。不是继续执行下面

        except Exception as e:

            actual=res.text
            actual={"msg":actual}  #补成字典

        expected=json.loads(item['expected'])  #通过json；load转字典。取用例里的预期的值

        for k,v in expected.items():   # 取预期结果，值，for循环，取key，value值

            self.assertEqual(actual[k],v)  #断言。实际结果取key，实际的值，等于预期结果的值
