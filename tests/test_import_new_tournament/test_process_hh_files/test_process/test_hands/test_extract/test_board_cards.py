import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.board_cards import board_cards
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_board_cards(self):
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

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
