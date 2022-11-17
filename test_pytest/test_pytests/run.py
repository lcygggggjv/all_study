

import pytest


#pytest  主程序  收集全部的用例


#把所有参数 都放到列表当中  空格也是元素

args=['--html=output.html']
pytest.main(args)