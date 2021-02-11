
import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.side_pot_n_winner import side_pot_n_winner
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_side_pot_n_winner(self):
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, ["HH20210112 SITGOID-G99999999T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 ---- for side pot.txt"])

        expected_side_pot_1_winner = [
            None,
            "Bubbazinitty",
            "slbetters",
            "GABI22",
            "Diamond JJ"
        ]

        expected_side_pot_2_winner = [
            None,
            None,
            None,
            None,
            "Diamond JJ"
        ]

        expected_side_pot_3_winner = [
            None,
            None,
            None,
            None,
            "drail0073"
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(side_pot_n_winner(h, n=1), expected_side_pot_1_winner[idx])
            self.assertEqual(side_pot_n_winner(h, n=2), expected_side_pot_2_winner[idx])
            self.assertEqual(side_pot_n_winner(h, n=3), expected_side_pot_3_winner[idx])
