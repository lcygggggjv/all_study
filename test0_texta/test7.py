import unittest


def check(usname,pwd):
    response={'message':None,'code':None,'token':None}

    if usname=='xxx'  and pwd==1234:
        response['message']='登录成功'
        response['code']=200
        response['token']='zz'
        return response
    elif usname=='':
        response['message']='用户名为空'
        response['code']=401
        response['token']='error'
        return response
    elif pwd=='':
        response['message']='密码为空'
        response['code']=401
        response['token']='error'
        return response
    else:
        response['message']='用户名或密码错误'
        response['code']=401
        response['token']='error'
        return response



case1={'usname':'xxx','pwd':1234,'expected':{'message':'登录成功','code':200,'token':'zz'}}
case2={'usname':'','pwd':1234,'expected':{'message':'用户名为空','code':401,'token':'xxx'}}
case3={'usname':'xxx','pwd':'','expected':{'message':'密码为空','code':401,'token':'xxx'}}
case4={'usname':'lcy','pwd':12345,'expected':{'message':'用户名或密码错误','code':401,'token':'xxx'}}
case5={'usname':'lcy2','pwd':123456,'expected':{'message':'用户名或密码错误2','code':401,'token':'xxx'}}





class testlogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:  #比如testlogin类，只执行一次
        print('每个类执行一次前置')

    @classmethod
    def tearDownClass(cls) -> None:

        print('每个类执行一次后置')


    def setUp(self) -> None:  #前置操作   每个用例执行之前unittest都会setup
        print('连接数据库')

    def tearDown(self) -> None:  #后置操作  每个用例执行后unittest都会teardown
        print('断开数据库')


    def test_2_login1(self):
        expected=case1['expected']
        actual=check(case1['usname'],case1['pwd'])

        self.assertEqual(expected,actual)


    def test2_login2(self):
        expected=case2['expected']
        actual=check(case2['usname'],case2['pwd'])

        # info=f"""expected:{expected}
        #         actualL:{actual}
        #             """
        # assert expected==actual ,info
        self.assertEqual(expected, actual)

    def test2_login3(self):
        expected = case3['expected']
        actual = check(case3['usname'], case3['pwd'])

        # info = f"""expected:{expected}
        #         actualL:{actual}
        #             """
        # assert expected == actual, info
        self.assertEqual(expected, actual)

    def test2_login4(self):
        expected=case4['expected']
        actual=check(case4['usname'],case4['pwd'])

        # info=f"""expected:{expected}
        #         actualL:{actual}
        #             """
        # assert expected==actual ,info
        self.assertEqual(expected, actual)

    def test2_login5(self):
        expected = case5['expected']
        actual = check(case5['usname'], case5['pwd'])

        # info=f"""expected:{expected}
        #         actualL:{actual}
        #             """
        # assert expected==actual ,info
        self.assertEqual(expected, actual)