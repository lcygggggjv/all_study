import json
import unittest

import jsonpath
import requests
from unittestreport import ddt,list_data

from test_项目搭建5.test_API.test_API import API

from test_项目搭建5.read_excel.read_excel1 import read_excel
from test_项目搭建5.config.configs import config

cases=read_excel(config.pay,sheetname='pay')

@ddt
class test_pay(unittest.TestCase,API):

    # 登录接口 login  前台

    def setUp(self) -> None:

        #1 获取登录的token
        token=self.user_login()

        self.token=token  #实例token属性，方便下面用方法

        # print(token)

        #2 获取商品信息 商品id  和skuid

        product=self.gets_product('4452')

        # print(product)
        prodid=product["prodId"]

        skuid=product["skuList"][0]["skuId"]   #取嵌套字典 skulist值，第一个位置，取skuid

        # skuid=jsonpath.jsonpath(product,'$..skuId')[0]   # jsonpath  前面是变量值，取值  。 下一层级  。。 所有子孙值 如果有2个一样，索引

        #3获取商品信息
        confirm=self.get_confirm(prodid,skuid,token)

        # 4 提交商品

        submits=self.submits(token)

        self.__class__.orderId=submits['orderNumbers']  #获取订单号 实例
            #设置类属性  替换与用例里数据一致 orderId

    @list_data(cases)
    def test_pays(self,item):    #每个用例变量
        #下单接口
        #测试数据处理
        #json数据  里面 #  占位符要替换
        json_data=item['json']
        json_data=self.replace_data(json_data)  #替换的是类方法调用，替换  一次性

        json_dict=json.loads(json_data)  #转成字典类型

        #获取headers数据

        headers={"Authorization":f"bearer {self.token}"}  #获取上面实例token属性


        res=requests.request(method=item['method'],
                             url=config.front_host +item['url'],
                             json=json_dict,  #转换成字典的值
                             headers=headers)  #从用例中获取方法
        try:
            actual= res.json()

        except Exception as e:
            actual=res.text
            actual={"msg":actual}

        expected=item['expected']  #取用例里的预期结果

        expected=json.loads(expected)  #转换成字符串

        for k ,v  in  expected.items():  #for循环取预期结果里的，key 和value

            self.assertEqual(actual[k],v)  #断言  实际结果的值和预期结果的值