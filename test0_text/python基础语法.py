
#
# print('hello python53')
#
# list1=['12',2,'kd','das']
# list1.insert(0,'ww')
# print(list1)
#
# list1=['12',2,'kd','das']
# list1.pop(0)    索引删除
# print(list1)

#
# list1=['12',2,'kd','das']
# list1.extend([1,'122','231'])
# print(list1)      一次性多个增加

#
# list1=['12',2,'kd','das']
# list1.append(['wq','ad'])     一次性只能一个'g'Huo ['12','123']列表
# print(list1)

# a=input('da')
# print(a)

#
# a=(1,2,46,'21',5,'da')
# print(a.index('da'))   查找元素位置
#
#
# a = (1, 2, 46, '21', 5, 'da')
# print(a[0:2:1])       切片取值
# #
# a = '103kdfdf32'
# a=a.repace('2','w')
# print(a)


# a='d'
# print(type(a))
#
# raise=12
# print(raise)
# raisetry = 12
# # with =
# # inport =
# print(try)

# dict1={'e':'ede','as':'2'}
# a = type(dict1)
# print(a)
#
# lsit1=['we','ew','123',87]
# a=type(lsit1)
# b=a
#
# print(type(b))   type的type  就是type   直接打印就知道数据类型

# num=2
#
# print(isinstance(num,float))   比较判断，true   false
# #
# lsit1='asd,das8,43'
# list1=lsit1.find('43')
# print(list1)
# number=int(input('数字'))
# if number %3 ==0 and number %5==0:
#     print('{}能 被3和5'.format(number))
# else:
#     print('{}bu能 被3和5'.format(number))
#

# ymd=int(input('请输入年份{}'.format('ymd:')))
# if  ymd  %4==0  and  ymd %100!=0 or ymd %400 ==0:
#     print('run')
# else:
#     print('no')       #模  %     被整除  任何数用对应的写  例如被4整除   %4   一百  就是%100
#
#

# T=('E','EQWE','A12')
# LIST1=list(T)
# print(LIST1)

#  # 12321
# number=input('5weis:')
# if number [0]==number[4] and number[1]==number[3]  and number[0]!='0':
#     print('nb')
# else:
#     print('ky')      回文数  个位和万位相同   十位和千位相同   用索引取值方法

# import random
# num1=random.randint(1,9)     取1-9的值
# num2=int(input('shuz'))
# if num2 >num1:
#    print('成功')
# else:
#     print('失败')
#
# #\


#
# ra=int(input('金额:'))
# if 50<ra<100:
#     print('10')
# elif ra>100:
#     print('20')
# else:
#     print('100')

# import random
# num1=random.randint(1,100)
# num2=int(input('数字:'))
# if num2 >num1:
#    print('成功')
# else:
#     print('失败')


# while ['12','23']:
#     print('python while循环条件语句')
#
#
#
# while False:
#     print('python while循环条件语句')


# while  后面条件不为恒定值
# while后面的条件随着循环执行次数变化而变化
#变量自减
# count=3
# while count>0:   #while后面的值要与变量相关
#     print('python while循环条件下的语句')
#     count-= 1    # 每执行一次都要减去1
#变量自加
# count =0
# while count <3 :  # while后面的值要与变量相关
#     print('python while循环条件下的语句')
#     count +=1    #每执行一次都要加1


# #  计算1到10整数的和，输出
# num=1
# sum=0
# while num<=10:
#     print(num)
#     sum+=num    # 这里是每个数字加到sum里面
#     num+=1    #这个是num数字的自加，每次循环加1到10为止
# print('1+10等于:',sum)

#
# import keyword   #查关键字
# print(keyword.kwlist)

#
# count=1
# tok=0
# while count<=10:
#     count+=1
#     sex=input('请输入你的性别:')
#     age=int(input('请输入你的年龄:'))
#     if sex=='f'  and  10<=int(age)<=12:
#         print('符合条件录取')
#         tok+=1
#     else:
#         if sex!='f':
#             print('你的性别不符合')
#         elif int(age)<10 or int(age)>12:
#             print('你的年龄不符合')
# print('总和有多少入选{}'.format(tok))
#


# an='123'
# b=int(an) #转成数字类型
# print(b)
#
# a='1234'
# b=float(a)  #z转成小数
# print(b)
#

# a='kasd3'
# print(a.index('k'))


#
# a='akwet'
# a=a[1::2]
# print(a)

#
# name='lcy'
# age='22'
# city='杭州'
#
# print("""
# -------------{}帅哥的基本信息--------
# 在全国选帅大赛比赛{}获得第一名
# 他的年龄为{}
# 所在城市{}
# """.format(name,name,age,city))


# name='lcy'
# age='22'
# city='杭州'
#
# print(f"""
# -------------{name}帅哥的基本信息--------
# 在全国选帅大赛比赛{name}获得第一名
# 他的年龄为{age}
# 所在城市{city}
# """)


# for a in range(1,10):        #99乘法表
#     for b in range(1,a+1):
#         print("{}*{}={}".format(a,b,a*b),end='')
#     print()

#冒泡算法
#for 循环   a[1,7,4,89,34,2]
#小的在前，大的在后
#相邻俩个数比较
#比较最多n-1
# a=[1,7,4,89,34,2]
# for b in range(len(a)-1):  #用n-1来控制循环次数
#     for c in range(len(a)-1):  #每一次循环对俩俩相邻数据进行比较，并用if判断，进行数据替换
#         if a[c]>a[c+1]:
#             a[c],a[c+1]=a[c+1],a[c]
# print(a)
# a=[1,7,4,89,34,2]
# for b in range(len(a)-1):
#     for c in range(len(a)-1):
#         print(c)

#有1，2，3，4 数字。能组成多少个互不相同的无重复数字，分别有多少

# count=0
# l=[]
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and  b!=c and a!=c:
#                 count+=1
#                 l.append(a*100+b*10+c)
# print('满足条件的数字有{}个:{}'.format(count,l))
#
# for a in range(1,6):
#     for b in range(a):
#         print('*',end='')  #每一层for循环结束后才换行，和乘法表差不多
#     print()
#
#
# for a in range(1,6):
#     for b in range(6-a):
#         print(' ',end='')
#     print('* '*a)
#


# list1=[[1,2,3,4],['甲','乙','丙','丁'],['a','b','c','d']]
# for a in list1:
#     for b in a:
#         print(b)
#
# t=(('test','python','lemon'),('lcy','12'))
# for a in t:
#     for b in range(len(a)):
#         if b==2:
#             for c in a[2]:
#              print(c)
#
# #
# dict1={'url':'www','data':{'phone':'12134','pwd':'9990'}}
# for a in dict1:
#     if a=='data':
#         for c in dict1['data'].values():
#             print(c)
#     else:
#         print(dict1[a])


# a=[1,2,3,4,5,1,2,3]    #列表去重，
# print(list(set(a)))

# a=[1,2,3,4,5]
# a.add()


#
# a=3
# a*=2
# print(a)


#
#
# print('lcy'  in  {'name':'lcy'})
#
# print('name'  in  {'name':'lcy'})

# a=1
# b=2
# print(a>b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# a=10
# b=3
# print(a%b)

ad=12

ad=dict(ad)

print(ad)