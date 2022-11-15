

from test_project_2.test_读取excel.test_excel import reads_excel
from test_project_2.config.seetin_常用变量 import Config
from test_project_2.common2.log处理 import logger


def unit():

    fspath=Config.File_name
    fs=reads_excel(fspath)
    print(fs)


unit()