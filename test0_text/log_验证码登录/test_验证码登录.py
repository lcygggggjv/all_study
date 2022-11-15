import base64
import json
import uuid

import requests


def gets_uid():

    return str(uuid.uuid4())

def get_captcha(uid):

    host='http://mall.lemonban.com:8108'
    url=host+f'/captcha.jpg?uuid={uid}'

    response=requests.request(method='GET',
                              url=url)

    return response.content

def base64_api(uname, pwd, img_bytes, typeid):
    # with open(img, 'rb') as f:
    base64_data = base64.b64encode(img_bytes)
    b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


def login(uid,code,usname,pwd):

    host='http://mall.lemonban.com:8108'

    url=host+'/adminLogin'

    data={
  "principal": usname,
  "credentials": pwd,
  "sessionUUID": uid,
  "imageCode": code
}
    response=requests.request(method='post',
                              url=url,
                              json=data)

    return response.text



if __name__ == '__main__':

    uid=gets_uid()

    captcha=get_captcha(uid)

    code=base64_api(uname='lcy123',pwd='lcy123456789',img_bytes=captcha,typeid=3)

    res=login(uid,code,usname='student',pwd='123456a')

    print(res)


