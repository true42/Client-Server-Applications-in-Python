import os.path
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from server import process_client_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR


class TestServer(unittest.TestCase):

    error_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    ok_dict = {
        RESPONSE: 200
    }

    def test_response_ok(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.ok_dict)

    def test_no_action(self):
        self.assertEqual(process_client_message(
            {TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.error_dict)

    def test_action_error(self):
        self.assertEqual(process_client_message(
            {ACTION: 'error', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.error_dict)

    def test_no_time(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.error_dict)

    def test_no_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1}), self.error_dict)

    def test_account_name_unknown(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'test'}}),
            self.error_dict)


if __name__ == '__main__':
    unittest.main()
