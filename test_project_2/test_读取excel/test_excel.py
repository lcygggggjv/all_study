
import unittest
from test_project_2.config.seetin_常用变量 import Config
from test_project_2.test_被测函数.test_logs函数 import logins

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

def reads_excel(filename,sheetname="Sheet1"):

    workbook=openpyxl.load_workbook(filename)

    sheet:Worksheet = workbook[sheetname]

    data=list(sheet.values)

    title=data[0]
    rows=data[1:]

    data=[dict(zip(title,row)) for row in rows ]

    return data   #一定要return  data  返回值

# ca=setins.File_name
#
# cases=reads_excel(ca)

if __name__=="__main__":   #单元自测
    ca=Config.File_name
    asd=reads_excel(ca)
    print(asd)