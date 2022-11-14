

#登录接口
#上传图片
#上传产品

import requests

def adminlogin(usname,pwd):
    #登录

    ress=requests.request('POST',
                          url="http://mall.lemonban.com:8108/adminLogin",
                          headers={"content-type":"application/json"},
                          json={"principal":usname,
                                "credentials":pwd,
                                "imageCode":"lemon"})

    try:
        connect=ress.json()  #抛出异常

    except:
         raise ValueError(f"响应结果不是json:",ress.text)  #值异常结果，不是json格式，就返回text格式

    return connect["access_token"]  #传回token在access——token里取


def uploadimage(fspath,token):     #上传图片接口,fspath ,token变量
    # fspath=r"D:\pycharm-workspace\test9\test_uploa产品\tx_20220922002008.png"  图片不可能是json格式

     #返回值示例，2022/09/6888e87caf5d4c0b8b77ceac3f2b34ff.png
    #s上传需要token值，登录接口返回

    files={"file":open(fspath,'rb')}  #打开fspath变量文件对应rb  自动读取模式，通过二进制格式打开

    headers={'Authorization':f'bearer{token}'}  #上传的图片，token在请求头里，写成变量传参

    resz=requests.request('POST',   #请求方式
                          url="http://mall.lemonban.com:8108/admin/file/upload/img",  #地址

                          files=files,  #数据是文件的格式，变量
                          headers=headers)  #请求头

    return resz.text   #返回文本

def upload_product(token,img):  #变量

    headers = {'Authorization': f'bearer{token}'}  #上传产品也要token

    resd=requests.request('POST',
                          url="http://mall.lemonban.com:8108/prod/prod",
                          headers=headers,
                          json={"prodName":"1213","brief":"","video":"","prodNameEn":"1213","prodNameCn":"1213","contentEn":"","contentCn":"<p>13131d</p>","briefEn":"","briefCn":"311","pic":img,"imgs":img,"preSellStatus":0,"preSellTime":None,"categoryId":289,"skuList":[{"price":0.01,"oriPrice":0.01,"stocks":0,"skuScore":1,"properties":"","skuName":"","prodName":"","weight":0,"volume":0,"status":1,"prodNameCn":"1213","prodNameEn":"1213"}],"tagList":[1],"content":"","deliveryTemplateId":1,"totalStocks":0,"price":0.01,"oriPrice":0.01,"deliveryModeVo":{"hasShopDelivery":True,"hasUserPickUp":False,"hasCityDelivery":False}})      #上传产品的url地址

    return resd.text


if __name__ == '__main__':

    token=adminlogin(usname="student",pwd="123456a")  #上个登录接口，获得token值。这个接口的返回只有token
    fspath = r'D:\pycharm-workspace\test_class\test_uploa产品\tx_连接数据库.png'   #

    img=uploadimage(fspath,token)   #上传图片返回的是图片

    resf=upload_product(token,img)     #产品需要登录token，需要上个接口的图片，按照参数传

    print(resf)