


#夹具,前置,后置,不使用unit test,怎么用前置后置

class Test_demo():

    #这是unittest的前置
    # def setup(self):
    #     print('用例前置')

    @classmethod
    def setup_class(cls):
        print('pytest的类前置加class')

    @classmethod
    def teardown_class(cls):

        print('pytest的类前置加class')


    #pytest放在方法的前置
    def setup_method(self):

        print('pytest用例前置,加method')

    # pytest放在方法下面的后置
    def teardown_method(self):

        print('pytest用例后置,加method')

    def test_1(self):

        print(2)



#module级别模块的前置,后置

def setup_module():

    print("模块级别的前置加module")


def teardown_module():
    print("模块级别的后置加module")


#pytest 函数的 前置用例,后置用例

def setup_function():

    print("函数前置用function,用例前置")

def teardown_function():

    print("函数前置用function,用例后置")


def test_002():
    print(3)
