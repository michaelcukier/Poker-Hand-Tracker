
import unittest
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import *
from GLOBAL_VARIABLES import TEST_HH_FOR_SIDE_POTS_FOLDER


class test(unittest.TestCase):
    def test_hands(self):

        hands_ = get_hands_in_list(TEST_HH_FOR_SIDE_POTS_FOLDER, ["HH20210112 SITGOID-G99999999T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 ---- for side pot.txt"])
        processed = process_hands(hands_)

        expected_times = [
            "2020/12/15 21:20:06 UTC",
            "2020/12/15 22:05:21 UTC",
            "2020/12/15 22:07:47 UTC",
            "2021/01/12 21:22:37 UTC",
            "2021/01/12 22:26:03 UTC"
        ]

        expected_levels = [
            "5 (1000.00/2000.00)",
            "13 (4500.00/9000.00)",
            "13 (4500.00/9000.00)",
            "7 (1500.00/3000.00)",
            "4 (750.00/1500.00)"
        ]

        expected_my_cards = [
            "3h Ah",
            "2h Js",
            "Qs Ah",
            "7h Th",
            "5d Qd",
        ]

        expected_board_cards = [
            "no-board",
            "6s 3d 5c 4d 2d",
            "8s 4c 2c Td 5d",
            "3c Jc 2d Tc 5h",
            "3s 7d 2d 9s Th"
        ]

        expected_tournament_ids = [
            23123480,
            23123480,
            23123480,
            23315145,
            23315614
        ]

        expected_hand_ids = [
            624700000,
            624749910,
            624752872,
            660426565,
            660501877
        ]

        expected_main_pot_winners = [
            "PotNoodle99912",
            "Ginijo",
            "slbetters",
            "Jhonybegoooddd",
            "Diamond JJ"
        ]

        expected_side_pot_1_winners = [
            None,
            "Bubbazinitty",
            "slbetters",
            "GABI22",
            "Diamond JJ"
        ]

        expected_side_pot_2_winners = [
            None,
            None,
            None,
            None,
            "Diamond JJ"
        ]

        expected_side_pot_3_winners = [
            None,
            None,
            None,
            None,
            "drail0073"
        ]

        expected_main_pot_sizes = [
            2.2,
            1.42,
            3.45,
            47.66,
            116.63
        ]

        expected_side_pot_1_sizes = [
            0,
            1.59,
            2.05,
            1.93,
            5.83
        ]

        expected_side_pot_2_sizes = [
            0,
            0,
            0,
            0,
            8.13
        ]

        expected_side_pot_3_sizes = [
            0,
            0,
            0,
            0,
            1.67
        ]

        for idx, p in enumerate(processed):
            self.assertEqual(p.time, expected_times[idx])
            self.assertEqual(p.level, expected_levels[idx])
            self.assertEqual(p.my_cards, expected_my_cards[idx])
            self.assertEqual(p.board_cards, expected_board_cards[idx])
            self.assertEqual(p.tournament_id, expected_tournament_ids[idx])
            self.assertEqual(p.id, expected_hand_ids[idx])
            self.assertEqual(p.main_pot_winner, expected_main_pot_winners[idx])
            self.assertEqual(p.side_pot_1_winner, expected_side_pot_1_winners[idx])
            self.assertEqual(p.side_pot_2_winner, expected_side_pot_2_winners[idx])
            self.assertEqual(p.side_pot_3_winner, expected_side_pot_3_winners[idx])
            self.assertEqual(p.main_pot_size_bb, expected_main_pot_sizes[idx])
            self.assertEqual(p.side_pot_1_size_bb, expected_side_pot_1_sizes[idx])
            self.assertEqual(p.side_pot_2_size_bb, expected_side_pot_2_sizes[idx])
            self.assertEqual(p.side_pot_3_size_bb, expected_side_pot_3_sizes[idx])
