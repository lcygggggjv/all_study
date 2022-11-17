


def gen():

    print('前置')
    yield
    print('中置')
    yield
    print('后置')
    yield
    print('最后')


a=gen()  #属性值

#一个个循环使用
# for e in a:
#     pass

next(a)  #一个个运行生成