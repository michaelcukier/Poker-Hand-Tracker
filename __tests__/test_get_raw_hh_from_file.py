import unittest
from hh_import.get_raw_hh_from_file import *





# USE FAKE DATA INSTEAD `!!!!! NO REAL CALLS TO FUNCTIONS !!!!




class TESTS_get_new_raw_hh_from_file(unittest.TestCase):



    def test_task_1(self):
        self.assertEqual(type(task_1()), list)
        for id in task_1():
            self.assertEqual(type(id), int)
            self.assertEqual(len(str(id)), 8)
        self.assertTrue(len(task_1()) == len(set(task_1())))

    def test_task_3(self):
        filenames = task_2()
        for file in task_3(filenames):
            self.assertTrue("$0{FULLSTOP}50 Hold'Em Turbo" in file)

    def test_task_4(self):
        all_in_folder = ['a', 'b', 'c', 'd', 'e']
        already_in_db = ['a', 'b', 'c', 'd']
        self.assertTrue(task_4(all_in_folder, already_in_db) == ['e'])



if __name__ == '__main__':
    unittest.main()
