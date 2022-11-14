
import openpyxl  #导入openpyxl库

from openpyxl.worksheet.worksheet import Worksheet  #导入worksheet方法

def read_excel(filename,sheetname="adminLogin"):   #用例文件，sheet页位置传参

    test_cases=openpyxl.load_workbook(filename)  #使用load_workbook方法导入excel用例

    sheet: Worksheet =test_cases[sheetname]   #使用worksheet方法取读取的用例里  对应sheet页内容

    data=list(sheet.values)    #取sheet值非列表/，需要转成列表，

    title=data[0]   #取excel第一行表头数据
    rows=data[1:]   #取除了第一行剩余的所有数据

    data=[dict(zip(title,row)) for row in rows]   #通过for循环，把剩余的数据一一对应，用zip函数，把表头和循环的所有值，压缩。最后转换成字典,外面套列表

    return data  #记得返回值



if __name__ == '__main__':   #自测函数

    xspath=read_excel(r'D:\pycharm-workspace\test_pytest\test_case\cases.xlsx')

    print(xspath)