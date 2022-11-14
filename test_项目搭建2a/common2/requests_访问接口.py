

import requests


url = 'http://api.lemonban.com/futureloan/member/login'
json_data = {'name': 'usname', 'password': 'pwd'}



def send_requests(url,json_data,method=None):

    res=requests.request(method=method,
                url=url,
                json=json_data,
                )

    return res

print(send_requests(url,json_data,method='post').json())