import unittest
import os
from common_utils import FileUtil


class FileUtilTestCase(unittest.TestCase):
    def setUp(self):
        self.test_obj = {'sample': 'test', 'item': 'whatever', 'other': ['1', 2, 'name']}
        self.pickle_obj_test_file1 = 'sample1.pkl'
        self.string_file = 'samplefile.txt'
        self.sample_string = 'lorum ipsum domafalfjsdalfjl'
        self.sample_json_string = """
        {
            "sample": [
                "data_point"
            ]
        }
        """

    def test_01_pickle(self):
        FileUtil.pickle_obj(obj=self.test_obj, filename=self.pickle_obj_test_file1)
        self.assertTrue(os.path.exists(self.pickle_obj_test_file1))

    def test_02_pickle(self):
        FileUtil.pickle_obj(obj=self.test_obj, filename=self.pickle_obj_test_file1)
        o = FileUtil.unpickle_obj(self.pickle_obj_test_file1)
        self.assertEqual(self.test_obj, o)

    def test_03_file(self):
        FileUtil.write_file(self.sample_string, self.string_file, 'w')
        self.assertTrue(os.path.exists(self.string_file))

    def test_04_file(self):
        FileUtil.write_file(self.sample_string, self.string_file, 'w')
        s = FileUtil.read_file(self.string_file, 'r')
        self.assertEqual(self.sample_string, s)

    def test_05_json(self):
        o = FileUtil.json_loads(self.sample_json_string)
        self.assertEqual(type(o), dict)
        self.assertEqual(o.get('sample'), ['data_point'])

    def test_06_json(self):
        s = FileUtil.json_dumps(self.test_obj)
        self.assertTrue(s)

    def tearDown(self):
        if os.path.exists(self.pickle_obj_test_file1):
            os.remove(self.pickle_obj_test_file1)
        if os.path.exists(self.string_file):
            os.remove(self.string_file)


if __name__ == '__main__':
    unittest.main()
