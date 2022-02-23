import sys
import os
import logging
import logging.handlers
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import LOG_LEVEL

SERVER_FORMATTER = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

STREAM_HAND = logging.StreamHandler(sys.stderr)
STREAM_HAND.setFormatter(SERVER_FORMATTER)
STREAM_HAND.setLevel(logging.ERROR)

LOG_FILE_HAND = logging.handlers.RotatingFileHandler(PATH, encoding='utf-8', maxBytes=1048576, backupCount=1)
LOG_FILE_HAND.setFormatter(SERVER_FORMATTER)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HAND)
LOGGER.addHandler(LOG_FILE_HAND)
LOGGER.setLevel(LOG_LEVEL)

if __name__ == '__main__':
    LOGGER.info('Информационное сообщение')
    LOGGER.warning('Предупреждение')
    LOGGER.error('Ошибка')
    LOGGER.critical('Критическое сообщение')
