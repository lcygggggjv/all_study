

import pathlib

from pymysql.cursors import DictCursor

from test_项目搭建5.read_excel.read_excel1 import read_excel


class Config:


    file_dir=pathlib.Path(__file__).absolute().parent   #绝对路径

    father_dir=file_dir.parent   #项目目录

    rots_dir=father_dir.parent  #根目录


    test_dir= rots_dir / father_dir / 'test_case' / 'cases.xlsx'     #用例所在位置


    log_dir= rots_dir /father_dir / 'test_Log' / 'test_log'

    host='http://mall.lemonban.com:8108'

    front_host='http://mall.lemonban.com:8107'

    host_usname='student'

    host_pwd='123456a'

    db = dict(user='lemon',
              password='lemon123',
              host='47.113.180.81',
              port=3306,
              cursorclass=DictCursor,  # 导入dictcursor类  得到字典
              db='yami_shops')

    sql = f'select user_id, mobile_code from  tz_sms_log  limit  2'

    fxpath=r'D:\pycharm-workspace\test_class\test_uploa产品\tx_连接数据库.png'

    front_usname='15675500781'

    front_pwd='123456'



if __name__ == '__main__':

    d=Config()

    s=read_excel(d.test_dir)
    print(s)



