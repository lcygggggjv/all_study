

# import requests
#
# rs=requests.post( "https://test2.teletraan.io/login",
#                   json={'query':'{"account":"eam116","password":"teletraan","tenantCode":"110"}'})
#
#
# headers={"user":"Mozilla/5.0"}
# print(rs.text)
#
# res=requests.post(url=url,data=data,headers=headers)
#
# print(res.json())
# print(res.request.headers)

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# url = 'https://www.douban.com/'
# r = requests.get(url, headers=headers)
# print(r.text)




# list1=[[1,2,4,],[6,"lemon",8,"make"]]
#
# for i in range(len(list1)):   #通过长度来循环，list1 长度，0，1
#     for j in  range(len(list1[i])):  #当i  等于0  j循环0，里面列表的所有字符，等于1，里面列表循环后面列表全部内容
#
#         print(list1[i][j])   #通过外面一层的循环长度i ，之后取循环j 循环i里的所有字符，

a=('a','b','c')
x=['1','2','4']

dat=[dict(zip(a,x))]
print(dat)