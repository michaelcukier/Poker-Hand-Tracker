
import unittest
from import_new_tournament.process_filenames.process.hands.extract.tournament_id import tournament_id
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_tournament_id(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_tournament_id = [
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(tournament_id(h), expected_tournament_id[idx])
