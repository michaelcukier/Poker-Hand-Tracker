import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.id import get_id
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_get_id(self):
        # open up all hands and have them in a list

        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

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
