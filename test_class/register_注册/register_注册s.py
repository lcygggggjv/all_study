import time

import requests

from test_project_6.common.get_mobile import get_mobile
from test_project_6.config.configs import config
from test_project_6.common.db_connect import conect_sql


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



def gets_sms_code(mobile):
    #获取验证码

    ress=requests.request('PUT',
                          url=config.front_host +'/user/sendRegisterSms',
                          headers={"content-type":"application/json"},
                          json={"mobile":mobile})

    # return ress.text   #验证码在数据库，不会返回验证码这里.因为是空值所以把return
                                #关闭，写了return就不往下执行了
        #生成验证码，接着查数据库 查tz_sms_code 表 条件 ；手机号等于多少，最新


    time.sleep(2)

    db=conect_sql(**config.db)   #config。db  传的是配置文件的数据
    sql=f'select mobile_code  from  tz_sms_log  where user_id ={mobile}  order by id  desc'  #通过查收输入·的手机号获得验证码
                                                                    #通过id排序取倒序
    result=db.query_one(sql)  #这里获取的是字典
    code=result['mobile_code']  #通过取Mobile值获得code

    db.close()  #关闭连接
    return code  #返回code 在数据库查询的

def check_sms_code(mobile,validcode):
    "校验验证码"
    data={"mobile":mobile,"validCode":validcode}   #校验接口数据只要传手机号和验证码就好上面获得的
    resk = requests.request('PUT',
                            url=config.front_host + '/user/checkRegisterSms',
                            headers={"content-type": "application/json"},
                            json=data)

    return resk.text

if __name__ == '__main__':
    mobile=get_mobile()   #
    validcode=gets_sms_code(mobile)  #到获得验证码的接口传手机号变量。获得验证码

    ss=check_sms_code(mobile,validcode)   ##校验，传手机号，和上面获得的验证码
    print(ss)