from loguru import logger

from test_项目搭建2.config.seetin_常用变量 import Config

logger.add(Config.Log_file,encoding="utf-8")