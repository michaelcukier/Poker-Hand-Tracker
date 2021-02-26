import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.main_pot_winner import main_pot_winner
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_level(self):
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

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
            self.assertEqual(main_pot_winner(h), expected_main_pot_winner[idx])
