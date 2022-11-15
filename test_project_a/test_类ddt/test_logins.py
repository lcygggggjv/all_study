
import unittest

from test_project_a.common.logs_处理 import logger #导入日志的方法
from  test_project_a.common.excel_2封装函数 import read2_excel  #导入excel
from test_project_a.test_测试函数.test_函数方法1 import testlogA  #导入测试函数
from test_project_a.config.setting import Config


filed=Config.CASE_FILE   #这里从配置文件，导入配置文件，方便修改

cases=read2_excel(filed)

from unittestreport import ddt,list_data

@ddt  #声明使用ddt数据驱动

class testlog98(unittest.TestCase):

    @list_data(cases)  #声明使用那个用例数据

    def testxx(self,case):   #case表示每次从cases取一个元素  类似for循环

        data1=case["data"]  #每个用例里的值 data的值  里有usname,和pwd
        logger.info("运行结果")
        data=eval(data1)  #取的每个用例值都是字符串，需要转换成字典
        actual=testlogA(data["usname"],data["pwd"])  #从每个用例里的data  取usname ，pwd


        expected=case["expected"]   #用例的预期结果
        expected = eval(expected)   #预期结果也是字典，要转换字典

        try:
            self.assertEqual(expected,actual)  #对比两个结果
        except AssertionError as e:
            logger.error(f"错误的断言结果{e}")
            raise   #手动抛出异常
        print(actual)