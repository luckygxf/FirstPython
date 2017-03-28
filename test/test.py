#encoding=utf-8
import sys
import logging

import json
import logging.config
import os


reload(sys)
sys.setdefaultencoding('utf-8')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + '\t' + str(self.age)

def setup_logging(default_path='logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('info message')
    logger.error('error message')