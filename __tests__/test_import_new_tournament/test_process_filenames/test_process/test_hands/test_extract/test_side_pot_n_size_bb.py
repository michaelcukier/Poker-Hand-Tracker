
import unittest
from import_new_tournament.process_filenames.process.hands.extract.side_pot_n_winner import side_pot_n_winner
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_level(self):
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, ['hh_for_side_pot_test.txt'])

        expected_side_pot_1_winner = [
            "no-side-pot",
            "Bubbazinitty",
            "slbetters",
            "GABI22",
            "Diamond JJ"
        ]

        expected_side_pot_2_winner = [
            "no-side-pot",
            "no-side-pot",
            "no-side-pot",
            "no-side-pot",
            "Diamond JJ"
        ]

        expected_side_pot_3_winner = [
            "no-side-pot",
            "no-side-pot",
            "no-side-pot",
            "no-side-pot",
            "drail0073"
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(side_pot_n_winner(h, n=1), expected_side_pot_1_winner[idx])
            self.assertEqual(side_pot_n_winner(h, n=2), expected_side_pot_2_winner[idx])
            self.assertEqual(side_pot_n_winner(h, n=3), expected_side_pot_3_winner[idx])
