import unittest
from common_utils import Base64Util


class Base64UtilCase(unittest.TestCase):
    def setUp(self):
        self.sample_password = 'password123'
        self.sample_b64encode_string = 'cGFzc3dvcmQxMjM='

    def b64encode_value_test(self):
        v = Base64Util.base64_encode_str(self.sample_password)
        self.assertEqual(v, self.sample_b64encode_string)

    def b64decode_value_test(self):
        v = Base64Util.base64_decode_str(self.sample_b64encode_string)
        self.assertEqual(v, self.sample_password)


if __name__ == '__main__':
    unittest.main()
