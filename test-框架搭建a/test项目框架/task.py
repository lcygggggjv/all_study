



# a=[('caseid', 'data', 'expected'), (1, '{"usname":"lcy","pwd":1234}', '{"message":"登录成功","code":200,"token":"good"}'), (2, '{"usname":"","pwd":1234}', '{"message":"用户名为空","code":401,"token":"bad"}'), (3, '{"usname":"lcy","pwd":""}', '{"message":"密码错误","code":202,"token":"wrong"}'), (4, '{"usname":"lcy2","pwd":1237}', '{"message":"全错误","code":203,"token":"bad best"}'), (5, '{"usname":"lcy3","pwd":1238}', '{"message":"全错误","code":203,"token":"bad best"}')]
#
# c=a[1:]
# b=a[0]
# print(b)
# print(c)

# a=['21','kk']
# b=['zs','asd']
#
# print(zip(a,b))

#
# n=int(input("数字："))
# sum=1
#
# for a in range(1,n+1):
#
#     sum*=a
#
# print(f"阶乘为{sum}")


# n=1
# a=10000
# while a<20000:
#     a*=1.0352  #单次本金+利息
#
#     n+=1   #统计年数
#
# print(f"需要:{n}年")

# a=10
# b=5
# c=a+b
#
# a+=c
# print(c)

#
# class ta:
#
#     le="顺序"
#     dg="产业"
#
#     def __init__(self,sty,ks):
#
#         self.sty=sty
#         self.ks=ks
#
#         print(f"这里要类属性{self.dg}")
#         print(f"这里是实现{sty}")
#
#     def rs(self,op):
#
#         self.op=op
#
#         print(f"实例方法{op}")
#     def emo(self):
#
#         self.rs("调用的")
#
#     @classmethod   #类方法
#
#     def uu(cls,check):
#
#         cls.check=check
#
#         print(f"这里类属性{check}")
#     @classmethod
#     def us(cls):
#
#         cls.uu("触摸")
#
#         print(f"这是调用类方法的{cls.le}")
#
#
#     @staticmethod    #静态方法
#
#     def chang(czs):
#
#         print(f"这是正常{czs}")
#
#
#
# A_ta=ta("重新","出发")
# print(ta.dg)
#
# print(A_ta.sty,A_ta.ks)
# A_ta.rs("不能忘")
#
# A_ta.emo()
#
# A_ta.uu("点击")
# A_ta.us()
#
# A_ta.chang("d")
#


import datetime   #导入datetime库
import time

# a=datetime.date.today()  #打印到年月日
#
# print(a)
#
# print(a.year)  #年
#
# print(a.month)   #月
# print(a.day)    #日
#
#
# print(datetime.datetime.now().hour)  #时
# print(datetime.datetime.now().minute)  #分
# print(datetime.datetime.now().second)   #秒
#
# z=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())   #年月日时分秒
# print(z)
#


# class persions:
#
#     def __init__(self):
#
#         print("我是person构造方法")
#
# class st(persions):
#
#     def __init__(self):
#
#         super().__init__()
#
#         print("我是st构造方法")
#
#
# xy=st()

# class A:
#
#     def __init__(self):
#         self.n=2
#
#
#     def adds(self,m):
#
#         self.n+=m
#
# class B(A):
#
#     def __init__(self):
#         self.n=3
#
#     def adds(self,m):
#
#         super().adds(m)
#
#         self.n+=3


# b=B()
#
# b.adds(2)
#
# print(b.n)


# class A:
#
#     def __init__(self,color):
#         self.n=color
#
#
#     def adds(self,td):
#
#         self.te=td
#
# class B(A):
#
#     def __init__(self,color):
#         self.n=color
#
#     def adds(self,td):
#
#         super().adds(td)
#
#         self.te=td
#
#
# kk=B("蓝颂")
#
# kk.adds("98")
#
# print(kk.n)

dict2={"name":"lcy","age":12,"city":"hz","salary":"点工"}

for k,v in  dict2.items():
    print(k)