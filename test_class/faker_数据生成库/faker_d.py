import random

import faker

fk=faker.Faker(locale=['zh_CN'])


#生成电话号码

print(fk.phone_number())

#生成身份证号码

print(fk.ssn())

#生成随机数函数 random  自己生成函数

mobile='183'  #以183固定开头的

for i in range(8):  #for循环,8位数，0-7

    new_number=random.randint(0,9)  #  每次生成一个0，9的一个随机数
    mobile+=str(new_number)  #每生成一个转成字符串，加一位在加上183

print(mobile)


#生成名字
print(fk.name())

#生成银行卡

print(fk.credit_card_number())

#生成地址

print(fk.address())

#生成用户信息，所有信息

print(fk.profile())

#随机生成一个数字
print(fk.random.randint(1,30))
#随机生成一个字符串
print(fk.pystr())
#随机生成一个文本
print(fk.text())
