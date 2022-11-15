import json

import requests
from unittestreport import ddt,list_data
import unittest

from test_项目搭建5.config.configs import config
from test_项目搭建5.read_excel.read_excel1 import read_excel
from test_项目搭建5.common.seetting import logger
from test_项目搭建5.common.test_adminlogin import adminlogin

cases=read_excel(config.product,sheetname='product')

@ddt

class test_product(unittest.TestCase):

    def setUp(self) -> None:
        token=adminlogin(config.prod_usname,config.prod_pwd)

        # print(token)
        self.token=token
    @list_data(cases)
    def test_addproduct(self,item):

        data1=item['data']
        data=json.loads(data1)
        url=config.host+item["url"]
        headers={"Authorization":f"bearer{self.token}"}   #token，加上标头  authorization
        resa=requests.request(method=item['method'],
                              url=url,   #url=item['url']
                              json=data,
                              headers=headers)
        # print(resa.json())
        try:
            actual=resa.json()

        except Exception as e:
            actual=resa.text
            actual={"msg":actual}
        print(f'实际:{actual}')

        expected=json.loads(item['expected'])
        print(f'预期:{expected}')
        for k,v in  expected.items():
            self.assertEqual(actual[k],v)
