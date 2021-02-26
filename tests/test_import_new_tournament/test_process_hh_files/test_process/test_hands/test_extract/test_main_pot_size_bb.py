
import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.main_pot_size_bb import main_pot_size_bb
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_level(self):
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

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
