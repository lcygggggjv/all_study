
import pathlib



class config:

    bs_dir= pathlib.Path(__file__).absolute().parent
    sj_dir=bs_dir.parent
    rot_dir=sj_dir.parent

    host ='http://mall.lemonban.com:8108'

    HOST='http://mall.lemonban.com:8107'

    file_dir =rot_dir / sj_dir  / 'cases_用例'  / 'case_login登录2.xlsx'

    log_file= rot_dir  / sj_dir / 'log_日志'  /  'log_记录'