
import unittest
from loguru import logger

logger.add(sink="py65",level="INFO",encoding="utf-8")

def testlog(usname,pwd):
    reponse={"message":None,"code":None,"token":None}

    if usname=="lcy"  and pwd==6666:
        reponse["message"]="登录成功"
        reponse["code"]=200
        reponse["token"]="best token"
        return reponse

    elif usname=="":
        reponse["message"]="用户名为空"
        reponse["code"]=301
        reponse["token"]="bad token"
        return reponse

    elif pwd=="":
        reponse["message"]="密码为空"
        reponse["code"]=302
        reponse["token"]="old token"
        return reponse

    else:
        reponse["message"]="用户名或密码错误"
        reponse["code"]=401
        reponse["token"]="fxxk token"
        return reponse


caseA={"usname":"lcy","pwd":6666,"expected":{"message":"登录成功","code":200,"token":"best token"}}
caseB={"usname":"","pwd":6666,"expected":{"message":"登录失败","code":301,"token":"bad token"}}
caseC={"usname":"lcy","pwd":"","expected":{"message":"密码为空","code":302,"token":"old token"}}
caseD={"usname":"lcy2","pwd":66669,"expected":{"message":"用户名或密码错误","code":401,"token":"fxxk token"}}


class testloog(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("每个类用例前执行一次，前置")
    @classmethod
    def tearDownClass(cls) -> None:
        print("每个类用例之后执行一次，后置")


    def setUp(self) -> None:
        print("每次用例执行一次，连接数据库")

    def tearDown(self) -> None:
        print("每次用例后都执行，断开数据库")



    def test11(self):

        expected=caseA["expected"]   #预期结果  key取值
        actual=testlog(caseA["usname"],caseA["pwd"])  #实际结果  调用函数，输入对应用例name，pwd

        try:
            self.assertTrue("codes" in actual)  #断言excepted再actual里

        except AssertionError as e:
            logger.error(f"断言失败结果{e}")   #存储失败日志
            raise e   #手动抛出异常
        print(actual)

    def test22(self):

        expected = caseB["expected"]
        actual = testlog(caseB["usname"], caseB["pwd"])

        # msg:f"""expected:{expected}
        #         actual:{actual}
        #                               断言相同，msg对比两个
        #         """
        # assert expected==actual, msg

        try:
            self.assertEqual(expected,actual) #断言相等的

        except AssertionError as e:
            logger.error(f"断言失败结果{e}")
            raise e
        print(actual)

    def test33(self):

        logger.info("运行正常的")

        expected = caseC["expected"]
        actual = testlog(caseC["usname"], caseC["pwd"])

        try:
            self.assertEqual(expected,actual)

        except AssertionError as e:
            logger.error(f"断言用例3{e}")
            raise e
        print(actual)


    def test55(self):

        logger.info("运行正常的")

        expected = caseD["expected"]
        actual = testlog(caseD["usname"], caseD["pwd"])

        try:
            self.assertIn(expected , actual)  #断言预期在不在里面实际

        except AssertionError as e:
            logger.error(f"断言用例5结果{e}")
            raise e
