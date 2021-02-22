
import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.board_cards import board_cards
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_board_cards(self):
        # open up all hands and have them in a list

        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]

        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh

        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_board_cards = [
            "Jd 5h 6d 3h Kh",
            "4s 5h 4d Qd 6h",
            "no-board",
            "Th 5c Kc",
            "8h 2h 4s 2s Kc",
            "no-board",
            "5d Kd Ad",
            "no-board",
            "no-board",
            "Ad 2s 6h Qc 9s",
            "4s Jh 9s Kh Td"
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(board_cards(h), expected_board_cards[idx])
