

import unittest

import unittestreport

from test_项目搭建3.config.Config import config

sites=unittest.defaultTestLoader.discover("test_login函数")

rea=unittestreport.TestRunner(sites,  title='商城管理登录报告',
                 tester='测试小李',
                 desc="登录测试报告",
                 templates=3)

rea.run()