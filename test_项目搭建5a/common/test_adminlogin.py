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


if __name__ == '__main__':
    token=adminlogin('student','123456a')

    print(token)
