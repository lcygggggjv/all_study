
import pytest

#使用pytest.mark，方法，后面的标签名称 可以自定义
@pytest.mark.important
def test_009():

    print('test_1')

@pytest.mark.important
def test_012():

    print('test_002')

def test_002():

    print('test_90')




#可以再类上面打标签  ,类下面有3个函数。代表筛选了3个用例

@pytest.mark.important
class Test_demo():

    def test_023(self):
        print('test_02')


    def test_0921(self):
        print('test_11')


    def test_11k(self):
        print('test_12')



# pytest -m  "important"  and  ‘login“  满足标签important 和login的用例

#  pytest -m  "important"  or ‘login“   满足标签important 或者  login的用例