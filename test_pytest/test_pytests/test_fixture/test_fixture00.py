


import pytest

#声明这是一个夹具,写一个普通函数
@pytest.fixture()
def setup():

#yield 之前是前置,之后是后置

    print("前置")
    yield    #把yield放在前置和后置中间
    print("后置")

#通过封装成函数,使用yield夹具,形成前置和后置


#可以搞2个夹具,先运行setup,再运行后面的夹具
@pytest.fixture()
def setup2():

#定义另一个夹具
    print("前置2")

    yield

    print("后置2")

@pytest.fixture()
def setup3():

#定义另一个夹具
    print("前置3")

    yield

    print("后置3")




#类级别的夹具

#先声明 再用scope作用域=类
@pytest.fixture(scope='class')

def setup_class():

    print("类前置")

    yield

    print("类后置")


#模块级别的前置后置,直接作用域使用module
@pytest.fixture(scope='module')

def setup_module():

    print("模块前置")

    yield

    print("模块后置")


#包/文件夹 级别的前置后置 作用域用package

@pytest.fixture(scope='package')

def setup_package():

    print("包前置")

    yield

    print("包后置")


# session项目级别的前置后置,,整个项目,作用域对应
@pytest.fixture(scope='session')

def setup_session():

    print("session前置")

    yield

    print("session后置")


#执行test_dd 类, 会运行3次setup  ,一个类,类前置只运行一次

#使用pytest ,mark,usefixtures 一次性传进方法里  类和函数都可以用
@pytest.mark.usefixtures('setup','setup2','setup3','setup_class',
                         'setup_module','setup_package','setup_session')
class Test_dd():

    def test_99(self):

        print(1)


    def test_123(self):

        print(2)

    def test_90(self):

        print(3)


    # def test_011(self,setup,setup2,setup3,setup_class,setup_module):
    #
    #     print(1)
    #
    # def test_012(self,setup, setup2, setup3, setup_class):
    #     print(2)
    #
    # def test_013(self,setup, setup2, setup3, setup_class):
    #     print(3)



@pytest.mark.usefixtures('setup','setup2','setup3','setup_class',
                         'setup_module','setup_package','setup_session')

#运行两个类,会有两个前置
class Test_d2():

    def test_99(self):

        print(1)


    def test_123(self):

        print(2)

    def test_90(self):

        print(3)

    # def test_011(self,setup,setup2,setup3,setup_class,setup_module):
    #
    #     print(1)
    #
    # def test_012(self,setup, setup2, setup3, setup_class):
    #     print(2)
    #
    # def test_013(self,setup, setup2, setup3, setup_class):
    #     print(3)