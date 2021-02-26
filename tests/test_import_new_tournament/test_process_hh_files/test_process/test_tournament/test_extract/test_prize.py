import unittest
from import_new_tournaments.process_hh_files.process.tournament.extract.prize import prize
from GLOBAL_VARIABLES import TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER


class test(unittest.TestCase):
    def test_prize(self):

        parent_folder = TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER
        ts_filename = 'TS20201217 T23127921 E197421416 NL Hold’em $1.00 + $0.10.ots'

        self.assertEqual(
            prize(parent_folder, ts_filename),
            999)
