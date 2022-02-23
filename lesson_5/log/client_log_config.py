import sys
import os
import logging
import logging.handlers
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import LOG_LEVEL

CLIENT_FORMATTER = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

STREAM_HAND = logging.StreamHandler(sys.stderr)
STREAM_HAND.setFormatter(CLIENT_FORMATTER)
STREAM_HAND.setLevel(logging.ERROR)

LOG_FILE_HAND = logging.FileHandler(PATH, encoding='utf-8')
LOG_FILE_HAND.setFormatter(CLIENT_FORMATTER)

LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM_HAND)
LOGGER.addHandler(LOG_FILE_HAND)
LOGGER.setLevel(LOG_LEVEL)

if __name__ == '__main__':
    LOGGER.info('Информационное сообщение')
    LOGGER.warning('Предупреждение')
    LOGGER.error('Ошибка')
    LOGGER.critical('Критическое сообщение')
