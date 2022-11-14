

import requests


def logings(headers,):
    url='http: // mall.lemonban.com: 8108 / adminLogin'

    data={

    "principal": "student",

    "credentials": "123456a",

    "imageCode": "lemon"
}

    res=requests.request(method="post",
                         url=url,
                         headers=headers,
                         json=data)
    return res

logings()