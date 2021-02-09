
import unittest

from utils.create_fake_database.create_fake_database import CreateFakeDatabase
from import_new_tournament.get_new_filenames.tasks.query_local_database import query_local_database


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
        new_filenames = [
            "HH20210112 SITGOID-G23315209T1 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210112 SITGOID-G23315209T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"
        ]

        files = query_local_database(
            filenames=new_filenames,
            database_file_path='./testDB.db'
        )

        # since there's "23889488" in the database,
        # should return 5-2=3 elements from above list
        self.assertEqual(len(files), 3)
        self.assertCountEqual(
            [
                "HH20210112 SITGOID-G23315209T1 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20210112 SITGOID-G23315209T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
                "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"
            ],
            files
        )
