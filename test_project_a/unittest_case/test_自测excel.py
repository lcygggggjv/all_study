
from test_project_a.common.excel_2封装函数 import read2_excel

def test_excel2():
    fspath=r"D:\pycharm-workspace\test_项目搭建设计\data_测试用例\case4.xlsx"
    data=read2_excel(fspath)
    print(data)

test_excel2()