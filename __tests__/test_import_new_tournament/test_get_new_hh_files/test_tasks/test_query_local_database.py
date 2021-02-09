
import unittest

from utils.create_fake_database.create_fake_database import CreateFakeDatabase
from import_new_tournament.get_new_hh_files.tasks.query_local_database import query_local_database
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER

from os import listdir
from os.path import isfile, join


class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.database = CreateFakeDatabase(
            db_name='testDB',
            table_name='tournaments',
            columns_labels=['ID'],
            data=[
                ['23889488']
            ])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.database.destroy()

    def test_query_local_database(self):
        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]

        files = query_local_database(
            filenames=new_filenames,
            database_file_path='./testDB.db'
        )


        # since there's "23889488" in the database,
        # should return 9-2=7 elements from above list
        self.assertEqual(len(files), 7)
        self.assertCountEqual(
            [
                "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20210112 SITGOID-G23315209T1 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20210112 SITGOID-G23315209T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"
            ],
            files
        )
