
import re
#正则表达式  regular 正则
#导入正则re模块
#场景；是一种通过某种规则，匹配字符串的技术
#通过search
#target.group() 对象

# str1='hello world'
#
# b=re.search('l',str1)  #在str1里找l.显示找到的位置索引，类似.find（）
#
# print(b)   #显示找到的位置索引
# #得到匹配的具体的数据
# print(b.group())  #显示搜索的字符串
#
# b=re.search('hl',str1)  #只匹配连在一起的字符串
#
# print(b)


#   .点号  匹配任意一个字符 除了（\n)换行符
#  【7a】匹配【】列举的字符。就是匹配7或者a这两个字符其中一个
#   \d  匹配数字  0-9
#   \D  匹配非数字。不是数字
#   \s  匹配空白 ，空格，tab键
#   \S   匹配非空白
#   \w   匹配单词字符，既a-z A-Z。 0-9 ，_ 字母数字下划线
#  \W  匹配非单词字符  不按照规则

#
# #匹配  \d 数字
# str1='hello world'
# b=re.search(r"l\d",str1)  #匹配一个l，后面是一个0-9的数字，没有显示none
# print(b)  #空的，l后面没有数字是空格

# str2='dsaddas'
# c=re.search(r'd\w',str2)
# print(c)

# # 匹配字符串  \w
# str1='hello world'
# b=re.search(r"l\w",str1)  #匹配l，后面是字符串的，只找前面一组，后面不管
# b1=re.findall(r"l\w",str1)   #匹配l，后面是字符串的，找到全部符合的组合
# print(b)
# print(b1)
#
# #匹配空格  \s
# str1='hello world'
# b=re.search(r"l\s",str1) #匹配l后面加一个空格 这里l后面没有
# print(b)
#
# str2='hello worl d'
# b2=re.search(r"l\s",str2)  #匹配l后面加一个空格 这里最后面有符合l+空格
# print(b2)
#
# #匹配[]里任意一个符合的 或
# str1='hello world'
# s=re.search(r"l[fd]",str1)  #这里括号里lf没有符合，但符合ld ，打印 ld
# print(s)
#
# #匹配 。任意字符
# str1='helro world'
# s2=re.search(r"l.",str1)  #匹配l后面任意字符。换行符\n除外
# print(s2)

#匹配*号 0次或多次  既’wrk*‘  只要k后面有没有k了，没有就显示wr  有2个就是 wrkk
str1='helro worlsd'
s2=re.search(r"worl*",str1)  #匹配l后面任意字符。换行符\n除外
print(s2)

# str3='ddaookw23jk'
#
# s=re.search(r'ao*',str3)   #看*号前面的一位和后面是不是有重复，有就显示，没有就不显示
#
# print(s)

# str3='ddaookw23jk'
#
# s=re.search(r'ao.',str3)   # .号匹配任意字符 除换行符除外
#
# print(s)


#    +号  匹配前一个字符 1次或 n次  至少1次
str32='dasssdaw'
rs=re.search(r's+',str32)
print(rs)


z='daadw22ww'
c=re.search(r'a\w',z)  #取第一个a 后面，任意字符
print(c)

# str3='ddaookw23jk'
#
# s=re.search(r'ao[fs]',str3)   # []匹配 里面任意一个符合的
#             #[fs] 不行因为  ao后面是0 f ,s都不是  换成[fO]就行
# print(s)

# str3='ddaoo kw23jk'
#
# s=re.search(r'o\s',str3)   #  \s  匹配空格
#
# print(s)

# str3='ddaoo kw23jk'
#
# s=re.search(r'o\w',str3)   #  \s  匹配任意字符
#
# print(s)
#   #  ？号  非贪婪模式  0次或1次  从第一个字符看符不符合

d='sddd8jeerx'

sss=re.search(r'2?',d)

print(sss)