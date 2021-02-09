


import unittest
from import_new_tournament.process_hh_files.process.hands.extract.main_pot_winner import main_pot_winner
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_level(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_main_pot_winner = [
            "bacchus5555",
            "WBRoy",
            "PotNoodle99912",
            "OffMyMedz",
            "PotNoodle99912",
            "PotNoodle99912",
            "Burn Card",
            "WBRoy",
            "bacchus5555",
            "WBRoy",
            "OffMyMedz",
        ]

        for idx, h in enumerate(hands):
            # print('"' + main_pot_winner(h) + '",')
            self.assertEqual(main_pot_winner(h), expected_main_pot_winner[idx])
