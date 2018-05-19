import unittest
from unit_conversion import UnitConversion


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_01_convert_bytes_test(self):
        b = 409600000333000
        r = UnitConversion.bytes_to_str(b, True)
        self.assertEqual(r, '372.53tb')
        r = UnitConversion.bytes_to_str(b, False)
        self.assertEqual(r, '409.6tb')

    def test_02_convert_string_test(self):
        r = UnitConversion(True)._convert_string(372.53, 'TB')
        r2 = UnitConversion.str_to_bytes('372.53tb')
        self.assertEqual(r, r2)
        print(r, r2)

    def test_03_convert_string_invalid(self):
        r = UnitConversion.str_to_bytes('33 MB')
        print(r)


if __name__ == '__main__':
    unittest.main()
