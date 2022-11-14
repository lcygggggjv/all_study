
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


def read_file(filename,sheetname="Sheet1"):

    workbook=openpyxl.load_workbook(filename)   #先打开文件

    sheet:Worksheet=workbook[sheetname]   #打开sheet页

    data=list(sheet.values) #取sheet内的数据，都转换成列表


    title=data[0]
    rows=data[1:]

    data=[dict(zip(title,row))  for row in rows]     # row循环每个元组，zip函数把2个一一对应，外面用字典转换        循环就是把元组拿出来，和表头那个元组zip，然后转字典，再存到一个空列表里面

    return data

filed=r"D:\pycharm-workspace\test-框架搭建\datas\case4.xlsx"
cases=read_file(filed)

# cases=read_file(r"D:\pycharm-workspace\test-框架搭建\datas\case4.xlsx")




from unittestreport import ddt ,list_data
from loguru import logger

logger.add(sink="py78",encoding="utf-8",level="INFO")

@ddt
class testing(unittest.TestCase):
  #声明使用

    @list_data(cases)  #使用那些测试数据

    def testq(self,case):

        data1=case["data"]   #每个用例的data

        data=eval(data1)
        actual=testlogA(data["usname"],data["pwd"])  #每个用例之中的name，id。调用登录函数

        expected=case["expected"]
        expected=eval(expected)

        try:
            self.assertEqual(expected,actual)

        except AssertionError as e:
            logger.error(f"断言错误的结果{e}")
            raise    #手动抛出异常
