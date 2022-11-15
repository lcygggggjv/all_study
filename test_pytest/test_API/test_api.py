import json
import re
import time

import faker
import jsonpath
import openpyxl
import pymysql
import requests
from openpyxl.worksheet.worksheet import Worksheet
from pymysql.cursors import DictCursor

from test_pytest.Config.config import Config
import base64
import uuid

class data:
    smsflag = 'cookie'
    mobile = '18355936526'
    username = 'kds'






def replace_data(string,parten='#(.+?)#'):

    result=re.finditer(parten,string)

    for el  in  result:

        old=el.group()  #获取老的数据

        new=el.group(1)

        news=getattr(data,new)  #使用getattr 获取类的属性

        string=string.replace(old,str(news))

    return string


if __name__ == '__main__':

    res=replace_data('{"name":"#smsflag#","age":"12","mobile":"#mobile#"}')

    print(res)










def read_excel(filename,sheetname):   #读取excel，读取数据为字符串

    workbook=openpyxl.load_workbook(filename)

    sheet:Worksheet =workbook[sheetname]

    data=list(sheet.values)   #sheet里取值,并转换成列表

    title=data[0]  #取第一行数据
    rows=data[1:]  #取第一行之后的值


    data=[dict(zip(title,row)) for row  in  rows]   #列表推导式  先用row循环每个rows  和表头进行一一压缩拼接成字典，最后外面是列表

    return data


def get_uuid():  #获取uuid

    uid=uuid.uuid4()   #导入uuid4方法 直接获取

    return str(uid)   #uuid返回值需要转换字符串


def get_captcha(uid):   #获取图片

    res=requests.request(method='get',
                         url=Config.host+f'/captcha.jpg?uuid={uid}'    #格式化输出，直接通过url传入uuid
                         )

    return res.content

def  base64_api(usname,pwd,typeid,img,):  #上传图片鉴别平台  名称和密码，图片以及 类别id

    # with open(img, 'rb') as f:
    base64_data = base64.b64encode(img)   #拿别人封装函数
    b64 = base64_data.decode()
    data = {"username": usname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


def longin(uid,code,username,pwd):   #验证码登录接口
    #放到data里 传参
    data={"principal":username,
          "credentials":pwd,
          "sessionUUID":uid,
          "imageCode":code}

    res=requests.request(method='post',
                         url=Config.host+'/adminLogin',
                         json=data)

    return res.text


class connect_sql:


    def __init__(self,user=None,password=None,host=None,port=None,db=None,**kwargs):   #使用关键字传参，默认值为none

        #s实例connect属性，下面的函数直接调用实例即可    字典解包  **config.db  ，定义的参数名一一对应，名称
        self.connect=pymysql.connect(user=user,
                                   password=password,
                                    host=host,
                                    port=port,
                                    cursorclass=DictCursor,  #导入dictcursor类 ,默认元组，搞成字典
                                    db=db)


    def query_one(self,sql):

        cursor=self.connect.cursor()  #初始化游标

        self.connect.commit()  #提交一次事务

        cursor.execute(sql)   #使用execute方法，传入sql

        result_one=cursor.fetchone()  #查迅单个 结果

        cursor.close()  #关闭链接

        return result_one   #返回值

    def query_all(self,sql):

        cursor=self.connect.cursor()

        self.connect.commit()

        cursor.execute(sql)

        result_all=cursor.fetchall()

        cursor.close()

        return result_all


    def close(self):

        self.connect.close()   #实例的connect 属性关闭



def adminlogin(usname,pwd):



    res=requests.request('post',
                         url=Config.host+'/adminLogin',
                         headers={"content-type":"application/json"},
                         json={"principal":usname,
                            "credentials":pwd,
                            "imageCode":"lemon"})  #万能验证码

    try:
        ress=res.json()

    except:
        raise ValueError("返回结果不是：json",res.text)

    return ress["access_token"]  #取token


def upload_img(fxpath,token):   #传参  图片文件 ，登录的token

    file={"file":open(fxpath,'rb')  }   #打开fxpath文件 形参，rb模式

    res=requests.request('post',
                         url=Config.host+'/admin/file/upload/img',
                         headers={"Authorization":f"bearer {token}"},
                         files=file)  #文件传用files
    return res.text


def updload_product(img,token):

    # data里的图片需要改成形参，以及none 布尔值修改
    res=requests.request('post',
                         url=Config.host+'/prod/prod',
                         headers={"Authorization":f"bearer {token}"},
                         json={"prodName":"1213","brief":"","video":"","prodNameEn":"1213","prodNameCn":"1213","contentEn":"","contentCn":"<p>13131d</p>","briefEn":"","briefCn":"311","pic":img,"imgs":img,"preSellStatus":0,"preSellTime":None,"categoryId":289,"skuList":[{"price":0.01,"oriPrice":0.01,"stocks":0,"skuScore":1,"properties":"","skuName":"","prodName":"","weight":0,"volume":0,"status":1,"prodNameCn":"1213","prodNameEn":"1213"}],"tagList":[1],"content":"","deliveryTemplateId":1,"totalStocks":0,"price":0.01,"oriPrice":0.01,"deliveryModeVo":{"hasShopDelivery":True,"hasUserPickUp":False,"hasCityDelivery":False}})
    #{"prodName":"XIN","brief":"","video":"","prodNameEn":"XIN","prodNameCn":"XIN","contentEn":"","contentCn":"<p>DWQW21</p>","briefEn":"","briefCn":"D","pic":img,"imgs":img,"preSellStatus":0,"preSellTime":None,"categoryId":289,"skuList":[{"price":0.01,"oriPrice":0.01,"stocks":10000,"skuScore":1,"properties":"颜色:金色","skuName":"金色 ","prodName":"XIN 金色 ","weight":0,"volume":0,"status":1,"propertiesEn":"Color:golden","skuNameEn":"golden ","prodNameCn":"XIN 金色 ","prodNameEn":" golden ","pic":img,"partyCode":"122345678"}],"tagList":[1],"content":"","deliveryTemplateId":1,"totalStocks":10000,"price":0.01,"oriPrice":0.01,"deliveryModeVo":{"hasShopDelivery":True,"hasUserPickUp":False,"hasCityDelivery":False}}
    return res.text



def get_mobile():


    fk=faker.Faker(locale=['zh_CN'])   #注意改成中国的

    return fk.phone_number()


def get_sms_code(mobile):   #获取验证码,输入手机号


    res=requests.request('PUT',
                         url=Config.front_host+'/user/sendRegisterSms',
                         json={"mobile":mobile})  #抓包抓的参数格式

    #不需要打印返回值

    time.sleep(3)  #提交数据库里等待一下

    db=connect_sql(**Config.db)  #实例类，传输入参数，字典解包

    sql=f'select  mobile_code  from  tz_sms_log  where  user_id={mobile} order by  id  desc'  #通过传入的手机号，查询tz_sms_log表里的code  通过id降序

    result_one=db.query_one(sql)  #通过实例的 属性 传入sql

    code=result_one['mobile_code']  # result获得值为字典 {'mobile_code': '131494'} 通过字典取mobile 取code值

    db.close()  #关闭

    return code  #返回结果


def check_smscode(mobile,validcode):


    res=requests.request('PUT',
                         url=Config.front_host+'/user/checkRegisterSms',
                         json={"mobile":mobile,"validCode":validcode})  #传参格式

    return res.text



def front_login(usname,pwd):

    res=requests.request('post',
                         url=Config.front_host+'/login',
                         json={"principal":usname,
                               "credentials":pwd,
                               "appType":3,"loginType":0})

    try:
        rss=res.json()

    except:
        raise ValueError(f"响应结果不是：json",res.text)

    return rss["access_token"]


def get_prodinfo(prodid):

    params="prodId=4748"  #通过params传到url地址后面

    res=requests.request('GET',
                         url=Config.front_host+'/prod/prodInfo?',
                         params=params)

    try:
        return res.json()
    except:
        return res.text

def get_confirm(prodid,skuid,token):  #需要传入商品id

    res=requests.request('post',
                         url=Config.front_host+'/p/order/confirm',
                         json={"addrId":0,"orderItem":{"prodId":prodid,"skuId":skuid,"prodCount":1,"shopId":1},
                               "couponIds":[],"isScorePay":0,"userChangeCoupon":0,
                               "userUseScore":0,"uuid":"b0877682-4f5a-47a5-a7a4-2f0c179f371b"},
                         headers={"Authorization":f"bearer {token}"})

    try:
        return res.json()

    except:
        return res.text


def submit(token):

    resa=requests.request('post',
                          url=Config.front_host+'/p/order/submit',
                          headers={"Authorization":f"bearer {token}"},
                          json={"orderShopParam":[{"remarks":"","shopId":1}],
                                "uuid":"b0877682-4f5a-47a5-a7a4-2f0c179f371b"})

    try:
        return resa.json()
    except:
        return resa.text



if __name__ == '__main__':

    # cases=read_excel(Config.login_dir,'adminLogin')
    # uid=get_uuid()
    #
    # cpatcha=get_captcha(uid)
    #
    # code=base64_api(usname='lcy123',pwd='lcy123456789',typeid=3,img=cpatcha)
    #
    # ress=longin(uid,code,username=Config.host_usname,pwd=Config.host_pwd)

    # ap=connect_sql(**Config.db)  #实例类,传入形参，关键字参数  使用字典解包
    #
    # sql=f'select user_id, mobile_code from  tz_sms_log  limit  2'
    # sql_ones=ap.query_one(Config.sql)

    # token=adminlogin(Config.host_usname,Config.host_pwd)
    #
    # img=upload_img(Config.fxpath,token)
    #
    #
    # res=updload_product(img,token)


    # mobile=get_mobile()
    #
    # code=get_sms_code(mobile)
    #
    # cs=check_smscode(mobile,code)

    token=front_login(Config.front_usname,Config.front_pwd)

    #{"shopId":1,"shopName":null,"prodId":4748,"prodName":"12313","price":0.01,"content":"<p>133345</p>","oriPrice":0.01,"waterSoldNum":0,"totalStocks":1110,"brief":"1313","video":"","pic":"http://mall.lemonban.com:8108/2022/10/f4d95814dad048a79ee01e0b2826eb0d.jpg","imgs":"http://mall.lemonban.com:8108/2022/10/f4d95814dad048a79ee01e0b2826eb0d.jpg","categoryId":289,"prodType":0,"scorePrice":null,"liveRoomParams":[],"skuList":[{"skuId":12018,"price":0.01,"oriPrice":0.01,"stocks":1110,"skuName":"金色 ","skuScore":1,"pic":null,"properties":"颜色:金色"}],"groupActivityId":0,"activityPrice":null,"startDeliveryFee":null,"deliveryModeVO":{"hasUserPickUp":false,"hasShopDelivery":true,"hasCityDelivery":false},"preSellStatus":0,"preSellTime":null}

    product=get_prodinfo('4748')

    prodid=product["prodId"] #直接取product里 prodid

    print(prodid)
    skuid=jsonpath.jsonpath(product,'$..skuId')[0]   #取第一个

    print(skuid)

    asd=get_confirm(prodid,skuid,token)

    sub=submit(token)

    print(sub)