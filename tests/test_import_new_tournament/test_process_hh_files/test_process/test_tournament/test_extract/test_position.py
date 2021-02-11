
import unittest

from import_new_tournaments.process_hh_files.process.tournament.extract.position import position
from GLOBAL_VARIABLES import FAKE_TOURNAMENT_SUMMARY_FOLDER


class test(unittest.TestCase):
    def test_position(self):

        parent_folder = FAKE_TOURNAMENT_SUMMARY_FOLDER
        ts_filename = 'TS20210122 T23889488 E211608095 NL Hold’em $3.00 + $0.30.ots'

        self.assertEqual(
            position(parent_folder, ts_filename),
            12)
