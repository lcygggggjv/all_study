
import unittest
import unittestreport

def login(usname,pwd):
    response={'message':None,'code':None,'Token':None}   #先定义空的，然后符合对应条件返回内容

    if usname=='lcy123'  and  pwd==123456:
        response['message']='success'
        response['code']=200
        response['Token']='True'
        return response
    elif usname=='':
        response['message']='用户名为空'
        response['code']=400
        response['Token']='fail'
        return response
    elif pwd=='':
        response['message'] = '用户名错误'
        response['code'] = 400
        response['Token'] = 'fail'
        return response
    else:
        response['message'] = '用户名或密码错误'
        response['code'] = 400
        response['Token'] = 'fail'
        return response

#一个个调用login函数，输入参数
# print(login('lcy',123456))
# print(login('',123456))
# print(login('lcy',''))
# print(login('1233',1213324))


#每条用例输入的内容信息   要和上面的respons，返回条件一致
case1={'usname':'lcy123','pwd':123456,'expected':{'message':'success','code':200,'Token': 'True'}}
case2={'usname':'','pwd':123456,'expected':{'message':'密码为空','code':400,'Token':'fail'}}
case3={'usname':'lcy123','pwd':'','expected':{'message':'用户名为空','code':400,'Token':'fail'}}
case4={'usname':'lcy1234','pwd':1234565,'expected':{'message':'用户名或密码错误','code':400,'Token':'fail'}}

# def test_1():  #写成函数以调用
#     actual=login(case1['usname'],case1['pwd'])   #实际结果是调用login函数的case1运行的结果
#     expected=case1['expected']   #预期结果拿对应的用例里编写的预期结果
#     # if actual==expected:   #if判断预期结果和实际结果是否相等，并给出结论
#     #     print('本条用例通过')
#     # else:
#     #     print('本条用例不通过')
#     msg1=f"""expected:{expected}
#                 actual:{actual}
#         """  #assert  写出预期和实际的报错对比信息
#     assert expected==actual ,msg1
#
# def test_2():
#     actual = login(case2['usname'], case2['pwd'])
#     expected = case2['expected']
#     msg1 = f"""expected:{expected},
#                 actual:{actual}"""
#     assert expected == actual,msg1
#
# def test_3():
#     actual=login(case3['usname'],case3['pwd'])
#     expected=case3['expected']
#     msg1=f"""expected:{expected},
#                 actual:{actual}"""
#     assert expected==actual,msg1
#
# def test_4():
#     actual=login(case4['usname'],case4['pwd'])
#     expected = case3['expected']
#     msg1 = f"""expected:{expected},
#                  actual:{actual}"""
#     assert expected == actual, msg1

#一个个调用测试的函数
# test_1()
# test_2()
# test_3()
# test_4()


class Testlogin(unittest.TestCase):   #TestLoin类，继承unittest.TestCase

    def test_login1(self):   #定义一个实例方法，和上面不一样，上面是类
        actual=login(case1['usname'],case1['pwd'])   #方法里面调用login函数  输入对应用例内容
        expected=case1['expected']  #取用例1的预期结果

        self.assertEqual(expected,actual)  #智能提示  报错信息

    def test_login2(self):
        actual = login(case2['usname'], case2['pwd'])
        expected = case2['expected']

        self.assertEqual(expected, actual)

    def test_login3(self):
        actual = login(case3['usname'], case3['pwd'])
        expected = case3['expected']

        self.assertEqual(expected, actual)

    def test_login4(self):
        actual = login(case4['usname'], case4['pwd'])
        expected = case4['expected']

        self.assertEqual(expected, actual)

