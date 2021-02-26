
import unittest
from import_new_tournaments.get_new_hh_files.tasks.remove_untracked_tournaments import remove_untracked_tournaments
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from os import listdir
from os.path import isfile, join


class test(unittest.TestCase):

    def test_remove_untracked_tournament(self):
        new_filenames = [f for f in listdir(TEST_RANDOM_HAND_HISTORIES_FOLDER) if isfile(join(TEST_RANDOM_HAND_HISTORIES_FOLDER, f))]
        new_filenames.append("blob")
        files = remove_untracked_tournaments(new_filenames)
        self.assertEqual(
            len(files),
            9)
