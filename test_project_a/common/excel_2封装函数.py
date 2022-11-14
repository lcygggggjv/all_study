
import openpyxl

from  openpyxl.worksheet.worksheet import Worksheet

from test_项目搭建设计.config.setting import Config

def read2_excel(filename,sheetname="Sheet1"):

    workbook=openpyxl.load_workbook(filename)

    sheet: Worksheet =workbook[sheetname]

    data=list(sheet.values)

    title=data[0]
    rows=data[1:]

    data=[dict(zip(title,row) )for row in rows]

    return data

filed=Config.CASE_FILE

cases=read2_excel(filed)


#单元测试自测

#1  当你想测试这个模块功能时候，单独调用点击，执行下面代码
#  2当其他模块调用这个模块时候，下面测试代码不会执行
#  模块当中就是只有各种定位，函数，类中
# if __name__ =="__main__":
#     fspath = Config.CASE_FILE
#     data = read2_excel(fspath)
#     print(data)
#

