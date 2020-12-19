import unittest
from hh_import.get_raw_hh_from_file.run import *





# USE FAKE DATA INSTEAD `!!!!! NO REAL CALLS TO FUNCTIONS !!!!

class TESTS_get_new_raw_hh_from_file(unittest.TestCase):
    def test_task_4(self):
        all_in_folder = ['a', 'b', 'c', 'd', 'e']
        already_in_db = ['a', 'b', 'c', 'd']
        self.assertTrue(task_4(all_in_folder, already_in_db) == ['e'])



if __name__ == '__main__':
    unittest.main()
