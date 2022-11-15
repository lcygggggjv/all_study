

from loguru import logger

from test_project_6.config.configs import config


logger.add(config.logs_file,encoding='utf-8')

