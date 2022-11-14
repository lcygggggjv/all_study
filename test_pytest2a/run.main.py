


import unittestreport

import unittest


site=unittest.defaultTestLoader.discover(r'D:\pycharm-workspace\test_项目搭建6\test_单项unittest')  #这里取，uinttest那里的路径目录

print(site)

runs=unittestreport.TestRunner(site,
                               title='测试报告',
                                tester='测试员',
                                desc="XX项目测试生成的报告",
                                templates=3)
runs.run()