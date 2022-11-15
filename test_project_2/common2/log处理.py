from loguru import logger

from test_project_2.config.seetin_常用变量 import Config

logger.add(Config.Log_file,encoding="utf-8")