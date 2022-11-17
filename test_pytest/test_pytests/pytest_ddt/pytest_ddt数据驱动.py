


import unittest


from unittestreport import ddt,list_data

#
# #ddT  是unittest Testcase里面的
# @ddt
# class Test_demo(unittest.TestCase):
#
#     @list_data([1,2,3])
#     def test_001(self,item):
#
#         print(item)



#使用pytest 用函数形式，使用ddt

import pytest

#使用pytest.mark.parametrize方法，不要继承unittest
# @pytest.mark.parametrize('item',[1,2,3]) ,要传一个列表.前面 ~=list,data
#                          要传一个字符串item 和上面一致
#
# def test_1(item):
#     print(item)

# 类的 不用继承unittest,再类方法前面使用pytest,parametrize方法

class Test_kk():

    @pytest.mark.parametrize('item', [1, 2, 3])
    def test_2(self,item):

        print(1)

    # def test_03(self):
    #
    #     print(3)
    #
    # def test_04(self):
    #
    #     print(5)