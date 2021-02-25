import unittest

from import_new_tournaments.process_hh_files.process.tournament.extract.opponents import opponents
from GLOBAL_VARIABLES import TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER


class test(unittest.TestCase):
    def test_opponents(self):

        parent_folder = TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER
        ts_filename = 'TS20210122 T23889488 E211608095 NL Hold’em $3.00 + $0.30.ots'

        self.assertCountEqual(
            opponents(parent_folder, ts_filename),
            ['MGMNHDaYu',
             'GetChu1',
             'DenTurbo',
             'reeseuave24',
             'mjitri12',
             'Iconoclast63',
             'Lexthenext',
             'DmexicanPooh',
             'DubJ1313',
             'CoachTom58',
             'YakAttack904',
             'Fiend4poker',
             'Snow88man'])
