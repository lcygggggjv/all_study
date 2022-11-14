

import unittestreport
import unittest

sits=unittest.defaultTestLoader.discover(r'D:\pycharm-workspace\test_项目搭建5\test_unittest')

print(sits)

# ad=unittestreport.TestRunner(sits, title='登录报告',
#                  tester='测试渣渣',
#                  desc="登录测试总结",
#                  templates=3)
#
# ad.run()