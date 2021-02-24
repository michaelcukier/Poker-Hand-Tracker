
import unittest
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER, FAKE_TOURNAMENT_SUMMARY_FOLDER
from utils.create_fake_database.create_fake_database import CreateFakeDatabase
from import_new_tournaments.get_new_hh_files.get_new_filenames import get_new_filenames

from db_api.tables.report_by_day.sql_query import sql_query

class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.database = CreateFakeDatabase(
            db_name='testDB',
            table_name='tournaments',
            columns_labels=[
                'ID',
                'finished_time',
                'price',
                'prize',
                'position',
                'elapsed_time',
                'Entries'
            ],
            data=[
                [24120630, '2021/02/23 18:42:18 UTC', 3.3, 9.9, 4, 60, 1],
                [24113211, '2021/02/23 06:28:39 UTC', 6.6, 9, 14, 71, 1],
                [24112193, '2021/02/23 04:15:24 UTC', 3.3, 16.53, 4, 85, 1],
                [24103572, '2021/02/21 22:13:58 UTC', 0.55, 0, 47, 0, 1],
                [24103198, '2021/02/21 22:11:26 UTC', 0.55, 0.72, 13, 70, 1],
                [24103381, '2021/02/21 21:41:49 UTC', 0.55, 0, 24, 20, 1]
            ])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.database.destroy()

    def test_sql_query(self):

        # Day    | Nb of games played | Money spent | Money won | session length
        # 02/21  | 3                  | 1.65        | 0.72      | 70
        # 02/23  | 3                  | 13.2        | 35.43     | 216

        for x in sql_query('./testDB.db'):
            print(x)
        pass



