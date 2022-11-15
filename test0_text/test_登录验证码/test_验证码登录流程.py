import base64
import json
import uuid

import requests


def gets_uid():

    return str(uuid.uuid4())


def gets_captcha(uid):

    host='http://mall.lemonban.com:8108'

    url=host+f'/captcha.jpg?uuid={uid}'  #通过拼接在url传参 ，f ’={uid}‘  通过上面获得的uuid传
    response=requests.request(method='GET',
                              url=url)

    return response.content   #图片返回的是二进制值，用content

def base64_api(uname, pwd, img_bytes, typeid):   #通过登录图鉴平台，来识别图片验证码，并返回正常的code
    # with open(img, 'rb') as f:   #这里是通过读取图片地址方式获取数据，img传img_path 图片保存的绝对地址
    # base64_data = base64.b64encode(f.read())  f.read读取
    base64_data = base64.b64encode(img_bytes)   #直接读取图片里的数据
    b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


def login(uid,code,usname,pwd):
    host = 'http://mall.lemonban.com:8108'
    url=host+'/adminLogin'   #拼接柠檬班网站

    data={
          "principal":usname,   #通过位置参数
          "credentials":pwd,
          "sessionUUID":uid,  #通过接口获得uuid
          "imageCode":code}  #通过上面接口获得code

    response=requests.request(method='post',
                              url=url,
                              json=data)

    return response.text   #登录结果用文本显示


if __name__ == '__main__':

    uid=gets_uid()   #通过函数方法获取uuid

    captcha=gets_captcha(uid)   #通过上个接口返回的uuid，传参

    code=base64_api(uname='lcy123',pwd='lcy123456789',img_bytes=captcha,typeid=3)   #通过上个接口返回的captcha验证码值输入进去，
                                                                            # 其余是图片验证平台账号密码

    res=login(uid,code,usname='student',pwd='123456a')  #通过之前接口获得的code值，和uuid，直接输入，然后输入柠檬班账号密码.
                        #关键字传参在后面，对应上面的函数也要在后面，否则报错,顺序一一对应参数！！！！

    print(res)  #最后是打印