# from selenium import webdriver
# driver =  webdriver.Chrome()
# driver.get("https://blog.csdn.net/weixin_47935594/article/details/121527300")
# driver.maximize_window()
#
# age=int(input('ta:'))
# if age>18:
#     print('年轻')
# elif age>15:
#     print('lao')
# else:
#     print('nian')
#
# d='123'
# for a in d:
#     print(a)
#
# for a in range(1,21,2):
#     print(a)

# str='1','2','sr','ter'
# print(str[2])
#
# str='w','2','3','33','od'
# print(str[1:3:1])

# str='12','2','de','3w'
# print(str[::-1])
#
# str='d','e','eea','ad'
# print(str[2::])

# ade=int(input('请输入年龄:'))
# if ade>40:
#     print('年轻')
# elif ade>30:
#     print('中年人')
# else:
#     print('yong')

# ste='30','we'
# for a in ste:
#     print(a)

# for a in range(1,23,1):
#     print(a)
#

# str='sddjfj3kma'
# str=str.replace('sddjfj3kma','uu')
# print(str)

# str='我都大大是的d'
# print(str.index('大大'))
# str='我是大帅哥'
# print(str.find('帅哥'))


# phone='vivo'
# city='杭州'
# work='测试'
#
#
# print(""" ---------{}同学基本信息---------
# sj:{}
# 城市:{}
# 工作:{}
#
# """.format(phone,phone,city,work))

#
# 姓名:'李春雨'
# 年龄:'24'
# 城市:'杭州'
#
# print("""--------{0}帅哥的基本信息------------
# name:{0}
# age:{1}
# city:{2}
#
#
#
# """.format('姓名','姓名','年龄','城市'))

# sys=input("你认为我是大帅哥吗？:")
# if sys=='True':
#     print('是的！')
# elif sys=='False':
#     print('必须是！')
# else:
#     print('还有说！')

#
# t=()
# print(type(t))
#
#
# t=(1,2,4,45,'kas',('python','hello'))
# print(t[0::2])
# print(t[1::2])
# print(t.index(2))
# print(t.count(4))
# t=[1,2,4,45,'kas',['python','hello']]
# t.append(9)
# print(t)   增加在末尾

# t=[1,2,4,45,'kas',['python','hello']]
# t.insert(2,'2')
# print(t)
# t=[1,2,4,45,'kas',['python','hello']]
# t.extend(['12','3','2'])
# print(t)t=[1,2,4,45,'kas',['python','hello']]  '一次性增加全部‘

# t=[1,2,4,45,'kas',['python','hello']]
# t.pop(2)
# print(t)    '删除默认最后一个，也可通过索引删除'
# #
# list1=['d',2,3,5,7,'df','python',['good','very']]
# list1.copy()
# print(list1)   复制整个列表

#
# list1=['d',2,3,5,7,'df','python',['good','very']]
# list1.remove(7)
# print(list1)     删除指定元素
#

# 元组和列表不同之处
# 1；元组不可变，列表可变
# 2元组如果只有一个元素要加逗号，列表不用
# 3元组tuble（），列表list[]
#
#相同之处
# 有序，有索引
# 可以索引取值
# 切片的方法一致-

# list1=['d',2,3,5,7,'df','python',['good','very']]
# list1[1]='23'
# print(list1)     索引位置直接赋值
#
# list1=['d',2,3,5,7,'df','python',['good','very']]
# list1.clear()
# print(list1)   清空全部列表

# list1=['d',2,3,5,7,'df','python',['good','very']]
# print(list1[3])     切片查，取值
#
# list1=['d',2,3,5,7,'df','python',['good','very']]
# print(list1[3:4:1])    取值

# list1=['d',2,3,5,7,'df','python',['good','very']]
# print(list1[7][0])    取嵌套里嵌套
#
# dict1={1:'no',0.02:'qian',True:'good'}
# print(type(dict1))   类型
#
# dict1 = {1: 'no', 0.02: 'qian', True: 'good'}
# print(dict1[0.02])     通过键值对取值
#
# dict1 = {1: 'no', 0.02: 'qian', True: 'good'}
# dict1['ad']=22
# print(dict1)   没有的值 直接[]新增

# dict1 = {'class':'python','study':['lcy','zl','as'],'mago':{'q':'12','lw':'25'}}
# dict1['class']=3
# print(dict1)     存在的值就等于修改

# dict1 = {'class':'python','study':['lcy','zl','as'],'mago':{'q':'12','lw':'25'}}
# print(dict1['mago']['q'])     通过key 一层一层查

# dict1 = {'class':'python','study':['lcy','zl','as'],'mago':{'q':'12','lw':'25'}}
# dict1.pop('class')
# print(dict1)           指定删除key


# python运算符
# a=16
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# %模运算   取余的整数   判断奇数偶数

# print(5%4)
# print(5%3)

# # 赋值运算符   +=   -=   =
# x=1
# x+=2    1+2
# print(x)
# x=10
# x-=2
# print(x)     10-2

# 比较运算符    >  >= , <  <=  ==  != 不等于
# a=10
# b=2
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print(a==b)
# print(a!=b)

# # print('A'=='a')    区分大小写
# print(False==0)  成立  False=0   True=1

# count=0
# while count<3:
#     print('循环次数')
#     count+=1    #从0开始，每次加一个，到3次为止结束

# count=3
# while count>0:
#     print('循环次数')
#     count-=1   #从3开始，依次递减，每次都校验直到0为止

# count=1
# t=0
# while count<=10:
#     count += 1
#     sex=input('请输入你的性别')
#     age=input('请输入你的年龄')
#     if sex=='f' and 10<=int(age)<=12:
#         print('恭喜你入选！')
#         t+=1
#     else:
#         if sex!='f':
#             print('性别不符合')
#         elif int(age)<10 or int(age)>12:
#             print('年龄不符合')
# print('总入选人数{}:'.format(t))

# num=1
# sum=0
# while num<=10:
#     sum+=num
#     num+=1
# print('总和是{}'.format(sum))


#
# num=10
# sum=0
# while num<=100:
#     sum+=num
#     num+=1
# print('总和是{}:'.format(sum))


# num=0
# while True:
#     num+=1
#     print('语句')
#     if num<3:
#         continue
#     else:
#         break

# num=1
# sum=0
# while True:
#     sum+=num
#     num+=1
#     if num<=10:
#         continue
#     else:
#         break
# print('总和是{}'.format(sum))
#
# #
# count=1
# k=0
# while count<=10:
#     sex=input('性别')
#     age=input('年龄')
#     count += 1
#     if sex=='f' and 10<=int(age)<=12:
#         print('恭喜')
#         k += 1
#     else:
#         if sex!='f':
#             print('性别错了')
#         elif int(age)<10 or int(age)>12:
#             print('年龄错了')
#     if count<=10:
#         continue
#     else:
#         break
# print('总数是:{}'.format(k))
#
#
# #
#
# num=1
# sum=0
# while num<=10:
#     sum+=num
#     num+=1
# print(sum)

# s=(1,2,3,4,5,6,7,8,9,10)
# for item in s:
#     sex=input('请输入性别')
#     age=int(input('请输入年龄'))
#     if sex=='f' and  10<=int(age)<=12:
#         print('恭喜')
#         s+=1
#     else:
#         if sex!='f':
#             print('性别不符合')
#         elif int(age)<10  or int(age)>12:
#             print('年龄不符合')
# print('s')

#
# s='python'
# for a in s:
#     print(a)

# list1=['12','d','da','ok']
# for a in list1:
#     print(a)
#
# dict1={'name':'lcy','age':'18'}
# for a in dict1:
#     print(a)
# dict1={'name':'lcy','age':'18'}
# for value in dict1.values():
#     print(value)
# t=(1,2,3,4,5,6,7,8,9,10)
# for a in t:
#     print(a)

# count=1
# sum=0
# while count<=10:
#     count+=1
#     sex=input('性别')
#     age=int(input('年龄'))
#     if sex=='f' and 10<=int(age)<=12:
#         print('恭喜')
#         sum+=count
#     else:
#         if sex!='f':
#             print('性别不符合')
#         elif int(age)>12  or int(age)<10:
#             print('年龄不符')
# print(sum)
#
# print(list(range(6,0,-1)))  #递减
#
#
# s='python'
# for a in range(0,len(s)):
#     print(s[a])
#
# t=(1,2,3)
# for a in range(0,len(t)):
#     print(t[a])
#
# list1=[1,2,3,4,6,7]
# for a in range(0,len(list1)):
#     print(list1[a])


# sum=0
# for a in range(0,11):
#     sum+=a
#     print(sum)

# sum=0
# for a in range(0,101):
#     sum+=a
#     print(sum)

# sum1=0
# sum2=0
# for a in range(0,101):
#     if a%2==0:
#         sum1+=a
#     else:
#         sum2+=a
# print('奇数和为{},偶数和为{}'.format(sum2,sum1))

# a=int(input('shuz'))
# if a%2==1 and a%3==1:
#     print('{}能被3和5整除'.format(a))   #模的整除
# else:
#     print('{}不能被3和5整除'.format(a))


# list1=[[1,2,3,4],['a','b','c']]
# for a in list1:   #遍历一次
#     for b in a:    #再遍历一次
#         print(b)

# t=(('test','python','lemon'),('lcy',',ake'))
# for a in t:
#     for b in range(len(a)):
#         if b==2:
#             for c in a[2]:
#                 print(c)

# dict1={'name':'lcy','data':{'age':'18','pwd':'123456'}}
# for a in dict1:
#     if a=='adte':
#         for b in dict1['data'].values():
#             print(b)
#     else:
#         print(dict1[a])