

import unittest
import unittestreport

suit=unittest.defaultTestLoader.discover(start_dir='.')  #开始目录 ..上一级目录，test2当前目录
# print(suit)
#
# result=unittest.TextTestRunner().run(suit)
# print(result)

runner=unittestreport.TestRunner(suit,filename="reports.html",
                                 title='py53期,lcy的测试报告',
                 tester='lcy',
                 desc="py53期自动化测试报告",
                templates=2)
runner.run()


# 分清哪个是类属性，哪个是实例属性。
#
#
#
# 题目1：封装一个学员类StudentStudy
#
# 属性：姓名，年龄、所在城市、期望薪资
#
# 打印所有实例属性
# #
# class StudentStudy:
#     student=True
#     name=True
#     age=True
#     salary=True
#     def __init__(self,name,age,city,salary):
#           print('柠檬班python53期自动化课程')
#           print(f'学员姓名:{name}')
#           print(f'学员年龄:{age}')
#           print(f'学员城市:{city}')
#           print(f'学员期望薪资:{salary}')
#           self.name=name
#           self.age=age
#           self.city=city
#           self.salary=salary
#
# A_StudentStudy=StudentStudy('lcy','23','杭州','15k')
# B_StudentStudy=StudentStudy('KKK','24','杭州','15k')
# print(A_StudentStudy.name,A_StudentStudy.age,A_StudentStudy.city,A_StudentStudy.salary)


# 题目2:
#
# 封装一个员工类Employee:
#
# 属性：员工姓名、工作年限、户籍城市、薪资、岗位名称
#
# 打印所有实例属性
# #
# class Employee:
#     Employee_name='kk'
#     year='yes'
#     city='yes'
#     salary='yes'
#     Postname='yes'
#     def __init__(self,name,year,city,salary,postname):
#             print('浙江杭州某不知名小公司')
#             print(f'员工姓名:{name}')
#             print(f'工作年限:{year}')
#             print(f'户籍城市:{city}')
#             print(f'薪资:{salary}')
#             print(f'岗位名称{postname}')
#
#             self.name=name
#             self.year=year
#             self.city=city
#             self.salary=salary
#             self.postname=postname
#
# A_Employee=Employee('LCY','1','安徽蒙城','8k','点点点工作者')
# print(A_Employee.name,A_Employee.year,A_Employee.city,A_Employee.salary,A_Employee.postname)
#
# print(Employee.salary)  #获取Employee类 salary 属性
#
# print(Employee(['lcy'],('12'),{'城市':'s1'},32,{'8k'}).Employee_name) #获取Employee类对象的 Employee_name属性






