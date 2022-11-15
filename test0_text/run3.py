import unittest
import unittestreport

suit1=unittest.defaultTestLoader.discover('test666')
print(suit1)

rds=unittestreport.TestRunner(suit1,filename="report6.html",
                 report_dir="./reports",
                 title='lcy666报告',
                 tester='lcy',
                 desc="lcy自主研发",
                 templates=2)
rds.run()
