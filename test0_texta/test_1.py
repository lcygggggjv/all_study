# def eam(s):
#
#
#
#     return s
#
# print(eam(0))
#
# ia = '12'


# class buy :
#     money=11  #在类下面，定义变量就是类属性，类变量
#
# print(buy.money)
#
# buy.money='kk'
# print(buy.money)


# class  car:
#     wheels=True
#     brand=True
#
#     def __init__(self,color):
#         print('车')
#         # print(f'品牌{logo}')
#         print(f'颜色{color}')
# #定义属性
#         # self.logo = logo
#         self.color=color


# my_car=car('小鸟','蓝')
# you_car=car('小刀','黑')
# print(car.brand)  #类属性通过类调用
# print(car('蓝色').brand)   #类属性通过对象的，要填写self定义的所有参数
#
# caer=car('蓝色')
#
# print(caer.color)   #实例属性，通过实例调用
#
# print(car.color)   #实例属性，不能通过类调用

# print(my_car.color)   #
# print(you_car.color)

#
#
# class  car:
#     wheels=True
#     brand=True
#
#     def __init__(self,color):
#         print('车')
#         # print(f'品牌{logo}')
#         print(f'颜色{color}')
# #定义属性
#         # self.logo = logo
#         self.color=color
#
#     def run(self):   #函数总是加一个self参数，实例方法
#         print('跑车')
#
#     def add_98(self,money):
#         #方法当中和函数一样，使用参数
#         print(f'加上{money}油')
#         #再实例方法中获取实例属性，就是第一个def的，参数是self.
#         print(f'我的车颜色更{self.color}')
#
#         print(self)  #打印对象本身，可以的
#
#         #调用run 方法  要加self.
#         self.run()
#
#         self.__init__('lams')   #调用第一个函数  ，加里面的要传对应参数
#
#     def fix(self):
#         print(f'正在修理{self}')  #self相当于函数参数
#
#
#     def get_wheels(self):   #通过self。获取类属性
#         print(self.wheels)
#
#     @classmethod     #声明类方法  类方法   和其他方法没有关系
#     def got_wheels(cls,ok):
#         print(cls.wheels)   #通过类方法调用cls
#         cls.ok=ok
#         print(f'这很{ok}')
#         print(cls)  #类本身
#
#     @staticmethod
#     def ge_error():  #不用加self，cls 和普通函数一样
#         print('错误')
#
#
# my_car=car('蓝色')    #my_car 都等于self

#调用实例方法，通过再方法前面加上对象的前缀 。
# my_car.run()   #调用第一个实例，没有传参
# my_car.add_98(100)   #调用第二个的实例方法，有参数，需要传参
# my_car.fix()
# my_car.get_wheels()    #类方法调用
# my_car.got_wheels('88')   #使用和实例方法一样
# my_car.ge_error()    #静态方法调用  ，可以放在类外面
#再方法当中使用实例属性

#2  我在一个函数调用另一个函数，要加self.  加函数名称

#
# class  car:
#     wheels=True
#     brand=True
#
#     def __init__(self,color):
#         print('车')
#         print(f'颜色{color}')
#
#         self.color=color
#
#     def run(self):
#         print('跑车')
#
#     def add_98(self,money):
#         #方法当中和函数一样，使用参数
#         print(f'加上{money}油')
#         #再实例方法中获取实例属性，就是第一个def的，参数是self.
#         print(f'我的车颜色更{self.color}')
#
#         print(self)  #打印对象本身，可以的
#
#         #调用run 方法  要加self.
#         self.run()
#
#         self.__init__('lams')   #调用第一个函数  ，加里面的要传对应参数
#
#     def fix(self):
#         print(f'正在修理{self}')  #self相当于函数参数
#
#
#     def get_wheels(self):   #通过self。获取类属性
#         print(self.wheels)
#
#     @classmethod     #声明类方法  类方法   和其他方法没有关系
#     def got_wheels(cls,ok):
#         print(cls.wheels)   #通过类方法调用cls
#         cls.ok=ok
#         print(f'这很{ok}')
#         print(cls)  #类本身
#
#     @staticmethod
#     def ge_error():  #不用加self，cls 和普通函数一样
#         print('错误')
#
#
# #继承   子类通过在里面写父类的car名，可以使用父类的所有方法
# class BYDcar(car):
#     pass
#
#     def adw(self):
#         print('子类自己的')    #最父级不能获得子类的方法
#
#
# # byd=BYDcar('蓝色')
# # byd.run()
#
# class aicar(BYDcar):   #孙子继承父级的，父级
#     pass
#
# zk=aicar('蓝色')
# zk.run()
# zk.adw()
#
# #多重继承  多个父类
#
# class xx(car,BYDcar,aicar):  #多个父类，使用他们的方法

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
