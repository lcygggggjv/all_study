

import openpyxl

from  openpyxl.worksheet.worksheet import Worksheet

from test_project_5.config.config import config

def read_excels(filename,sheetname="Sheet1"):

    workbook=openpyxl.load_workbook(filename)

    sheet:Worksheet  =workbook[sheetname]

    data=list(sheet.values)

    title=data[0]

    rows=data[1:]

    data=[dict(zip(title,row))  for  row  in  rows]

    return data

case22=read_excels(config.file_dir)
print(case22)


if __name__=="__main__":

    fspath=r"D:\pycharm-workspace\test_项目搭建4\cases_用例\case_login登录2.xlsx"

    ts=read_excels(fspath)
    print(ts)

