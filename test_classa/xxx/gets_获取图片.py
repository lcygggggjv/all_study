


#
# import requests
#
# url='https://pic3.zhimg.com/v2-58d652598269710fa67ec8d1c88d8f03_r.jpg?source=1940ef5c'
#
# response=requests.get(url)  #requests，get方式
#
# # print(response.content)   #图片是二进制是用content
#
#
# #保存图片
#
# with open('auth.jpg','wb') as f:   #wb模式是写图片   文本是wt
#     f.write(response.content)    #写入用write

#
# class A:
#
#     def __init__(self,name):
#
#         self.name=name
#
#     def ak(self):
#
#         self.age=18
#
#     def op(self,sarary):
#
#         self.sarlay=sarary
#
# class B(A):
#
#     def __init__(self,name):
#         self.name=name
#
#     def ak(self):
#
#         super().ak()   #等于上面的self.age=18，先运行这个，后续才是
#         self.age=20
#         super().ak()  #放在最后，就是最后在运行这步
#
#     def ap(self,ii):
#
#         self.sarlays=ii
#
# c_a=B('lcy')
# c_a.ak()
# c_a.ap('da')
# print(c_a.age)
# print(c_a.ap)


class dad:

    def __init__(self):
        print("daw")


    def kty(self,das):
        self.das=das


a_a=dad()

a_a.kty('12')
print(a_a.kty)