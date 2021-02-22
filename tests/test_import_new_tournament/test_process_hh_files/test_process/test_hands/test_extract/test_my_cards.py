
import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.my_cards import my_cards
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_my_cards(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_my_cards = [
            "4s Qs",
            "7d Js",
            "8c 8h",
            "6h 9s",
            "Qd Td",
            "8d 7d",
            "6c Tc",
            "6h Kh",
            "Th Kd",
            "Qh 7s",
            "8d Js",
        ]

        for idx, h in enumerate(hands):
            # print('"' + my_cards(h) + '",')
            self.assertEqual(my_cards(h), expected_my_cards[idx])
