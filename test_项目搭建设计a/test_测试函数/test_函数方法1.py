import unittest

import openpyxl
import unittestreport
from openpyxl.worksheet.worksheet import Worksheet


def testlogA(usname,pwd):

    reponse={"message":None,"code":None,"token":None}


    if usname=="lcy" and pwd==1234:
        reponse["message"]="登录成功"
        reponse["code"]=200
        reponse["token"]="good"
        return reponse

    elif usname=="":
        reponse["message"] = "用户名为空"
        reponse["code"] = 401
        reponse["token"] = "bad"
        return reponse

    elif pwd=="":
        reponse["message"] = "密码为空"
        reponse["code"] = 401
        reponse["token"] = "wrong"
        return reponse

    else:
        reponse["message"] = "用户名或密码错误"
        reponse["code"] = 401
        reponse["token"] = "very bad"
        return reponse

