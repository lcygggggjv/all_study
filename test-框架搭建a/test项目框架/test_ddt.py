

# import unittest
# import unittestreport
#
# sie=unittest.defaultTestLoader.discover("test9")
# # print(sie)
#
# run12=unittestreport.TestRunner(sie,
#                  title='球探报告',
#                  tester='cr7',
#                  desc="lcy的n次报告",
#                  templates=2)
#
# run12.run()

import unittest
from loguru import logger
logger.add(sink='py53',encoding='utf-8',level='INFO')

def test_case(usname,pwd):
    response={'message':None,'code':None,'token':None}
    if usname=='lcy' and pwd==123456:
        response['message']='登录成功'
        response['code']=200
        response['token']='great token'
        return response
    elif usname=='':
        response['message'] = '用户名为空'
        response['code'] = 401
        response['token'] = 'bad token'
        return response
    elif pwd=='':
        response['message'] = '密码为空'
        response['code'] = 401
        response['token'] = 'bad token'
        return response
    else:
        response['message'] = '用户名或密码错误'
        response['code'] = 401
        response['token'] = 'bad token'
        return response


# case1={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}
# case2={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}
# case3={'usname':'lcy','pwd':123456,'expected':{'message':'mm','code':201,'token':'great token'}}
# case4={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}
#
# cases=[case1,case2,case3,case4]   #用一个列表把所有用例放在一起

# 读取case3.xlsx表格数据，得到所有测试数据，保存到case变量

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

def read_dict(file,sheet_name='Sheet1'):   #形参file 默认sheet—nema

    workbook=openpyxl.load_workbook(file)  #先打开文件
    sheet:Worksheet=workbook[sheet_name]   #选择sheet页

    data=list(sheet.values)   #取sheet页里面值，转换成列表
    title=data[0]  #取第一行
    rows=data[1:]   #取从一行开始，到最后的

    data=[dict(zip(title,row))  for row in rows]  #列表推导式，循环每一个元素，用zip合并title，row，转换成字典，到新列表

    return data  #返回用例值

cases=read_dict(r"D:\pycharm-workspace\test-框架搭建\datas\case3.xlsx")#用一个cases变量接收， Windows路径表示，\n,\t,r让那些转义字符正常使用




#导入unittestreport  的ddt  和列表
from unittestreport import ddt,list_data

@ddt  #声明使用ddt数据驱动

class testlog98(unittest.TestCase):

    @list_data(cases)  #声明使用那个用例数据

    def testxx(self,case):   #case表示每次从cases取一个元素  类似for循环

        data1=case["data"]  #每个用例里的值 data的值  里有usname,和pwd
        data=eval(data1)  #取的每个用例值都是字符串，需要转换成字典
        actual=test_case(data["usname"],data["pwd"])  #从每个用例里的data  取usname ，pwd


        expected=case["expected"]   #用例的预期结果
        expected = eval(expected)   #预期结果也是字典，要转换字典

        try:
            self.assertEqual(expected,actual)  #对比两个结果
        except AssertionError as e:
            logger.error(f"错误的断言结果{e}")
            raise   #手动抛出异常
        print(actual)