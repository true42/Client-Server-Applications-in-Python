import json
import sys
import time
import argparse
import logging
import log.client_log_config
from socket import socket, AF_INET, SOCK_STREAM
from common.variables import DEFAULT_PORT, DEFAULT_IP_ADDRESS, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from common.utils import send_message, get_message
from decor import log

CLIENT_LOGGER = logging.getLogger('client')

@log
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.strftime('%a, %d %b %Y %H:%M:%S', time.gmtime()),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


@log
def process_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser


def main():

    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    if not 1023 < server_port < 65536:
        CLIENT_LOGGER.critical(f'Запуск сервера с порта {server_port}. '
                               f'Допустимые значения с 1024 до 65535.')
        sys.exit(1)
    CLIENT_LOGGER.info(f'Адрес сервера: {server_address}, порт: {server_port}')

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        CLIENT_LOGGER.info(f'Принято сообщение от сервера {answer}')
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.error('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
