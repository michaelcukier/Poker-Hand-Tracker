import unittest


from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER, FAKE_TOURNAMENT_SUMMARY_FOLDER
from import_new_tournament.get_new_filenames.TournamentFiles.TournamentFiles import TournamentFiles
from os import listdir

from os.path import isfile, join

from utils.extract_id_from_title import extract_id_from_title

from import_new_tournament.get_new_filenames.tasks.get_tournament_summaries_and_re_entries import get_tournament_summaries_and_re_entries


class test(unittest.TestCase):
    def test_get_tournament_summaries_and_re_entries(self):

        # setup
        filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        filenamesClasses = []
        for f in filenames:
            filenamesClasses.append(TournamentFiles(tournament_id=extract_id_from_title(f)))
        out = get_tournament_summaries_and_re_entries(
            tournament_files=filenamesClasses,
            TOURNAMENT_SUMMARY_FOLDER=FAKE_TOURNAMENT_SUMMARY_FOLDER
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
            2,
        ]

        for idx, o in enumerate(out):
            self.assertEqual(o.re_entries, re_entries[idx])
            self.assertEqual(o.tournament_summary_filename, ts[idx])

