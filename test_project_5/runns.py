

import unittest
import unittestreport


sites=unittest.defaultTestLoader.discover('test_uintestCase')   #这里写的路径是登录函数接口的目录地址

# print(sites)

s2=unittestreport.TestRunner(sites,
                 title='接口自动化报告',
                 tester='测试小李',
                 desc="接口项目自动化",
                 templates=3)
s2.run()