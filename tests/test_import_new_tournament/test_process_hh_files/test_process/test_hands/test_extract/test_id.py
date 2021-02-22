

import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.id import get_id
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_get_id(self):
        # open up all hands and have them in a list

        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]

        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh

        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

        expected_ids = [
            627325357,
            627327620,
            627328481,
            627328893,
            627329469,
            627330445,
            627330797,
            627331964,
            627332459,
            627332818,
            627333718,
        ]

        for idx, h in enumerate(hands):
            self.assertEqual(get_id(h), expected_ids[idx])

