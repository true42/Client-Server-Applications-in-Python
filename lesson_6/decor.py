import sys
import log.client_log_config
import log.server_log_config
import logging

if 'server.py' in sys.argv[0]:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func):
    def func_to_log(*args, **kwargs):
        res = func(*args, **kwargs)
        LOGGER.debug(f'Вызвана функция {func.__name__} с аргументами {args},{kwargs}')
        return res
    return func_to_log
