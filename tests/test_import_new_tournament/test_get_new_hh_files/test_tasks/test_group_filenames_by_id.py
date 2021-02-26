import unittest
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.get_new_hh_files.tasks.group_filenames_by_id import group_filenames_by_id


class test(unittest.TestCase):

    def test_group_filenames_by_id(self):
        new_filenames = [f for f in listdir(TEST_RANDOM_HAND_HISTORIES_FOLDER) if isfile(join(TEST_RANDOM_HAND_HISTORIES_FOLDER, f))]
        files = group_filenames_by_id(new_filenames)

        ids = [
            23889488,
            23140753,
            23140119,
            23315209,
            23140238,
            24095328
        ]

        hh_amount = [
            2,
            3,
            1,
            2,
            1,
            1
        ]

        for idx, f in enumerate(files):
            self.assertEqual(f.__dict__['tournament_id'], ids[idx])
            self.assertEqual(len(f.__dict__['hand_history_filenames']), hh_amount[idx])
