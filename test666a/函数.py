

# def a(money):
#     print(f'你的工资多少{money}')
#     print(f'月薪{money}')
#     print('真不戳')
#     #1表示函数执行后得到的结果
#     return 1
#
# a(2000)
# a(3000)


# def a(money):
#     print(f'你的工资多少{money}')
#     print(f'月薪{money}')
#     print('真不戳')
#     #1表示函数执行后得到的结果
#     return 1  #需要打印
#
# print(a(2000))
#
# #或者用变量接收
#
# b=a(2000)
# print(b)

# #
# def add(kk):
#     a=10
#     b=5
#     c=a+b
#     if kk>10:
#         return 7
#     print('return')
# print(add(9))

#
# def bb(kk):
#     print(f'你叫什么{kk}')
#     print('名字真好听')
#     return 3
#     print('return')
# print(bb(129))


# def add(a,b):
#     c=a+b
#     print(a)
#     print(b)
#     return c
# print(add(3,4))
#
# print(add(b=4,a=3))

# price=input('数字:')
# num1=input('重量：')
#
#
# try:
#     s = float(price )*float( num1)
# except:
#     print('cuo')
from test0_text import aa

# person_info = [
#
# {
#
# "name": "明鹏程",
#
# "age": 22,
#
# "gender": "男",
#
# "hobby": "学习",
#
# "motto": "学习使我快乐"
#
# },
#
# {
#
# "name": "萌笑天",
#
# "age": 20,
#
# "gender": "女",
#
# "hobby": "拿30K offer",
#
# "motto": "下次拿个40K 的"
#
# },
#
# ]

# with open('info1.txt',mode='wt',encoding='utf-8') as e:
#     f=open('info1.txt')
#     a=person_info[0].keys()  #通过切片取值取它的key值
#     s=list(str(b)  for b in person_info[0].values())  #通过列表推导式，将这个列表里转化成字符串，形成一个新列表
#     x = list(str(b) for b in person_info[1].values())
#     e.write(f"{','.join(a)} \n")  # 通过,隔开，拼接   \n   换行
#     e.write(f"{','.join(s)} \n")
#     e.write(f"{','.join(x)} \n")

# heading=person_info[0].keys()
# s=','.join(heading)
#
# with open('info1.txt',mode='w',encoding='utf-8') as e:
#     e.write(s)
#     e.write('\n')
#     for woed in person_info:
#         for key,value in woed.items() :
#             woed[key]=str(value)
#         z=woed.values()
#         z=','.join(z)
#         z+='\n'
#         e.write(z)


# a={'kk':'12'}
# for x in range(len(a)):
#     for key,value in x.items:
#         print(key,value)


from  test0_text.aa import  eam

# def run ():
#     print('tt')
#
# run()
# aa.eam(9)
# print(aa.ia)


class buy :
    money=11  #在类下面，定义变量就是类属性，类变量

print(buy.money)

buy.money='kk'