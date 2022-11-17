import json
import unittest
import pytest
import requests


# class Test_demo(unittest.TestCase):
#
#     def test_01(self):
#
#         pass
#
#
# class Test_demo2():
#
#     def test_02(self):
#         pass
#
# def test_d():
#
#     pass

@pytest.fixture()
def setup():

    print('每次执行一次方法，运行一次用例前置')

    yield

    print('每次执行一次方法，运行一次用例后置')



@pytest.fixture(scope='class')

def class_up():

    print('每执行一次类，运行一次用例前置')

    yield

    print('每执行一次类，运行一次用例后置')



from test_pytest.test_API.test_api import read_excel
from test_pytest.Config.config import Config
from unittestreport import ddt,list_data
from loguru import logger



# import pytest
# import xlrd
#
# def get_data():
#     filename = r'D:\pycharm-workspace\test_pytest\test_case\cases.xlsx'
#     wb = xlrd.open_workbook(filename)
#     sheet = wb.sheet_by_index(0)
#     rows = sheet.nrows
#     print(rows)
#     cols = sheet.ncols
#     print(cols)
#     lst = []
#     for row in range(rows):
#         for col in range(cols):
#             cell_data = sheet.cell_value(row, col)
#             lst.append(cell_data)
#
#     return lst

 #传入前置，和类前置


item=read_excel(Config.test_dir,'adminLogin')   #读取用例 列表里嵌套字典
#[{'id': 1, 'title': '标题1', 'url': '/adminLogin', 'method': 'post', 'data': '{\n "principal": "student",\n "credentials": "123456a",\n "imageCode": "lemon"\n}', 'expected': '{"token_type": "bearer"}'}, {'id': 2, 'title': '标题2', 'url': '/adminLogin', 'method': 'post', 'json': '{\n "principal": "stud",\n "credentials": "123456a",\n "imageCode": "lemon"\n}', 'expected': '{"msg": "Incorrect account or password"}'}, {'id': 3, 'title': '标题3', 'url': 'http://mall.lemonban.com:8108/adminLogin', 'method': 'post', 'json': '{\n "principal": "student",\n "credentials": "123",\n "imageCode": "lemon"\n}', 'expected': '{"msg": "Incorrect account or password"}'}]
# @ddt
@pytest.mark.usefixtures('setup','class_up')
class Test_admin():

    @pytest.mark.parametrize('data',item)  #传字符串变量data，item是传的字典值
    # @list_data(item)
    def test_01(self,data):

        logger.info("运行结果")
        data1=data['data']  #取里面的data值，下面需要用

        json_data=json.loads(data1)  #字符串在转换成字典


        res=requests.request('post',
                             url=Config.host +'/adminLogin',
                             json=json_data,
                             headers={"content-type":"application/json"})

        try:
            actual=res.json()  #try 是json格式跳过，

        except Exception as e:  #异常类型放到变量e

            actual=res.text  #不是json执行这个，等于文本，
            actual={"msg":actual}  #补成字典

        expected=json.loads(data['expected'])  #通过字典取值，取字符串变量data里，对应的expected

        for k, v in  expected.items():   #for循环，取预期结果的值

            assert actual[k] == v  #断言 实际结果的值，和预期结果的值