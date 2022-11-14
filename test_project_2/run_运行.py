import requests

# import unittest
# import unittestreport
#
#
# sda=unittest.defaultTestLoader.discover("test_unittest框架")
#
#
# cda=unittestreport.TestRunner(sda, title='测试报告',
#                  tester='测试小李',
#                  desc="九神报告",
#                  templates=3)
#
# cda.run()












# ls=[1,2,3]
# ls=tuple(ls)
# # ls=tuple(ls1)
# print(ls)

#
# diet={"name":"lcy"}
#
# print(diet.())

# 用户输入考试成绩，当分数高于90（包含90）时打印A；
# 否则如果分数高于80（包含80）时打印B；否则如果当分数高于70（包含）时打印C；
# 否则如果当分数高于60（包含60）时打印D；其他情况就打印E

# count=int(input("输入分数:"))
#
# if count>=90:
#     print("成绩:A")
# elif count>=80:
#     print("成绩: B")
# elif count>=70:
#     print("成绩:C")
# elif count>=60:
#     print("成绩:D")
# else:
#     print("成绩:E")

# 如下程序从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出
# 提示：
#
# a.
# 1!等于
# 1
#
# b.
# 2!等于
# 1 * 2
#
# c.
# 3!等于
# 1 * 2 * 3
#
# d.n!等于
# 1 * 2 * 3 * ... * n
#


# sum=2
#
# num=0
#
# while sum<=100:
#
#     if sum%2 == 0 :
#         num=num +sum
#     else:
#         num=num-sum
#
#     sum+=1
#
# print(num)
#
# a="1234"
# ls=list(a)
# print(ls)

# a=['1', '2', '3', '4']
#
# s="".join(a)
#
# print(s)
#
# string='lcy,18,男'
# a=string.split(',')
# print(a)
#
# sp='w12133w'
# z=sp.split("w")
# print(z)

# data1=requests.get("http://www.baidu.com")
#
# print(data1.text)

# url='http://httpbin.org/get?name=lcy'
#
# res=requests.get(url)

# url='http://httpbin.org/post'
# data={"kk":"999"}
#
# res=requests.post(url,params={"name":"lcy","age":18},
#                  data=data)
#

# json_data={"qw":12}
# headers={"cokie":"xxxw"}

{
  "input": {
    "leader": {
      "id": "8d57bd7b-e50f-4836-a567-d29d4f9d87c1"
    },
    "member": [
      {
        "id": "0fb0a0a9-fad7-4472-9fa7-d4e115dc8fb9"
      }
    ],
    "name": "222"
  }
}

res=requests.request(method="post",
                     url='https://test2.teletraan.io/graphql/?createEamTeam',
                     # headers=headers,
                     json=json_data
                     )


print(res.text)