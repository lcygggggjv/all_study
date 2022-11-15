

# 现在有字符串：str1 = 'python cainiao 666'
# 请使用代码找出第 5 个字符
str1='python cainiao 666'
print(str1[4])

# 请复制一份字符串，保存在变量 str_two 当中(赋值运算符)
str1='python cainiao 666'
str_two=str1
print(str_two)


# 题目
# 卖橘子的计算器（字符串转化）
# 写一段代码，用户输入橘子的价格，和重量，计算出应该支付的金额！（
# 提示：不需要校验数据，默认传入数字就可以了。
# 使用input函数获取用户输入哦，并且input 得到的数据都是字符串类型，
#
# 字符串转化成浮点数可以用 float(my_string)
#
# ）
#
#

price = float(input("请输入橘子价格："))
weight = float(input("请输入橘子重量："))
a=price * weight
print(('请支付金额{}元'.format(a)))


# 题目
# 字符串综合演练 （字符串索引和切片。注意位置和索引的区别）
# my_hobby = "Never stop learning!"
#
#
#
# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”）；
# “索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）；
# 开始位置 ，是指字符串起始，即下标为0开始；末尾，是指字符串最后。
#
#
#
# 1）截取从 位置2 ~ 位置6 的字符串(含 位置2和6)
my_hobby = "Never stop learning!"
print(my_hobby[2:7])

# 2）截取完整的字符串
my_hobby = "Never stop learning!"
print(my_hobby[:])
print(my_hobby[0:20])

# 3）从 索引3 开始，每2个字符中取一个字符(含索引3，步长为2)
my_hobby = "Never stop learning!"
print(my_hobby[3::2])

# 4）截取字符串末尾两个字符
my_hobby = "Never stop learning!"
print(my_hobby[18:20])
print(my_hobby[-2:])
# 5）字符串的倒序
my_hobby = "Never stop learning!"
print(my_hobby[::-1])

# 题目
# 有字符串s如下
# s = 'python'
# 请编写代码打印字符串s的第一个字符
s = 'python'
print(s[0])
# 请编写代码打印字符串s的最后一个字符
s = 'python'
print(s[-1])

# 题目
# 字符串格式化
# 把姓名、年龄、密码、性别、专业、爱好分别存储在变量中，用下列格式展示：
# age = 18
# 控制台中输出的显示效果：

姓名='lcy'
年龄=18
密码='123456'
性别='man'
专业='计算机'
爱好='足球'

print("""
-------------{}帅哥的基本信息表------------
name:{}
age:{}
password:{}
sex:{}
major:{}
hobby:{}
""".format(姓名,姓名,年龄,密码,性别,专业,爱好))

print(f"""
-------------{姓名}帅哥的基本信息表------------
name:{姓名}
age:{年龄}
password:{密码}
sex:{性别}
major:{专业}
hobby:{爱好}
""")




# 题目：下面字符串定义正确的结果是（多选）
# A. 'hello world!'
# B. "hello world!"
# C. '他说："他很努力！"'

"""窗前明月光，疑是地上霜。
举头望明月，低头思故乡。"""

'A B  C  D '