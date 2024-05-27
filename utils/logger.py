"""
logger
"""

import logging


def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up the logger
    :param name:
    :param log_file:
    :param level:
    :return:
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
