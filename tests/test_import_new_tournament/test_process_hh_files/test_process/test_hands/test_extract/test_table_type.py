import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.table_type import table_type
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_table_type(self):
        hand = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20210122 SITGOID-G23889488T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])
        hand = hand[0]  # convert list of length 1 to str
        hand = hand.replace("'", '"')
        expected_table_type = '9-max'
        self.assertEqual(table_type(hand), expected_table_type)
