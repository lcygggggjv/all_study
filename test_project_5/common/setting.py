
from  loguru import logger

from test_项目搭建4.config.config import config

logger.add(config.log_file,encoding="utf-8")
