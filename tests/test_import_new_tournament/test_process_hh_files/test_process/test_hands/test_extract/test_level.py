


import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.level import level
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_level(self):
        # open up all hands and have them in a list

        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]

        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh

        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_levels = [
            "6 (1250.00/2500.00)",
            "6 (1250.00/2500.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)",
            "7 (1500.00/3000.00)"
        ]

        for idx, h in enumerate(hands):
            # print('"' + level(h) + '",')
            self.assertEqual(level(h), expected_levels[idx])






#
# def level(hand_txt):
#     return hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]
