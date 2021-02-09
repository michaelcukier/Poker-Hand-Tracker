

import unittest
from import_new_tournament.process_filenames.process.hands.extract.side_pot_n_size_bb import side_pot_n_size_bb
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_side_pot_n_size_bb(self):
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, ['hh_for_side_pot_test.txt'])

        expected_side_pot_1_size_bb = [
            0,
            1.59,
            2.05,
            1.93,
            5.83
        ]

        expected_side_pot_2_size_bb = [
            0,
            0,
            0,
            0,
            8.13
        ]

        expected_side_pot_3_size_bb = [
            0,
            0,
            0,
            0,
            1.67
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(side_pot_n_size_bb(h, n=1), expected_side_pot_1_size_bb[idx])
            self.assertEqual(side_pot_n_size_bb(h, n=2), expected_side_pot_2_size_bb[idx])
            self.assertEqual(side_pot_n_size_bb(h, n=3), expected_side_pot_3_size_bb[idx])
