

import logging

def get_logger(log_name='py55',level_name="INFO",filename="default.log"
               ,fors="%(asctime)s  | %(levelname)s | %(filename)s - %(message)s"):

    logger=logging.getLogger(log_name)
    logger.setLevel(level_name)

    handler=logging.StreamHandler()
    handler.setLevel(level_name)

    logger.addHandler(handler)



    fmt=logging.Formatter(fors)
    handler.setFormatter(fmt)

    if filename!=None:
        file_name = logging.FileHandler(filename=filename, encoding='utf-8')
        file_name.setLevel(level_name)

        logger.addHandler(file_name)
        file_name.setFormatter(fmt)

    return logger

