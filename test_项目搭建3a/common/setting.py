



from loguru import logger
from test_项目搭建3.config.Config import config


logger.add(config.log_info,encoding="utf-8")

