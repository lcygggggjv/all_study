# 题目1：
#
# 把以下字典分行添加到文件当中：
#
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
#
# 得到一个 info.txt 的文件：
#
# name,age,gender,hobby,motto
#
# 明鹏程,22,男,学习, 学习使我快乐
#
# 萌笑天,20,女,拿30K offer,下次拿个40K 的






#
# 题目2：
#
# 手工准备cases.txt 文件，文件中手工复制 2 行数据：
#
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
#
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@pwd:1000
#
# 请利用上课所学知识，把txt里面的两行内容取出然后保存到一个列表和字典当中：（可定义函数）
#
# 列表当中，有2个字典
#
# 每一行的数据，就是一个字典。
#
# 字典的key分别是：url,mobile,pwd

# a=[121,123455]
# b=[1,3,5]
#
# def k (nn):
#     return (f'{nn}')
#
#
# print(k(a),k(b))

# a='@2134562@sw@'
# b=a.split('@')
# print(b)

with open('cases.txt', encoding='utf-8') as f:
    data=f.readline().strip('\n')
    data2=data.split('@')

# with open('cases.txt',encoding='utf-8') as f:
#     next(f)
#     rr=f.readline().strip('\n')
#     r2=rr.split('@')

for i in range(len(data2)):
    # data=f.readline().strip('\n')
    # data2=data.split('@')

    dict1={}
    li_1=data2[i].split(':')
    dict1[li_1[0]]=li_1[1]
    # print(dict1)

# with open('cases.txt',encoding='utf-8') as f:
#     next(f)
#     rr=f.readline().strip('\n')
#     r2=rr.split('@')
with open('cases.txt', encoding='utf-8') as f:
    next(f)
    rr=f.readline().strip('\n')
    r2=rr.split('@')

for i in range(len(r2)):
    dict2={}
    l2=r2[0].split(':')
    dict2[l2[0]]=l2[1]
    # print(dict2)

m_list=[]
m_list.append(dict1)
m_list.append(dict2)
print(m_list)
# with open('cases.txt', encoding='utf-8') as f:
#     next(f)
#     rr = f.readline().strip('\n')
#     rr_2=rr.split('@')
    # m_dict2={}
    # for i in range(len(rr_2)):
    #     li_2=rr_2[i].split(':')
    #     m_dict2[li_2[0]]=li_2[1]
    # # print(m_dict2)




with open('cases.txt', encoding='utf-8') as f:
    a=f.readline()
    # data2 = data.split('@')
with open('cases.txt', encoding='utf-8') as f:
    next(f)
    b = f.readline()
    # rr_2 = rr.split('@')

def  dd (data):
    # data = f.readline().strip('\n')
    data2 = data.split('@')
    m_dict = {}
    for i in range(len(data2)):
        li_1 = data2[i].split(':')
        m_dict[li_1[0]] = li_1[1]
    return m_dict



def list1(m_dict,m_dict2):
    my_list=[]
    my_list.append(m_dict)
    my_list.append(m_dict2)
    return my_list
print(list1(dd(a),dd(b)))


def list1(m_dict,m_dict2):
    my_list=[]
    my_list.append(m_dict)
    my_list.append(m_dict2)
    return my_list
print(list1(dd(a),dd(b)))
