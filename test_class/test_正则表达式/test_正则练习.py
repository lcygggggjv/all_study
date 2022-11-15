


str1="""{"appType":3,"checkRegisterSmsFlag": "#smsflag#","mobile": "#mobile#","userName":"#username#","password":"123456","registerOrBind":1,"validateType":1}"""

import re

# res=re.search('#(.+?)#',str1)    # 两个#号之间匹配 匹配所有符合的 .号是任意一个字符，+号至少有一个
   #换行只显示一个  ，不换行显示全部  ?号非贪婪模式，尽可能少的匹配

# print(res)
# print(res.group())
# # res1=re.search('#(.+)#',str1)
# print(res.group(1))  #去掉2边括号，加括号，形成1个组，
#

class Data:
    smsflag='cookie'
    mobile='18355936526'
    username='kds'


#找出所有符合规则的#号
res2=re.finditer('#(.+?)#',str1)   #finditer是匹配全部的   ?号 非贪婪模式，尽可能少匹配
                            #  +号  至少前一个字符 1次或多次次  至少一次


for el in res2:   #for 循环取全部的匹配

    old=el.group()  #el每次循环的匹配的具体数据内容. el从第一组匹配   old是接收，后面组循环
    print(old) #开始的el是对象，.group才能去
    new_name=old.strip('#')   #old使用strip去指定#号，新的值等于，老的数据去除两边的#号
    print(new_name)
    new_=getattr(Data,new_name)   #取新的值，上面类的属性 ， getattr(data,'smsflag') NEW=SMSFLAG =对应类里面的属性 和data.smsflag结果一致
    print(new_)
    str1=str1.replace(old,new_)  #使用replace替换  前面旧的后面是新的，每次循环一组至结束

print(str1)   #打印新的



#
# res=re.finditer(r'#(.+?)#',str1)
#
#
# for el in res:
#
#     old=el.group()
#
#     new=old.strip('#')
#
#     new_ss=getattr(Data,new)
#
#     str1=str1.replace(old,new_ss)
#
# print(str1)














