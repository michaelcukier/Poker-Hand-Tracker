import unittest
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.get_new_hh_files.tasks.group_filenames_by_id import group_filenames_by_id


class test(unittest.TestCase):

    def test_group_filenames_by_id(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        files = group_filenames_by_id(new_filenames)

        ids = [
            23889488,
            23140753,
            23140119,
            23315209,
            23140238,
            99999999
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
