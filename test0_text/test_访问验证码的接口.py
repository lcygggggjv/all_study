


import uuid

import requests

uid=uuid.uuid4()

url='http://mall.lemonban.com:8108/captcha.jpg'

params={'uuid':uid}
response=requests.request('get',
                 url=url,
                params=params)

# print(response.content)  #图片是二进制用content

#直接用wb 模式写入

with open('dao.png','wb')as f:

    f.write(response.content)