# 题目2：（提示）不需要用不定长参数，把数据存到列表中，for 循环求乘积。

# a=[1,2,3,4]
# s=1
# for b in a:
#     s*=b
#     print(s)

#

# 定义函数，将输入的所有数字相乘之后对20取余数，用户输入的数字个数不确定。

# def a(*k):
#     n=1
#     for c in k:
#         n*=c
#        b=n%20
#     print(f'取余数{b}')
#
#
# a(2,22,1)









#
# 题目3：列表去重函数
#
# 定义一个函数 def remove_element(a_list):，
#
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素(不能用集合去重，要使用for循环)

# z_list=[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# def remove_element(a_list):
#     list2=[]
#     for a in a_list:
#         if a not in list2:
#             list2.append(a)
#     return list2
#
#
# print(remove_element(z_list))



#
#
# 题目4：通过定义一个计算器函数，调用函数传递两个参数，
#
# 然后获取用户输入，如果用户输入1，对2个参数做加法运算，并返回结果。
#
# 如果用户输入2，对2个参数做减法运算，并返回结果。
#
# 如果用户输入3，对2个参数做乘法运算，并返回结果。
#
# 如果用户输入4，对2个参数做乘法运算，并返回结果。
#

# def a(a,b):
#     c=int(input('请输入:'))
#     if c==1:
#        # print(f'{a+b}')
#         return a+b
#     elif c==2:
#        # print(f'{a-b}')
#         return a-b
#     elif c==3:
#         #print(f'{a*b}')
#         return a*b
#     elif c==4:
#        # print(f'{a/b}')
#         return a/b
#
# print(a(2,2))











# 题目5：BMI 计算
#
# 使用函数完成以下操作
#
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
#
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 : 65 / 1.62 ** 2 = 24.8
#
# b.根据BMI指数，给与相应提醒
#
# 低于18.5： 过轻 18.5-25： 正常 25-28： 过重 28-32： 肥胖 高于32： 严重肥胖

# def z():
#     k=float(input('请输入体重：'))
#     m=float(input('请输入身高：'))
#     list1=['你的体重过轻','你的体重正常','你的体重过重','你的体重严重肥胖，需要减肥']
#     bmi=k/m **2
#     if k/m **2<18.5:
#          print('你的bmi指数为:'"%.1f"%bmi)
#          return list1[0]
#     elif 18.5<=k/m **2<=25:
#          print('你的bmi指数为：'"%.1f"%bmi)
#          return list1[1]
#     elif 28<=k/m **2<=32:
#          print('你的bmi指数为：'"%.1f"%bmi)
#          return list1[2]
#     else:
#         print('你的bmi指数为：'"%.1f"%bmi)
#         return list1[3]
# print(z())


def get_bmi(k,h):
    bmi=k/h**2
    if bmi<18.5:
        return '你的体重过轻'
    elif 18.5<=bmi<=25:
        return '你的体重正常'
    elif 28<=bmi<=32:
        return '你的体重过重'
    else:
        return '你的体重严重肥胖'


print(get_bmi(55,1.73))