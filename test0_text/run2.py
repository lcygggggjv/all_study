
#
# import unittest
# import unittestreport
#
# ras=unittest.defaultTestLoader.discover('test7')
# print(ras)
#
# ko=unittestreport.TestRunner(ras,filename="report.html",
#                  report_dir="./reports",
#                  title='lcy的',
#                  tester='lcy',
#                  desc="不错的项目",
#                  templates=2)
#
# ko.run()


#导入模块 configparser   import  ConfigParser   后面的首字母大写
from configparser import  ConfigParser

parser=ConfigParser()    #parser=configparser（） 方法
parser.read("test_ini.ini",encoding="utf-8")  #读取文件

lcy=parser.get("salary","k")   #通过parser.get获取对应的上面{]内容，左边以及变量
print(lcy)   #所有打印出来的都是字符串，  转换  ，不支持注释
