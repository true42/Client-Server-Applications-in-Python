import os.path
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from client import process_ans, create_presence
from common.variables import RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, ACTION, PRESENCE, TIME, USER, \
    ACCOUNT_NAME


class TestClient(unittest.TestCase):
    error_str = '400 : error'

    ok_str = '200 : OK'

    def test_create_presence(self):
        test_presence = create_presence('Guest')
        test_presence[TIME] = 1.1
        self.assertEqual(test_presence, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_ok(self):
        self.assertEqual(process_ans({RESPONSE: 200}), self.ok_str)

    def test_error(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: ERROR}), self.error_str)

    def test_value_error(self):
        self.assertRaises(ValueError, process_ans, {'NOT_RESPONSE': 'Results'})


if __name__ == '__main__':
    unittest.main()
