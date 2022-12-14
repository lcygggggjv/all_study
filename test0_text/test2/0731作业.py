#
# 题目1：冒泡排序, 面试题，不要求提交，（选做题）
#
# 面试之前背熟，工作中用不到。（了解什么是冒泡排序
#\\
# 冒泡排序（Bubble Sort），是一种计算机科学领域的较简单基础的排序算法。其基本思路是，对于一组要排序的元素列，依次比较相邻的两个数，将比较小的数放在前面，比较大的数放在后面，如此继续，直到比较到最后的两个数，将小数放在前面，大数放在后面，重复步骤，直至全部排序完成。
#
# 这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端（升序或降序排列），就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名“冒泡排序”。




#题目2、输出99乘法表(双重for循环)
#
# 格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

for a in range(1,10):
    for b in range(1,a+1):
        print(f'{a}*{b}={a*b}',end='\t')
    print()

for a in range(1,10):
    for b in range(1,a+1):
        print('{}*{}={}'.format(a,b,a*b),end='\t')
    print()


#
# 题目3：用户输入月份,判断这个月是哪个季节(for循环实现)
#
for a in range(1,13):
    b=int(input('请输入月份：'))
    if 1<=b<=3:
        print('这是春天！')
    elif 4<=b<=6:
        print('这是夏天！')
    elif 7 <= b <= 9:
        print('这是秋天！')
    elif 10<=b<=12:
        print('这是冬天！')
    else:
        print('请输入正确月份！')



# 题目4：编写如下程序：
#
# a.用户输入1-7七个数字，分别代表周一到周日；
#
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
#
# c.如果输入0，退出循环
#
# d.输入其他内容，提示：“输入有误，请重新输入！”
#
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
#
a=[1,2,3,4,5,6,7]
b=['周一','周二','周三','周四','周五','周末','周末']

while True:
    c=int(input('请输入数字:'))
    if c in a:
        print('今天是:{}'.format(b[c-1]))
    elif c==0:
        break
    else:
        print('输入有误，请重新输入！')

a={1:'周一',2:'周二',3:'周三',4:'周四',5:'周五',6:'周末',7:'周末'}

while True:
    b=int(input('请输入数字：'))
    if b in a:
        print(f'这是{a[b]}')
    elif b==0:
        break
    else:
        print('请输入正确数字！')





#
# 题目5：编写程序实现，
#
# 在程序中预设一个0~9之间的整数(预设就是指自己指定一个数字即可)，让用户通过键盘输入所猜的数，如果大于预设的数，显示“遗憾，太大了”，
#
# 小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中该数，显示“预测N次，你猜中了！”，其中N是用户输入数字的次数。
#
# 提示：使用while无限循环，当猜中时break

# a=6
# b=0
# while True:
#     c=int(input('请输入1-9的整数：'))
#     b+=1
#     if c>a:
#         print('遗憾，太大了')
#     elif c<a:
#         print('遗憾，太小了')
#     else:
#         print(f'预测{b}次，猜对了')
#         break



