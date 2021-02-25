
import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.nb_occupied_seats import nb_occupied_seats
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_nb_occupied_seats(self):
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20210122 SITGOID-G23889488T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

        expected_my_cards = [
            7,
            7,
            7,
            8,
            9,
            9,
            5
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(nb_occupied_seats(h), expected_my_cards[idx])
