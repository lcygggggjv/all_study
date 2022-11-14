
import unittest

def logins(usname,pwd):

    response={"message":None,"code":None,"token":None}

    if usname=="lcy" and pwd==1234:
        response["message"]="登录成功"
        response["code"]=200
        response["token"]="good"
        return response

    elif usname=="":
        response["message"] = "用户名为空"
        response["code"] = 401
        response["token"] = "bad"
        return response
    elif pwd=="":

        response["message"] = "密码为空"
        response["code"] = 401
        response["token"] = "wrong"
        return response
    else:
        response["message"] = "用户名或密码错误"
        response["code"] = 401
        response["token"] = "very bad"
        return response

