import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    format='%(asctime)s,%(msecs)03d [%(name)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(filename='./logs/producer.log',
                            maxBytes=5 * 1024 * 1024,
                            backupCount=2,
                            delay=0),
    ],
)


def get_logger(class_name):
    return logging.getLogger(class_name)
