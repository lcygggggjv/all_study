import re
import time
import uuid

import faker
import jsonpath
import pymysql
import requests
from pymysql.cursors import DictCursor

from test_项目搭建5.common.db_connect import conect_sql
from test_项目搭建5.config.configs import config


class API:

    def get_mobile(self):
        fk = faker.Faker(locale=["zh_CN"])  # 记得加locale-=【“zh_cn
        return fk.phone_number()  # 返回随机手机号

    @classmethod  # 这里用到类本身数据，定义类方法
    def replace_data(cls, string, pattern='#(.+?)#'):
        # 数据替换
        result = re.finditer(pattern, string)

        for el in result:
            old = el.group()  # 得到老的数据
            new_name = el.group(1)

            new_ = getattr(cls, new_name)  # 到类的里面获得新的数据

            string = string.replace(old, str(new_))  # 进行数据替换 新值要是字符串
        return string

    def adminLogins(self, usname, pwd):  # 形参传用户名，密码
        """ 后台登录接口"""
        data = {
            "principal": usname,
            "credentials": pwd,
            "imageCode": 'lemon'}  # 登录数据，用户名，密码，图片验证码，这里是万能验证码

        url = config.host + '/adminLogin'  # 传url

        headers = {"content-type": "application/json"}  # 登录需要传请求接口
        res = requests.request(method='POST',
                               url=url,
                               headers=headers,
                               json=data)

        try:
            ras = res.json()  # 抛出异常 json格式向下

        except:
            raise ValueError(f'响应结果不是json:', res.text)  # 不是json格式，text文本格式

        return ras["access_token"]  # 返回取响应值的token

    def uploads_img(self, fxpath, token):  # 上传图片

        files = {'file': open(fxpath, 'rb')}  # 上传文件格式，用file ，打开文件，rb二进制格式，图片写变量，

        headers = {"Authotization": f"bearer {token}"}  # 需要上传登录接口的token
        url = config.host + '/admin/file/upload/img'
        response = requests.request('POST',  # 请求方式是post上传
                                    url=url,
                                    files=files,
                                    headers=headers)  # 通过文件类型上传

        return response.text  # 返回文本，后面会用到上面的fxpath图片变量

    def upload_product(self, img, token):
        """上传产品"""

        headers = {"Authorization": f"bearer {token}"}  # 格式化参数，对应token格式

        url = config.host + '/prod/prod'

        response = requests.request('POST',
                                    url=url,
                                    json={"prodName": "1213", "brief": "", "video": "", "prodNameEn": "1213",
                                          "prodNameCn": "1213", "contentEn": "", "contentCn": "<p>13131d</p>",
                                          "briefEn": "", "briefCn": "311", "pic": img, "imgs": img, "preSellStatus": 0,
                                          "preSellTime": None, "categoryId": 289, "skuList": [
                                            {"price": 0.01, "oriPrice": 0.01, "stocks": 0, "skuScore": 1,
                                             "properties": "", "skuName": "", "prodName": "", "weight": 0, "volume": 0,
                                             "status": 1, "prodNameCn": "1213", "prodNameEn": "1213"}], "tagList": [1],
                                          "content": "", "deliveryTemplateId": 1, "totalStocks": 0, "price": 0.01,
                                          "oriPrice": 0.01,
                                          "deliveryModeVo": {"hasShopDelivery": True, "hasUserPickUp": False,
                                                             "hasCityDelivery": False}},
                                    headers=headers)  # 这里是json=
        # 这里的data数据，抓包获取，可以直接把参数复制放在里面,要把图片变量输出，none和true，false，进行修改
        return response.text  # 直接文本打印

    # def get_sms_code(self, mobile):
    #
    #     headers = {"content-type": "application/json"}
    #
    #     response = requests.request('PUT',
    #                                 url=config.host + '/user/sendRegisterSms',
    #                                 headers=headers,
    #                                 json={"mobile": mobile})  # 注册接口需要手机号，这里是做手机号变量
    #     # 这个验证码生成在数据库，下一步连接数据库
    #
    #     time.sleep(2)  # 生成验证码写入数据库，需要时间
    #
    #     db = conect_sql(**config.db)  # 调用封装的连接数据库的类
    #
    #        #查询tz——sms -log 表  条件  手机号等于，最新一条
    #     sql = f'select mobile_code from tz_sms_log  where user_id ={mobile}  order by id  desc'  # 查找sql 通过手机号
    #
    #     result = db.query_one(sql)  # 通过db上面变量，调用query方法
    #
    #     code = result["mobile_code"]
    #
    #     db.close()  # 关闭数据库连接
    #
    #     return code  # 返回数据库查询的code

    def gets_sms_code(self,mobile):
        # 获取验证码

        ress = requests.request('PUT',
                                url=config.front_host + '/user/sendRegisterSms',
                                headers={"content-type": "application/json"},
                                json={"mobile": mobile})

        # return ress.text   #验证码在数据库，不会返回验证码这里.因为是空值所以把return
        # 关闭，写了return就不往下执行了
        # 生成验证码，接着查数据库 查tz_sms_code 表 条件 ；手机号等于多少，最新

        time.sleep(2)

        db = conect_sql(**config.db)  # config。db  传的是配置文件的数据
        sql = f'select mobile_code  from  tz_sms_log  where user_id ={mobile}  order by id  desc'  # 通过查收输入·的手机号获得验证码
        # 通过id排序取倒序
        result = db.query_one(sql)  # 这里获取的是字典
        code = result['mobile_code']  # 通过取Mobile值获得code

        db.close()  # 关闭连接
        return code  # 返回code 在数据库查询的

    def check_sms_code(self,mobile, validcode):
        "校验验证码"
        data = {"mobile": mobile, "validCode": validcode}  # 校验接口数据只要传手机号和验证码就好上面获得的
        resk = requests.request('PUT',
                                url=config.front_host + '/user/checkRegisterSms',
                                headers={"content-type": "application/json"},
                                json=data)

        return resk.text


    def user_login(self):

        #前台接口
        data={"principal":config.product_username,    #前台商城接口 登录参数
              "credentials":config.product_pwd,
              "appType":3,"loginType":0}

        res=requests.request('post',
                             url=config.front_host +'/login',  #前台接口
                             json=data,
                             headers={"content-type":"application/json"})

        try:
            rea= res.json()  # 判断json格式输出，，text文本

        except :
            raise ValueError(f'响应结果不是：json格式',res.text)
        return rea["access_token"]  #取token

    def gets_uuid(self):

        uid=str(uuid.uuid4())  #转换成字符串

        return uid



    def gets_product(self,prodId):  #可以写入形参prodid

        params='prodId=4452'   #get请求，直接用params 传在url后面
        resp=requests.request('get',  #get请求
                              url=config.front_host +'/prod/prodInfo?',  #
                              params=params,
                              )
        try:
            return resp.json()

        except:
            return resp.text

    def get_confirm(self,prodId,skuId,token):  #把商品id 和skuid uid 作为形参  token

        data={"addrId":0,
              "orderItem":{"prodId":prodId,"skuId":skuId,"prodCount":1,"shopId":1},
              "couponIds":[],"isScorePay":0,"userChangeCoupon":0,"userUseScore":0,
              "uuid":"d5eaca4a-fed2-4504-8a23-8c1a3a601a1c"}

        res=requests.request('post',
                             url=config.front_host +'/p/order/confirm',
                             json=data,
                             headers={"Authorization":f"bearer {token}"})

        try:
            return res.json()

        except:
            return res.text

    def submits(self,token):

        data={"orderShopParam":[{"remarks":"","shopId":1}],
              "uuid":"d5eaca4a-fed2-4504-8a23-8c1a3a601a1c"}

        ress=requests.request('post',
                              url=config.front_host +'/p/order/submit',
                              json=data,
                              headers={"content-type":"application/json",
                                       "Authorization":f"bearer {token}"})

        try:
            return ress.json()
        except:
            return ress.text


if __name__ == '__main__':
    api = API()

    mobile = api.get_mobile()

    # validcode = api.gets_sms_code(mobile)
    #
    # cs=api.check_sms_code(mobile,validcode)
    token=api.user_login()

    product=api.gets_product('4452')

    prodId = product["prodId"]

    # skuId = product["skuList"][0]["skuId"]

    skuId = jsonpath.jsonpath(product,'$..skuId')[0]
    # uid=api.gets_uuid()

    confirm=api.get_confirm(prodId,skuId,token)

    submits=api.submits(token)


    print(submits)  # 打印上传产品返回结果

