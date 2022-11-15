

# 1、写一个测试用例，让断言不通过。
#
# 2、使用异常捕获断言错误
#
# 3、通过日志记录用例执行过程，至少包含一个info和error的日志。
#
# 4、日志保存到 py53.log 文件当中
#
# 注意：上传作业不需要压缩，直接上传文件夹，并且附带代码的目录结构截图 以及 运行结果的小视频。

import unittest
from loguru import logger
logger.add(sink='py53',encoding='utf-8',level='INFO')

def test_case(usname,pwd):
    response={'message':None,'code':None,'token':None}
    if usname=='lcy' and pwd==123456:
        response['message']='登录成功'
        response['code']=200
        response['token']='great token'
        return response
    elif usname=='':
        response['message'] = '用户名为空'
        response['code'] = 401
        response['token'] = 'bad token'
        return response
    elif pwd=='':
        response['message'] = '密码为空'
        response['code'] = 401
        response['token'] = 'bad token'
        return response
    else:
        response['message'] = '用户名或密码错误'
        response['code'] = 401
        response['token'] = 'bad2 token'
        return response


case1={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}
case2={'usname':'lcy','pwd':123456,'expected':{'message':'登录成功','code':200,'token':'great token'}}
case3={'usname':'lcy','pwd':123456,'expected':{'message':'mm','code':201,'token':'great token'}}

class testlogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('每次用例前只执行一次')

    @classmethod
    def tearDownClass(cls) -> None:
        print('每次用例后只执行一次')

    def setUp(self) -> None:
        print('每次用例执行一次，连接')

    def tearDown(self) -> None:
        print('每次用例执行之后一次，断开')


    def test_11(self):
        actual=test_case(case1['usname'],case1['pwd'])
        logger.info('记录下面的运行结果1')
        expected=case1['expected']

        try:
            self.assertEqual(actual,expected)  #判断预期和实际想不想等
            print(actual)
        except AssertionError as e:
            logger.error(f'断言等于失败的结果{e}')
            raise e  #手动异常捕获异常

    def test_12(self):
        logger.info('记录下面的运行结果2')
        actual = test_case(case2['usname'], case2['pwd'])
        expected=case2['expected']
        print(actual)    #放在里面不成功，跳except  这条用例不执行，相当于if  不满足条件，跳过
        try:
            self.assertTrue('coding' in actual)   #断言某x在不在actual里

        except AssertionError as e:
            logger.error(f'断言coding在actual结果{e}')
            raise e
        print(actual)  #放在最后执行

    def test_76(self):
        logger.info('记录写的')
        actual=test_case(case3['usname'],case3['pwd'])
        expected=case3['expected']
        try:
            self.assertIn(id,actual)

        except AssertionError as e:
            logger.error(f'断言3的{e}')
            raise e

        print(actual)