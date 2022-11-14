import base64
import json
import uuid

import requests


#步骤
#1生成uuid
# 2获取验证码的接口 要uuid
# 3第三方验证码平台。识别验证码
# 4登录需要的uuid  和imagcode  需要通过访问


def gets_uuid():
    #生成uuid
    return str(uuid.uuid4())  #返回是文本，要转换成字符串

def gets_captcha(uid):
    #获取验证码
    host='http://mall.lemonban.com:8108'
    url=host+f'/captcha.jpg?uuid={uid}'  #保证是同一个人登录

    response=requests.request(method='GET',
                              url=url)

    return response.content  #直接返回二进制


def base64_api(uname, pwd, img_bytes, typeid):
    #验证过程
    base64_data = base64.b64encode(img_bytes)  #直接用返回的二进制数据
    b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]   #


def login(uid,code,usname,pwd):
    host = 'http://mall.lemonban.com:8108'
    url= host+'/adminLogin'

    data={
          "principal":usname,
          "credentials":pwd,
          "sessionUUID":uid,
          "imageCode":code}

    response=requests.request('post',
                     url=url,
                     json=data)

    return response.text

if __name__ == '__main__':
    uid=gets_uuid()

    captcha=gets_captcha(uid)  #里面传的是上个结果需要的uuid

    code=base64_api(uname='lcy123',pwd='lcy123456789',  #code  是获得的图片验证码
                    img_bytes=captcha,   #上个接口获得的验证码
                    typeid=3)
    res=login(uid,code,usname='student',pwd='123456a')  #登录接口，传用户名，密码，code=上个验证码获取的，uuid

    print(res)
