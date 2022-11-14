


#
# 尝试用 requests 对登录接口进行访问，并获取返回值，
#
# 使用不同的用户名和密码，  参考的登录账号和代码如下：

import requests

url = 'http://api.lemonban.com/futureloan/member/login'
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2"}


data1={"mobile_phone":"13556789073",
       "pwd":"00999"}

def requ(url,headers,data1,method="post"):

    res=requests.request(method=method,
                    url=url,
                     headers=headers,

                     data=data1)

    return res
# print(requ(url,headers,data1).json())


