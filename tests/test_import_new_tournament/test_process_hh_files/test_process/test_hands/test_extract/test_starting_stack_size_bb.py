
import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.starting_stack_size_bb import starting_stack_size_bb
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_starting_stack_size_bb(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh

        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_starting_stack_size_bb = [
            7.3,
            7.2,
            5.9,
            7.9,
            7.8,
            9.3,
            10.8,
            10.7,
            10.6,
            10.5,
            10.4,
        ]

        for idx, h in enumerate(hands):
            # print(str(starting_stack_size_bb(h)) + ',')
            self.assertEqual(starting_stack_size_bb(h), expected_starting_stack_size_bb[idx])

