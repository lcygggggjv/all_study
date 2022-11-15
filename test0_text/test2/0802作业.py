
# 题目1：定义函数，并通过给函数传递不同的参数(要想清楚哪些做为参数哦！！)：

# def kk(a,b):  #a，b形式参数
#     c=a+b
#     return c  #函数运算的结果
#
# print(kk(1,2))  #1,2为实际参数
#  # a对应1，b对应2. 位置参数就是实际参数和形式参数一一对应，且不多不少

#
# def yy(z=2,x=3):  #z=2,x=3是默认参数。  单个默认参数有=号的要在后面
#     d=z+x
#     print(z)  #这里z=6 对应z关键字参数
#     print(x)   #x=8  对应x关键字参数
#     return d
# print(yy(z=6,x=8))  #z=6  x=8  关键字参数，有关键字参数，默认参数就不会用到
#



# 一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），
#
# 如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
#
# 编写一程序，询问购买价，再显示出折扣（%10或20%）和最终价格。
#
# def pr(a):   #参数值提取，再这边代码会变得值既变量，作为参数值
#     # a=int(input('请输入金额:'))
#     c=['九折','八折']
#     if 50<=int(a)<=100:
#         price=a-(a*0.1)
#         print(f"""折扣为{c[0]}
#     最终价格为{price}""")
#     elif int(a)>100:
#         price = a - (a * 0.2)
#         print(f"""折扣为{c[1]}
#     最终价格为{price}""")
#     else:
#         price = a
#         print(f'没有折扣，原价{price}')
#         return  price  #关注返回什么，注重返回值，继续用到的
#
# pr(100)
#

#
# 题目2：对前面知识做一个简单总结，自己梳理一下，重点复盘不太熟悉的知识点。
#
# 提交总结文件（txt, 思维导图,图片都可以）


# def a(kk):
#     print('多少时间')
#     print(f'{kk}')
#     return 9
#
# a(12)
# a(89)
# print(a(1))
#
#

# def a(kk,ou=1):
#     print('多少时间')
#     print(f'{kk}')
#     print(f'{ou}')
#     return 9
# a(kk=2,ou=3)
#

# a=['12',12,'dkad','das']
# for b in range(0,len(a)):  #循环a的长度，从0开始
#     print(b)
#
# a=[12,'asd','hc','p']
# for x in a:  #循环列表a
#     print(x)
#

# b='123kda3236'
# for c in range(0,len(b)):
#     print(c)

# s=('12',123,567,'kds')
# for z in range(len(s)):
#     print(z)

# s=('12',12,4,'asd')
# for items in s:
#     print(items)
#


#
# w={'name':'lcy','age':19,'city':'hz'}
# for a in w.items():  #取key和value
#     print(a)
#


# w={'name':'lcy','age':19,'city':'hz'}
# for a in w.values():  #只取value 值,
#     print(a)

#
# w={'name':'lcy','age':19,'city':'hz'}
# for a in w.keys():  #只取key 值,
#     print(a)
#

# w={'name':'lcy','age':19,'city':'hz'}
# for a,b in w.items():  #也可以通过2个变量接收.元组拆包
#     print(a,b)

#
# tuple_1=(3,4)
# a,b=tuple_1   #a,b  = 3,4
# print(a,b)
#
# cases=[['id','title','pem'],
#        [1, '标题1', '预期1'],
#        [2, '标题2', '预期2'],
#        [3, '标题3', '预期3']
#        ]
#
# for a in cases:
#     for b in a:
#         print(b)

# c=[1,2,3,4,5]
# for a in range(len(c)):
#     for b in range(len(c)):
#         print(b)

# 题目1：定义函数，并通过给函数传递不同的参数(要想清楚哪些做为参数哦！！)：
#
# 一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），
#
# 如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
#
# 编写一程序，询问购买价，再显示出折扣（%10或20%）和最终价格。

# 题目：优化去生鲜超市买橘子程序
#
# a.收银员输入橘子的价格，单位：元／斤
#
# b.收银员输入用户购买橘子的重量，单位：斤
#
# c.计算并且 输出 付款金额
#
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
#

# rmb=float(input('请输入价格:'))
# weight=float(input('请输入重量:'))
#
# price=rmb*weight
#
# try:
#     if price<0:
#         raise ValueError
#
# except :
#     print('输入的价格或重量要大于0')

# def buy():
#      while True:
#         try:
#             rmb=float(input('请输入价格:'))
#             weight=float(input('请输入重量:'))
#             price=rmb*weight
#             print(f'付款金额为{price}')
#
#
#         except :
#             print('输入数据有误，请重新输入')
#
#
# buy()



# 请你说出常见的异常类型，并举个例子说明什么场景会遇到该异常类型。

# importError  无法引入模块或包
# indexError 下标索引超出序列边界
# NameError；使用一个还没赋予对象的变量
# keyError  字典值不对
# syntaxERROR；语法错误
# valueError   值错误
#
#
# list1=[1,12,2,4]
# print(list1[6])   # indexError  索引值最大到3，超过3取不到了
#
# t='123a'
# print(b)  # NameError 没有变量b  没有赋值
#
# dict1={'name':'lcy','age':24,'city':'hz'}
# print(dict1['sex'])  #KeyError: 'sex'  字典没有key sex


# def a(name,pwd):
#     b={'id':None,'code':None}
#
#     if name=='lcy' and pwd==123456:
#
#         b['id']=12
#         b['code']=111
#
#         return b
#
# print(a('lcy',123456))

# def login(name,pwd):
#     z=100
#     c=100
#     msg="""
#
#
# """
#
#     assert

# f =open('info1.txt',mode='a',encoding='utf-8')
#
# f.write('\n zz\n')
# f.write('sd')

# f=open('1.png',mode='rb')
# data=f.read()
#
# f=open('2.png',mode='wb')   #拿到图片1读取，写入图片2里
# f.write(data)
# f.close()

# with open('1.png',mode='rb') as f:
#     data=f.read()
# def lens(a,*b):
#     print(f'这是{a}')
#     print(f'xxx{b}')
#
#     return
#
#
# lens(12,'ka','ad')
#
# def ka(s,**x):
#     print(f'数字{s}')
#     print(f'快{x}')
#     return
#
# ka(1,da=1,ad=1)
#
# def rs7(e,*t,**y):
#
#     print(f'{e}')
#     print(f'{t}')
#     print(f'{y}')
#     global d
#     d=d+12
#     print(f'{d}')
#     return
#
# # rs7('kk','不定长1','不定长2',z=12,k=8)
# d=100
# rs7(1,2,c=12)
# import time
#
#
# def  timesa(a):
#     print(f'{a}')
#     (f'时间{time.strftime('%Y-%m-%d')}')
#
# a=123445
# print('%d'%a)
#
# c='1dqwdew'
# print('%s'%c)
#
# e=3.126232
# print(f"{'%f'%e}")

class ket:   #ket类
    name='ka'   #类属性
    atm=123

    def __init__(self,color,top):  #实例属性
        self.color=color
        self.top=top

        print(f'这个是什么颜色{color},排名第几{top}')
        print(f'名字是什么{self.name}')   #获取类属性，用self，


    def run(self,key,value):   #实例方法
        self.key=key
        self.value=value

        print(f'字典的名称和值{key}{value}')

    def sit(self):
        self.run('绿色','67')   #调用其他方法的key,value输入参数，

    @classmethod   #类方法

    def tests(cls,id,say):
        cls.id=id
        cls.say=say
        print(f'这是类方法里的{id}和title{say}')
    @classmethod

    def test2(cls):
        cls.tests(12,'kk')
        print(f'想调用实例的值{cls.name}')

    @staticmethod  #静态方法

    def  nulls(lcy):
        print(f'这是静态方法就是普通函数{lcy}')

    @staticmethod

    def null2():
        print('这是空的静态函数')

A_ket=ket('蓝色','3')
print(ket.name)
print(A_ket.color,A_ket.top)

A_ket.run('lcy',19)
A_ket.sit()
A_ket.tests(100,'d')
A_ket.test2()
ket.nulls('ok')