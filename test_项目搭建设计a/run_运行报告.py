

import unittestreport
import unittest

site2=unittest.defaultTestLoader.discover("test_类ddt")


runs=unittestreport.TestRunner(site2, title='报告bug',
                 tester='测试小李',
                 desc="超级大的报告",
                 templates=3)
runs.run()