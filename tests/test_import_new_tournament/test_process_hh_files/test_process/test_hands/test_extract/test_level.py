import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.level import level
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_level(self):
        # open up all hands and have them in a list
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

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
            self.assertEqual(level(h), expected_levels[idx])

