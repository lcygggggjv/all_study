

import requests

ses=requests.session()

def logings(principal,credentials,imageCode):

    headers={"content-type": "application/json"}

    url="http://mall.lemonban.com:8108/adminLogin"

    data={"principal":principal,
          "credentials":credentials,
          "imageCode":imageCode}

    res=ses.request(method="post",
                         url=url,
                         headers=headers,
                        json=data)

    return res