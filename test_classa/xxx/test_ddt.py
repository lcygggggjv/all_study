

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
        response['token'] = 'bad2 token'
        return response


case1={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}
case2={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}
case3={'usname':'lcy','pwd':123456,'expected':{'message':'mm','code':201,'token':'great token'}}
case4={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}

cases=[case1,case2,case3,case4]   #用一个列表把所有用例放在一起

#导入unittestreport  的ddt  和列表
from unittestreport import ddt,list_data

@ddt  #声明使用ddt数据驱动

class testlog98(unittest.TestCase):

    @list_data(cases)  #声明使用那个用例数据

    def testxx(self,case):   #case表示每次从cases取一个元素  类似for循环
        actual=test_case(case["usname"],case["pwd"])   #调用上面函数的，用例每个name，pwd

        expected=case["expected"]   #用例的预期结果
        try:
            self.assertEqual(expected,actual)  #对比两个结果
        except AssertionError as e:
            logger.error(f"错误的断言结果{e}")
            raise   #手动抛出异常
        print(actual)