


# def eat(name,salary):
#     print(f"{name},工资{salary}")
#
#
# def offer(name,food):
#     print(f"{name},喜欢吃{food}")
#     eat(name,1000)
#
# offer("lcy","土豆丝")

person_info = [

{

"name": "明鹏程",

"age": 22,

"gender": "男",

"hobby": "学习",

"motto": "学习使我快乐"

},

{

"name": "萌笑天",

"age": 20,

"gender": "女",

"hobby": "拿30K offer",

"motto": "下次拿个40K 的"

},

]
# 得到一个 info.txt 的文件：
#
# name,age,gender,hobby,motto
#
# 明鹏程,22,男,学习, 学习使我快乐
#
# 萌笑天,20,女,拿30K offer,下次拿个40K 的

# with open("info3.txt",mode="wt",encoding="utf-8") as data:
#     a=person_info[0].keys()
#     b=list(str(k) for k   in   person_info[0].values())   #列表推导式，将所有元素循环，转换字符串，外面是列表
#     c=list(str(s)  for s  in  person_info[1].values())
#     data.write(f'{",".join(a)} \n')  #需要都是字符串
#     data.write(f'{",".join(b)} \n')   #结束换行
#     data.write(f'{",".join(c)} \n')


with open("cases.txt", mode="rt", encoding="utf-8") as f:

    a=f.readline()   #读取一行
    # print(a)
with open("cases.txt", mode="rt", encoding="utf-8") as f:
    next(f)  #接着读取
    b=f.readline()
    # print(b)

def li(data):   #定义函数，data形参
    data2=data.split("@")  #分割得到列表
    m_dict={}   #定义一个空字典
    for i in range(len(data2)):  #for循环 ，列表的长度  每个都是# 字符串，操作相同
        li2=data2[i].split(":")  #分割得到列表 ,例如列表长度3，，0，1，2，每一个字符串，如 "url:www.baidu''分割成["url","www.baidu"]这样的列表：，依次添加到字典

        m_dict[li2[0]]=li2[1]   #新增添加字典，列表第0个为key值，第一个为value值，。循环所有

    return m_dict  #返回字典

def lis2(m_dict,m_dict2):  #传参两个字典
    my_list=[]
    my_list.append(m_dict)  #一个个添加字典
    my_list.append(m_dict2)
    return my_list  #返回列表

print(lis2(li(a),li(b))) #调用函数，一下可以用两个 两行，不同参数