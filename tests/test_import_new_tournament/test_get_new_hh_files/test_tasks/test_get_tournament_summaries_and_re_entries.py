import unittest


from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER, TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER
from import_new_tournaments.get_new_hh_files.TournamentFiles.TournamentFiles import TournamentFiles
from os import listdir

from os.path import isfile, join

from utils.extract_id_from_title import extract_id_from_title

from import_new_tournaments.get_new_hh_files.tasks.get_tournament_summaries_and_re_entries import get_tournament_summaries_and_re_entries


class test(unittest.TestCase):
    def test_get_tournament_summaries_and_re_entries(self):

        # setup
        filenames = [f for f in listdir(TEST_RANDOM_HAND_HISTORIES_FOLDER) if isfile(join(TEST_RANDOM_HAND_HISTORIES_FOLDER, f))]
        filenamesClasses = []
        for f in filenames:
            filenamesClasses.append(TournamentFiles(tournament_id=extract_id_from_title(f)))
        out = get_tournament_summaries_and_re_entries(
            tournament_files=filenamesClasses,
            TOURNAMENT_SUMMARY_FOLDER=TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER
        )

        # tests
        ts = [
            "TS20210122 T23889488 E211613053 NL Hold’em $3.00 + $0.30.ots",
            "TS20201217 T23140753 E197540971 NL Hold’em $0.50 + $0.05.ots",
            "TS20201217 T23140753 E197540971 NL Hold’em $0.50 + $0.05.ots",
            "TS20201217 T23140753 E197540971 NL Hold’em $0.50 + $0.05.ots",
            "TS20201217 T23140119 E197503901 NL Hold’em $0.50 + $0.05.ots",
            "TS20210112 T23315209 E206991272 NL Hold’em $1.50 + $0.15.ots",
            None,
            "TS20210122 T23889488 E211613053 NL Hold’em $3.00 + $0.30.ots",
            "TS20210112 T23315209 E206991272 NL Hold’em $1.50 + $0.15.ots",
        ]

        re_entries = [
            2,
            1,
            1,
            1,
            1,
            2,
            1,
            2,
            2
        ]

        self.assertEqual(out[0].re_entries, re_entries[0])
        self.assertEqual(out[0].tournament_summary_filename, ts[0])

        self.assertEqual(out[1].re_entries, re_entries[1])
        self.assertEqual(out[1].tournament_summary_filename, ts[1])

        self.assertEqual(out[2].re_entries, re_entries[2])
        self.assertEqual(out[2].tournament_summary_filename, ts[2])

        self.assertEqual(out[3].re_entries, re_entries[3])
        self.assertEqual(out[3].tournament_summary_filename, ts[3])

        self.assertEqual(out[4].re_entries, re_entries[4])
        self.assertEqual(out[4].tournament_summary_filename, ts[4])

        self.assertEqual(out[5].re_entries, re_entries[5])
        self.assertEqual(out[5].tournament_summary_filename, ts[5])

        self.assertEqual(out[6].re_entries, re_entries[6])
        self.assertEqual(out[6].tournament_summary_filename, ts[6])

        self.assertEqual(out[7].re_entries, re_entries[7])
        self.assertEqual(out[7].tournament_summary_filename, ts[7])

        self.assertEqual(out[8].re_entries, re_entries[8])
        self.assertEqual(out[8].tournament_summary_filename, ts[8])




