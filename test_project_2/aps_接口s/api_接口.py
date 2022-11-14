

from test_项目搭建2.common2.requests_访问接口 import send_requests

def logink(usname,pwd):

    url='http://httpbin.org/post'

    json_data={"name":usname,"password":pwd}


    rez=send_requests(url=url,
                      json_data=json_data,
                      method="post" )

    return rez.json()