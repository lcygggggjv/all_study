

# a='a,d,f,v,c'
# b=a.count('a')   #a的总数
# print(b)

# a='a,d,f,v,c'
# b=a.replace('a','yyy')   #替换 a换成yyy
# print(b)


# a='a,d,f,v,c'
# b=a.split(',')    #加个逗号，得到列表
# print(b)


# a='a,d,f,v,c'
# b='-'.join(a)        #用-横杠连接
# print(b)

# a='a,d,f,v,c'
# b="".join(a)      #空格 连接  去掉，
# print(b)
#
#


#
# a='    a,d,f,v,c  '
# b=a.strip()       #去掉左右两边空格
# print(b)



# ls = ['a','b','c']
# ls.remove('b')
# print(ls)



# a={"name":"lcy","age":"18"}
# print(a.values())
# print(a.keys())
# print(a.items())

#
# ls = ['我', '爱', '学', '习', '天', '天', '向', '上']
# str1=''.join(ls)
# print(str1)


# string='lcy.18.男'
# a=string.split(',')
# print(a)

#
# a='12324'
# b='778'
# print(a+b)

# a="'123','24'"
# b="778"
# print(a+b)


# s= ['123','ad','azx']
# a=''.join(s)
# print(a)


# s= "'123','ad','azx'"
# a=','.join(s)
# print(a)

# s= "'123','ad','azx'"
# a=s.strip()
# print(a)

# s= ['123','ad','azx']
# s[1]='kk'
# print(s)

# s= ['123','ad','azx']
# s.sort()
# a=s
# a.reverse()
# print(a)

# s={'key':'name','lcy':'12'}
# print(s.values())
# print(s.keys())
# print(s.items())
# s={'key':'name','lcy':'12'}
# print(s.get('lcy'))
# s={'key':'name','lcy':'12'}
# s['age']='kk'
# print(s)
#
# sum1=0
# for a in range(1,101,2):
#     sum1+=a
#
#     print(sum1)

# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#                 if (x!=y) and (y!=z) and (z!=x):
#                         print("%d%d%d" % (x, y, z))

# #  %s   字符型
# y='asdfghj'
# print('%s'%y)   #按正常输出字符
# print('%6s'%y)   #输出6位字符，不足6位字符的左边用空格符补充，超过6位全部输出
# print('%.2s'%y)  #截取前两位字符，不足2位，左边用空格补充
# print('%6.2s'%y)  #先截取2位，在补足6位字符
#
#
# #  %d  数字型
# a=12345678
# print('%d'%a)     #按正常输出数字
# print('%6d'%a)    #输出6位数字，不足6位字符的左边用空格符补充，超过6位全部输出数字
# print('%06d'%a)    #输出6位数字，不足6位字符的左边用0补充，超过6位全部输出数字
# print('%.2d'%a)     #先截取2位数字，不足2位左边用0补充
# print('%6.2d'%a)    #先截取2位数字，补足6位字符，不足6位空格符补充
# print('%06.2d'%a)   #先截取2位数字，然后补足6位字符，不足6位用0补充
#
#  # %f   浮点型
#
# test=3.14159265
# print("按正常输出：%f"%test)    #%f：按正常输出，默认输出小数点后6位小数
# print("按长度输出：%11f"%test)   #输出6位数字，默认输出小数点后6位小数，不足6位数字的左边用空格符补充，超过6位数字的输出全部数字
# print("不足补0输出：%011f"%test)   #输出6位数字，默认输出小数点后6位小数，不足6位数字的左边用“0”补充，超过6位数字的输出全部数字
# print("按截取输出：%.4f"%test)     #输出小数点后2位小数
# print("截取后补足：%11.4f"%test)    #输出小数点后2位小数，然后补足6位字符，不足6位用空格符补充
# print("截取后补0：%011.4f"%test)   #输出小数点后2位小数，然后补足6位字符，不足6位用“0”补充
#
# a='1233'
# print('%6.2s'%a)
# a=1.23
# print('%06f'%a)



#
# for a in range(1,3):
#     print(a)

#
# for a in range(5):
#     name=input('请输入用户名:')
#     password=int(input('请输入密码:'))
#     if name=='lcy':
#         if password==123456:
#             print('登录成功')
#             break
#         else:
#             print('密码错误,请重新输入！,还有{}次机会'.format(4-a))
#     else:
#         print('用户名不正确，请重新输入！,还有{}次机会'.format(4-a))
#
#


# for i in range(3):
#     user = input('请输入用户名：')
#     passwd = input('请输入密码：')
#     if user=='root' and passwd == 'westos':
#         print('%s用户登录成功' %user)
#         break
#     else:
#         print('密码错误，请重新输入密码,您还剩%d次机会' %(2-i))
# else:
#     print('超过三次，登录失败')


# for a in range(10):
#     for b in range(a):
#         print(b)


#99乘法表

# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f'{a}*{b}={a}*{b}\t',end='\t')
#     print()

# a=10
# b=12
# c=16
# max=c
# if c<a:
#     max=a
# if c<b:
#     max=b
# print(max)


# a=10
# b=12
# c=16
# num=[a,b,c]  #放在列表里
# num.sort()  #  排序
# print(num[-1])   #取最大的一个

# a=10
# b=12
# c=16
# print(max(a,b,c))   #内置函数求最大值
#
# for a in range(10):
#     for b in range(a):
#         print(b,end='\t')


# dict1={'name':'lcy','age':19,'city':'hz'}
# for a in dict1:
#     print(a)   #默认循环key
#
# #
# dict1={'name':'lcy','age':19,'city':'hz'}
# for a in dict1.values():  #通过.value  取
#     print(a)
#     #

# dict1={'name':'lcy','age':19,'city':'hz'}
# for a ,b in dict1.items():   #通过.items  取全部的
#     print(a,b)

# for a in range(1,6):
#     for b in range(1,a+1):
#             print(b,end='\t')   #在循环内部不换行，执行完此循环之后换行
#     print()
#

# for a in range(1,10):
#     for b in range(1,a+1):   #每次循环执行都加一
#         print(f'{a}*{b}={a*b}',end='\t')    #99乘法表
#     print()

#
# while 1:
#     a = int(input('请输入数字:'))
#     if 1<=int(a)<=5:
#         print(f'今天是周{a}')
#     elif int(a)==6 or int(a)==7:
#         print(f'今天是周末')
#     elif int(a)==0:
#         break
#     else:
#         print('输入有误，请重新输入！')

# a=[1,2,3,4,5,6,7]   #定义一个列表放在里面引用
# b=['周一','周二','周三','周四','周五','周日','周日']  #定义一个列表放在里面引用
#
# while True:
#     c=int(input('请输入数字:'))   #需要int  ，不然可能当成字符串，
#     if c in a:
#         print('今天是{}'.format(b[c-1]))   #取b里的数据，按照索引0，1，2
#     elif c==0:
#         break   #终止循环
#     else:
#         print('输入错误，请重新输入！')
# #
# a=[1,7,4,89,34,2]
# for b in range(0,len(a)):
#      for c in range(0,len(a)):
#         print(c,end='\t')
# print(b)


# a=[1,7,4,89,34,2]
# for b in range(1,len(a)):
#     for c in range(0,len(a)-b):
#         if a[c]>a[c+1]:
#             a[c],a[c+1]=a[c + 1],a[c]
#
# print(a)
# a={'c':'周一',2:'周二',3:'周三',4:'周四',5:'周五',6:'周末',7:'周末'}
# print(a['c'])

# sum=0
# for a in range(1,5):  #从一开始，到4结束
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and b!=c and a!=c:  #判断条件
#                 print(a,b,c)
#                 sum+=1   #每个数加一遍
# print(sum)  #打印全部

# a=int(input('请输入数量:'))
# b=0
# q=[100000,100000,200000,200000,400000]
# w=[0.1,0.075,0.05,0.03,0.015,0.01]
# for d in range(len(q)):
#     if a <=q[d]:
#         b+=a*w[d]
#         a=0
#         break
#     else:
#         b+=q*[d]*w[d]
#         a-=q[d]
# b+=a*w[-1]
# print(b)


# profit=int(input('Show me the money: '))
# bonus=0
# thresholds=[100000,100000,200000,200000,400000]
# rates=[0.1,0.075,0.05,0.03,0.015,0.01]
# for i in range(len(thresholds)):
#   if profit<=thresholds[i]:
#       bonus+=profit*rates[i]
#       profit=0
#       break
#   else:
#       bonus+=thresholds[i]*rates[i]
#       profit-=thresholds[i]
# bonus+=profit*rates[-1]
# print(bonus)

#
# import copy
# a=[1,2,3,4,['a','b']]
# b=copy.copy(a)
# print(b)

# def eat (name,food):
#     print(f'{name} 请你吃{food}')
#
#
# def offer(name,salary):
#     print(f'{name} 拿到了 {salary}')
#


# def a(a,*k):   #不定长  可以传多个以元组的形式存在一起，收集剩下的位置参数收集
#     print(f'需要{k}')
#     # print(f'咱{y}')
#     print(f'说什么{a}')
#     return 4
#
# print(a('话说','真个','lcy'))    #不能收集关键字参数



# def zz(y,*r,**n):   #**n  接收剩下的关键字参数，以字典形式   ，等号放在最后面
#     print(f'{y}')
#     print(f'真能{r}')
#     print(f'真{n}')
#     return 0
#
# print(zz(12,'kkk','vy',n=12))
#

#
# def zz(y,*r,**n):
#     global d  #我在这里获取全局变量d
#     print(f'{y}')
#     print(f'真能{r}')
#     print(f'真{n}')
#     d=210
#     print(f'{d}')
#
#
# #函数里定义的变量，和外面定义的变量，不一样
# d=10
# zz(456)

# def eat(name,food):   #5
#     print(f'{name}请大家吃{food}')
#
#
# def off(name,salary):  #  2 来到这一步，name=lcy  salary=12k
#     print(f'{name}拿到了一个{salary}的off')  #3，依次对应
#     eat(name,'辣条')   #4  来到这个eat调用
#
#
# off('lcy','12k')   #先是调用off函数  1
#
# #

# def eat(name,food):   #5
#     print(f'{name}请大家吃{food}')
#
#
# def off(name,salary):  #  2 来到这一步，name=lcy  salary=12k
#     print(f'{name}拿到了一个{salary}的off')  #3，依次对应
#     eat(name,'辣条')   #4  来到这个eat调用
#
#
# off('lcy','12k')   #先是调用off函数  1
#







# def eat():
#     pass
#
# def main():
#     ch=input(":")
#     if ch=='eat':
#         eat()
#
# main(eat=1)

# def eat():
#     print("调eat")
#     pass
# def work():
#     print("调work")
#     pass
# def sleep():
#     print("调sleep")
#     pass
#
# def main(choice):
#     # choice = input("选择---")
#     if choice == "eat":
#         eat()
#     if choice == "work":
#         work()
#     if choice =="sleep":
#         sleep()
#
#
# main('eat')

# def eat(somefood):
#     print("调eat")
#     print(f"吃{somefood}")
#     pass
#
#
# def work(workingtime):
#     print("调work")
#     print(f"工作{workingtime}小时")
#     pass
#
#
# def sleep(sleepingtime):
#     print("调sleep")
#     print(f"睡了{sleepingtime}小时")
#     pass
#
#
# def main(food, sleep_time, work_time):
#     choice = input("选择---")
#     if choice == "eat":
#         eat(food)
#     if choice == "work":
#         work(work_time)
#     if choice == "sleep":
#         sleep(sleep_time)
#
#
# main("汉堡", "十", 8)


# s=0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and a!=c  and b!=c:
#                 print(a,b,c)
#                 s+=1    #把每种可能都加一次
# print(s)

# a=[1,4,7,2]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# for a in range(1,10):
#     for b in range(1,a+1):   #a=1  (1,2)   取到1  依次
#         print(f'{a}*{b}={a*b}',end='\t')
#     print()


# list1=[1,5,34,2,4,6,9,3]
#
# print(sorted(list1))


# list1=[1,5,34,2,4,6,9,3]
#
# for a in range(len(list1)):
#     for b in range(a,len(list1)):
#         if list1[a]>list1[b]:
#          list1[a],list1[b]=list1[b],list1[a]
# print(list1)
#
# list1=[1,2,3,4,1,2,3,4]
# set1=set(list1)
# list2=list(set1)
# print(list2)

# title1=['id','name','url']
# case1=[1,'lcy','http://11']
# case2=[2,'lcy2','http://12']
#
# lst=list(zip(title1,case1))
# print(lst)
#
# print(dict(lst))
# a=[1,2,3,5]
# try:
#     print(a[6])
# except:
#     print('报错了')

#
# a=int(input(':'))
# b=int(input(':'))
# c=int(input(':'))
#
# if a>b:
#     if a>c:
#         print(f'最大值为{a}')
#
# else:
#     if a<c:
#         if c<b:
#             print(f'最大值{b}')
#         else:
#             print(f'最大值为{c}')


# list1=[1,4,2]
#
# print(sorted(list1))
# a='1212,ad,0a'
#

#a.split(',')
# print(a)  #去掉俩边的引号
#
#
# a=['1212','ad','0a']
# str1=''.join(a)
# print(str1)   #jion  去掉空格，也可以填其他符号。合并
#
# a='12,12d,a,asd'
# c=a.split(',')
# print(c)  #得到列表形式
#
# a='  aks.asd,d12   '
# c=a.strip()  #去掉两边的空格
# print(c)
#
# a='12'
# b='12'
# print(a+b)
# sum=0
# for a in  range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and a!=c  and b!=c:
#                 print(a,b,c)
#                 sum+=1
#     print(sum)

# import math
#
# for i in range(1,10000):
#     x=int(math.sqrt(i+100))
#     y=int(math.sqrt(i+268))
#     if (x*x==i+100)and(y*y==i+268):
#         print(i)

# a=int(input('数字1:'))
# b=int(input('数字2:'))
# sum=a+b
# print(sum)

# a=int(input(':'))
# if a>0:
#     print('正数')
# elif a<0:
#     print('负数')
# else:
#     print('等于0')


# list1=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
# a=int(input('数字:'))
# if a not in list1:
#     print('不是阿姆斯特朗数字')
# else:
#     print('是')
#
# a=[1,23,6,8,9]
# v={'name':'lcy'}
# c='s'
# try:
#     print(a[9])
#     print(v['lc'])
#     print(int('a'))
# except IndexError as e:
#     print(f'indexError错误提示{e}')
# except KeyError as e:
#     print(f'keyError{e}')
# except ValueError as e:
#     print(f'valueError{e}')

# f=open('td.txt',encoding='utf-8')
#
# b=f.read()
# print(b)
# # f.close()
# str1='abd'
# print(str1.encode())
# print(type(str1.encode()))

#
# d=open('aa.py',mode='a',encoding= 'utf-8'  )
#
# d.write('\n lcy')

# f=open('截图3.png',mode='rb')
# print(f.read())
# f=open('截图5.png',mode='rb')
# f.write()
#
#
# string='lcy@18@男'
# a=string.split('@')
# print(a)

# for a in range(3):
#
#     print(a)



# def argss(*k):   #定义一个不定长参数
#
#     a=1  #定义变量a 为1，
#     if k:
#         for item in  k:   #每循环一次都想×
#             a*=item
#
#         s= a % 20   #于20
#         print(f"结果{s}")
#
#
# argss(10,20,30,40,50)
# argss(22,33)
#
#
#
# list1=[1,3,6,8,3,2,1,60,28]
#
# def lz(list1):   #形参
#
#     ak=[]   #空列表
#     for a in list1:   #for循环  列表里的
#         if a not in ak:  #如果不在里面新列表里面。
#
#             ak.append(a)  #添加到新列表
#
#     return  ak
#
# print(lz(list1))


