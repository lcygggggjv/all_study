import requests
from common.excel import read_excel_dict
import unittest
from unittestreport import ddt,list_data
from common.log_handler import logger
from config.setting import Config
import json
from api.apis import adminLogin

# 读取 cases.xlsx 表格的数据，得到所有的测试数据，保存到 cases 变量
# data_file = r"E:\pythonProject\Test\PyTest11\data\cases.xlsx"

# 从配置文件导入用例文件
data_file = Config.CASE_FILE3
cases = read_excel_dict(data_file, "addProduct")

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        """登录"""
        token = adminLogin(Config.username, Config.password)
        self.token = token  # 设置属性


    @list_data(cases)
    # @list_data(cases[2:3]) 运行第三个用例，可以用来调试 debug，来解决问题
    def test_add_product(self, item):
        # case 表示每次从 cases 当中取出来一个元素
        data_str = item["json"]
        logger.info("正在测试.....")

        # json字符串转成字典
        # data = eval(data_str)
        data = json.loads(data_str)

        # 获取headers
        # headers = item["headers"]
        headers = {"Authorization": f"bearer{self.token}"}

        # url拼接域名
        url = Config.HOST + item["url"]

        # 发起请求
        response = requests.request(url=url,
                                    method=item["method"],
                                    headers=headers,
                                    json=data)
        # 得到响应体
        try:
            actual = response.json()   # 返回的是字典
        except Exception as e:
            # Incorrect account or password, 通过json 获取响应发生异常，则通过 text 获取
            actual = response.text
            # 转换为字典，补一个键, {"msg": "Incorrect account or password"}
            actual = {"msg": actual}

        # print(actual)  # 字典

        # 从excel读取的数据是 str
        # expected = eval(item["expected"])
        # json 字符串转换为字典
        expected = json.loads(item["expected"])

        # 预期结果：  {"token_type":"bearer"}   可断言两次或更多，在字典中 再添加对应次的 键值即可
        """  实际结果： {'access_token': '9f9db761-cd57-4b08-bcea-85f25081a24c', 'token_type': 'bearer', 
                       'refresh_token': 'a557d46f-1dbb-4e68-ab86-f33aed3e28a4', 'expires_in': 1295999}  """

        # 取出msg 的值与预期结果断言
        # self.assertEqual(actual["msg"], expected)

        # 循环 实际结果的值 与预期结果的值 是否相等
        for k, v in expected.items():
            self.assertEqual(actual[k], v)
