import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.time import time
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_time(self):

        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

        expected_time = [
            "2020/12/17 22:17:35 UTC",
            "2020/12/17 22:19:14 UTC",
            "2020/12/17 22:19:55 UTC",
            "2020/12/17 22:20:12 UTC",
            "2020/12/17 22:20:37 UTC",
            "2020/12/17 22:21:21 UTC",
            "2020/12/17 22:21:36 UTC",
            "2020/12/17 22:22:29 UTC",
            "2020/12/17 22:22:51 UTC",
            "2020/12/17 22:23:08 UTC",
            "2020/12/17 22:23:47 UTC"
        ]

        for idx, h in enumerate(hands):
            # print('"' + time(h) + '",')
            self.assertEqual(time(h), expected_time[idx])


#
# def time(hand_txt):
#     return '202' + hand_txt.split('\n')[0].split(')- 202')[1]
