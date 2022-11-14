

from loguru import logger

from test_项目搭建5.config.configs import config


logger.add(config.logs_file,encoding='utf-8')

