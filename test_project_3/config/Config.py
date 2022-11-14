

import pathlib  #导入的




class config:

    config_dir=pathlib.Path(__file__).absolute().parent   #先找自己上一级，就是packbage包，config

    root_dir=config_dir.parent  #config里的上一级  项目所在根
    root_dir1=root_dir.parent


    filename=root_dir1 / root_dir / 'test_case用例存储'   /  'case_login登录.xlsx'    #向下拼接 从根开始 root_dir /  用例父级  /用例

    log_info= root_dir1 / root_dir / 'logs_日志存储'  / 'logs_日志存储\py001_log日志'    #向下拼接 从根开始 root_dir /  日志父级  /日志
