# 题目：
#
# 定义一个类 Dog, 包含 2 个属性：名字和年龄。
#
# 定义一个方法 eat 吃东西。
#

# class  Dog:
#
#     def __init__(self,name,age,food):
#         self.name=name
#         self.age=age
#         self.food = food
#     def eat(self):
#
#         print(f'这个小狗的名字叫:{self.name},它的年龄:{self.age},喜欢吃{self.food}')
#
# y_Dog=Dog('doudou',3,'土豆')
# y_Dog.eat()

#
# class  Dog:
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eat(self,food):
#
#         print(f'这个小狗的名字叫:{self.name},它的年龄:{self.age},喜欢吃{food}')
#
# y_Dog=Dog('doudou',3)
# y_Dog.eat('土豆')



#
# 题目：定义一个登录的测试用例类LoginCase。每一个实例对象都是一个登陆测试用例。
#
# 属性：用例名称 预期结果 实际结果(初始化时不确定值哦)
#
# 方法：
#
# 运行用例
#
# 说明：有2个参数：用户名和密码。 能够登录成功的用户名：py37, 密码：666666。
#
# 通过用户名和密码正确与否来判断，是否登录成功。并返回实际结果。
#
# ps: 可以在用例内部考虑处理不符合的情况哦：密码长度不是6位/密码不正确/用户名不正确等。。
#
# 获取用例比对结果(比对预期结果和实际结果是否相等，并输出成功or失败)
#
# 实例化2个测试用例 ，并运行用例(调用方法) ，呈现用例结果(调用方法)
#
# class LoginCase:
#
#     def __init__(self,Case_name,Expected_results):
#         self.Case_name=Case_name
#         self.Expected_results=Expected_results
#         self.Actual_results=None
#
#     def run_case(self,user_name,password):
#
#         if user_name=='py37' and int(password)==666666:
#             print( '登录成功,与预期结果一致，本条用例通过')
#             self.Actual_results=True
#             return True
#         else:
#             print ('登录失败,与预期结果不一致，本条用例不通过')
#             self.Actual_results=False
#             return False
# A_LoginCase=LoginCase('用例1','登录成功')
# B_LoginCase=LoginCase('用例2','登录成功')
#
# print(A_LoginCase.run_case('py37','666666'))
# print(B_LoginCase.run_case('py388','888888'))