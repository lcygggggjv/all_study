

import openpyxl

from openpyxl.worksheet.worksheet import Worksheet

def read_book(filename,sheetname="Sheet1"):

    workbook=openpyxl.load_workbook(filename)

    sheet: Worksheet=workbook[sheetname]

    data=list(sheet.values)

    title=data[0]
    rows=data[1:]

    data=[dict(zip(title,row))  for row in rows]

    return data


from test_项目搭建3.config.Config import config

if __name__=="__main__":

    fspath=config.filename

    data=read_book(fspath)

    print(data)