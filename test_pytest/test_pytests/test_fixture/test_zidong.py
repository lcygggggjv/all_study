



import pytest

@pytest.fixture()

def fixt():

    print("前置")

    yield  79

    print("后置")


@pytest.fixture()

def fixt_nest(fixt):
    print(fixt)


#自动执行过程
"""
fixt='fixt'
a=getattr(A()，fixt)

fixt=a()
"""

# def test_002(fixt):
#
#     print(fixt)


#  嵌套继承，fixt_nest继承了fixt，002继承了nest
def test_002(fixt_nest):

    print(fixt)