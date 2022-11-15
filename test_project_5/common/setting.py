
from  loguru import logger

from test_project_5.config.config import config

logger.add(config.log_file,encoding="utf-8")
