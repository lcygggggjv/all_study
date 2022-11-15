

from loguru import logger


from test_project_a.config.setting import Config

logger.add(Config.LOG_FILE,encoding="utf-8")  #配置文件里的文件，变量名

