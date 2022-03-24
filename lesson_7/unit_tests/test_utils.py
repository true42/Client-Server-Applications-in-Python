import os.path
import sys
import unittest
import json

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import MAX_PACKAGE_LENGTH, ENCODING, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from common.utils import send_message, get_message


class TestSocket:
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        if isinstance(json.loads(message_to_send.decode(ENCODING)), dict):
            json_test_message = json.dumps(self.test_dict)
            self.encoded_message = json_test_message.encode(ENCODING)
            self.received_message = message_to_send
        else:
            raise TypeError

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {ACCOUNT_NAME: 'test'}
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_error = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message_ok(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_error(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, "not_dict")

    def test_get_message_ok(self):
        test_socket = TestSocket(self.test_dict_recv_ok)
        self.assertEqual(get_message(test_socket), self.test_dict_recv_ok)

    def test_get_message_error(self):
        test_socket = TestSocket(self.test_dict_recv_error)
        self.assertEqual(get_message(test_socket), self.test_dict_recv_error)


if __name__ == '__main__':
    unittest.main()
