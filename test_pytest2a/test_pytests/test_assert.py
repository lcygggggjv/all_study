

import unittest


class Test_demo(unittest.TestCase):

    def test_01(self):

        self.assertEqual(1,2)



# class Test_d2():
#
#     def test_01(self):
#
#         self.assertEqual(1,2)   #没继承unittest。testcase ，不能用这个
                                #直接用自带  assert

# class Test_d():   #类的名称必须大写
#
#     def test_11(self):
#
#         assert 1 ==1

class Test_d():   #类的名称必须大写

    def test_11(self):

        assert "a"  in "bcd"   #包含




def test_04():

# 实际结果在前面   ，预期结果在后面
    assert 2 ==3



a=1000
b=100