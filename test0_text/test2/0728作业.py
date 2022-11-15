# b = input("请输入数据") 表示获取用户输入的内容，并存在 b 变量中，并且 数据类型为字符串。
#
#
# 题目1：
#
# 一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣；如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣和最终价格。
#
# 输入:
#
# price = xxx
#
# 输出:
#
# 购买折扣：8 折
#
# 优惠价格：xxx 元
#
# price=int(input('请输入金额:'))
# if  50<=int(price)<=100:
#     print("""购买折扣:9折
# 优惠价格为:{}元""".format(price*0.9))
# elif int(price)>100:
#     print("""购买折扣:8折
# 优惠价格为:{}元""".format(price*0.8))
# else:
#     print('没有优惠')
#
#
# price=int(input('请输入金额:'))
# if  50<=int(price)<=100:
#     res=int(price*0.1)
#     print(f"""购买折扣:9折
# 优惠价格为:{res}元""")
# elif int(price)>100:
#     res=int(price*0.2)
#     print(f"""购买折扣:8折
# 优惠价格为:{res}元""")
# else:
#     print('没有优惠')
#
#
#
import re

# 题目2：闰年判断
#
# 变量输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
#
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”。
#
# 闰年：
#
# 普通年能被4整除且不能被100整除的为闰年，世纪年能被400整除的是闰
#
# a=int(input('请输入年份:'))
# if a%4==0   and a%100 !=0 or  a%400==0:
#     print("{}是闰年".format(a))
# else:
#     print('{}是普通年'.format(a))
#





#
# 题目3：求三个整数中的最大值
#
# 提示：可定义3个变量，然后比大小

# a=10
# b=20
# c=15
# if b>c:
#     if b>a:
#         print('最大值为b')
#
#     else:
#         print('最大值为a')
# else:
#     if c>a:
#         print('最大值为c')
#     else:
#         print('最大值为a')
#
# #


str='hellodd1 wored'
res=re.search(r'wox*',str)
print(res)