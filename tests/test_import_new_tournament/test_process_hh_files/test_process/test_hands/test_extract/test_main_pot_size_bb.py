
import unittest
from import_new_tournament.process_hh_files.process.hands.extract.main_pot_size_bb import main_pot_size_bb
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_level(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_pot_size_bb = [
            24.6,
            22.8,
            3.1,
            3.1,
            2.6,
            2.6,
            3.1,
            3.1,
            8.1,
            31.7,
            22.17,
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(main_pot_size_bb(h), expected_pot_size_bb[idx])
