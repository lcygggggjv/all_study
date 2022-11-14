

import pathlib
from pymysql.cursors import DictCursor

class config:

    file_dir=pathlib.Path(__file__).absolute().parent   #绝对路径


    # files=pathlib.Path(__file__).absolute().parent

    father_dir=file_dir.parent

    rooots_dir=father_dir.parent

    excel_file= rooots_dir / father_dir / 'test_cases用例' / 'case_login登录2.xlsx'

    logs_file= rooots_dir  / father_dir / 'log_运行日志' / 'make_logs'

    prod_file= rooots_dir / father_dir /  'test_cases用例'  /  'case产品1.xlsx'


    excels_product= rooots_dir / father_dir / 'test_cases用例' / 'cases_prod用例.xlsx'

    product = rooots_dir / father_dir / 'test_cases用例' / '产品12.xlsx'

    pay= rooots_dir  / father_dir  / 'test_cases用例'  / 'cases.xlsx'


    prod_usname='student'

    prod_pwd='123456a'



    img=r'D:\pycharm-workspace\test9\test_uploa产品\tx_连接数据库.png'

    host='http://mall.lemonban.com:8108'

    front_host='http://mall.lemonban.com:8107'

    db=dict(user='lemon',
            password='lemon123',
            host='47.113.180.81',
            port=3306,
            cursorclass=DictCursor,   #导入dictcursor类  得到字典
            db='yami_shops')

    product_username='15675500781'

    product_pwd='123456'