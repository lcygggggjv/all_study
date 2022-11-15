


from loguru import logger

from test_pytest.Config.config import Config

logger.add(Config.log_dir,encoding='utf-8')
