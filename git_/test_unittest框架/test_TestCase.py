
import unittest
import unittestreport
from test_项目搭建2.test_被测函数.test_logs函数 import logins
from test_项目搭建2.test_读取excel.test_excel import reads_excel
from unittestreport import ddt,list_data
from test_项目搭建2.config.seetin_常用变量 import Config
from test_项目搭建2.common2.log处理 import logger
from test_项目搭建2.aps_接口s.api_接口 import logink


ca=Config.File_name
cases=reads_excel(ca)

@ddt
class test_12(unittest.TestCase):

    @list_data(cases)
    def test_kk(self,case):

        data1=case["data"]
        data=eval(data1)
        logink_actual=logink(data["usname"],data["pwd"])  #函数整个响应体
        actual=logink_actual["data"]["msg"]   #取响应里的msg信息：登录成功，用例需要对应修改预期结果

        logger.info("运行结果")
        expected=case["expected"]
        expected=eval(expected)

        try:
            self.assertEqual(expected,actual)  #判断相等
           # self.assertIn(expected,actual)  不过滤那整个响应体 判断实际结果，在不在预期里面

        except AssertionError as e:
            logger.error(f"断言错误{e}")
            raise e
        print(actual)



