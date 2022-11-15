
# 使用正则表达式 进行替换
# 调用apis_2,类的方式
import requests

from api.apis_2 import API
from common.excel import read_excel_dict
import unittest
from unittestreport import ddt,list_data
from common.helper import replace_data, Data
from common.log_handler import logger
from config.setting import Config
import json
# from api.apis import generate_sms_code, check_sms_code, generate_mobile
# 从配置文件导入用例文件
data_file = Config.CASE_FILE4
cases = read_excel_dict(data_file, "register")

@ddt
class TestRegister(unittest.TestCase, API):  # 继承 API, 多层继承
    def setUp(self) -> None:
        """前置"""
        # 生成验证码
        self.__class__.mobile = self.generate_mobile() # 设置类属性
        validcode = self.generate_sms_code(self.mobile)
        # 验证验证码
        self.__class__.checkRegisterSmsFlag = self.check_sms_code(self.mobile, validcode)
        self.__class__.userName = self.__class__.mobile

        # 设置 Data, 设置临时变量的属性
        # Data.checkRegisterSmsFlag = self.sms_flag
        # Data.mobile = self.mobile
        # Data.userName = self.mobile

    @list_data(cases)
    def test_register(self, item):
        # case 表示每次从 cases 当中取出来一个元素
        data_str = item["json"]
        logger.info("正在测试.....")

        # 替换其中的变量为具体的值
        # data_str = data_str.replace("#checkRegisterSmsFlag#", self.sms_flag)
        # data_str = data_str.replace("#mobile#", self.mobile)
        # data_str = data_str.replace("#userName#", self.mobile)
        #使用 正则表达式 进行数据替换
        data_str = self.replace_data(data_str)

        # json字符串转成字典
        data = json.loads(data_str)
        # 获取headers
        # headers = {"Authorization": f"bearer{self.token}"}

        # url拼接域名
        url = Config.FRONT_HOST + item["url"]
        # 发起请求
        response = requests.request(url=url, method=item["method"],  # headers=headers,
                                    json=data)
        # 得到响应体
        try:
            actual = response.json()   # 返回的是字典
        except Exception as e:
            # Incorrect account or password, 通过json 获取响应发生异常，则通过 text 获取
            actual = response.text
            # 转换为字典，补一个键, {"msg": "Incorrect account or password"}
            actual = {"msg": actual}
        # print(actual)
        # 从excel读取的数据是 str
        # json 字符串转换为字典
        expected = json.loads(item["expected"])
        # 循环 实际结果的值 与预期结果的值 是否相等
        for k, v in expected.items():
            self.assertEqual(actual[k], v)
