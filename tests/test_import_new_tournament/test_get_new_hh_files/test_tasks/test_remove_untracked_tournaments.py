
import unittest
from import_new_tournament.get_new_hh_files.tasks.remove_untracked_tournaments import remove_untracked_tournaments
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join


class test(unittest.TestCase):

    def test_remove_untracked_tournament(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames.append("blob")
        files = remove_untracked_tournaments(new_filenames)
        self.assertEqual(
            len(files),
            9
        )
