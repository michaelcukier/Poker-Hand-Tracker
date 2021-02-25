
import unittest
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER, TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER
from utils.create_fake_database.create_fake_database import CreateFakeDatabase
from import_new_tournaments.get_new_hh_files.get_new_filenames import get_new_filenames


class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.database = CreateFakeDatabase(
            db_name='testDB',
            table_name='tournaments',
            columns_labels=['ID'],
            data=[
                [23889488]
            ])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.database.destroy()

    def test_get_new_filenames(self):
        files = get_new_filenames(
            HH_PATH=TEST_RANDOM_HAND_HISTORIES_FOLDER,
            TOURNAMENT_SUMMARY_FOLDER=TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER,
            DATABASE_PATH='./testDB.db'
        )

        ids = [
            23140753,
            23140119,
            23315209,
            23140238,
            24095328
        ]

        hh_filenames = [
            ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt", "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt", "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"],
            ["HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"],
            ["HH20210112 SITGOID-G23315209T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt", "HH20210112 SITGOID-G23315209T1 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"],
            ["HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"],
            ["HH20210220 SITGOID-G24095328T3 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 -- for position from 9 to 2.txt"]

        ]

        ts_filenames = [
            "TS20201217 T23140753 E197540971 NL Hold’em $0.50 + $0.05.ots",
            "TS20201217 T23140119 E197503901 NL Hold’em $0.50 + $0.05.ots",
            "TS20210112 T23315209 E206991272 NL Hold’em $1.50 + $0.15.ots",
            None
        ]

        re_entries = [
            1,
            1,
            2,
            1,
        ]

        for idx, f in enumerate(files):
            # print(f.tournament_id)
            self.assertEqual(f.tournament_id, ids[idx])
            self.assertEqual(f.hand_history_filenames, hh_filenames[idx])
            self.assertEqual(f.tournament_summary_filename, ts_filenames[idx])
            self.assertEqual(f.re_entries, re_entries[idx])
