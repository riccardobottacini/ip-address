import os
import unittest

from scripts.csv_readers import read_csv


class TestCSVReaders(unittest.TestCase):

    def setUp(self):
        self.temporary_file = 'temporary_file'
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        df = read_csv('thisfiledoesnotexist')
        self.assertFalse(df)

    def test_empty_datafile(self):
        df = read_csv(self.temporary_file)
        self.assertFalse(df)

    def test_file_is_not_csv(self):
        df = read_csv(self.temporary_file)
        self.assertFalse(df)

    def tearDown(self):
        os.remove(self.temporary_file)


if __name__ == '__main__':
    unittest.main(verbosity=2)
