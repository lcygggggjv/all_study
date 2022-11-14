

from loguru import logger


from test_项目搭建设计.config.setting import Config

logger.add(Config.LOG_FILE,encoding="utf-8")  #配置文件里的文件，变量名

