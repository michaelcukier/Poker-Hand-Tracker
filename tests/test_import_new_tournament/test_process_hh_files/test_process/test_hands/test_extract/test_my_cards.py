
import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.my_cards import my_cards
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_my_cards(self):
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

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
            self.assertEqual(my_cards(h), expected_my_cards[idx])
