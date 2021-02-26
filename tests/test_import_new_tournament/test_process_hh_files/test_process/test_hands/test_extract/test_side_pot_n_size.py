import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.side_pot_n_size_bb import side_pot_n_size_bb
from GLOBAL_VARIABLES import TEST_HH_FOR_SIDE_POTS_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_side_pot_n_size_bb(self):
        hands = get_hands_in_list(TEST_HH_FOR_SIDE_POTS_FOLDER, ["HH20210112 SITGOID-G99999999T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 ---- for side pot.txt"])

        expected_side_pot_1_size_bb = [
            0,
            1.59,
            2.05,
            1.93,
            5.83
        ]

        expected_side_pot_2_size_bb = [
            0,
            0,
            0,
            0,
            8.13
        ]

        expected_side_pot_3_size_bb = [
            0,
            0,
            0,
            0,
            1.67
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(side_pot_n_size_bb(h, n=1), expected_side_pot_1_size_bb[idx])
            self.assertEqual(side_pot_n_size_bb(h, n=2), expected_side_pot_2_size_bb[idx])
            self.assertEqual(side_pot_n_size_bb(h, n=3), expected_side_pot_3_size_bb[idx])
