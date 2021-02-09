
import unittest
from import_new_tournament.process_filenames.process.hands.extract.time import time
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from utils.get_hands_in_list import get_hands_in_list


class test(unittest.TestCase):
    def test_time(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)

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
