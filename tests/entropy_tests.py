import unittest
from common_utils import SleepUtil


class SleepUtilCase(unittest.TestCase):
    def random_int_test(self):
        v = SleepUtil.random_int(15)
        self.assertGreater(v, 0)
        self.assertLess(v, 15)
        self.assertEqual(type(v), int)

    def random_sleep_test(self):
        SleepUtil.random_sleep(3)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
