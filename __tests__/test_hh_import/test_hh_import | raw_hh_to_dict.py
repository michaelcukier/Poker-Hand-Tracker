import unittest

from hh_import.raw_hh_to_dict.task_1 import task_1
from hh_import.raw_hh_to_dict.task_2 import task_2
from hh_import.raw_hh_to_dict.task_3 import task_3
from hh_import.raw_hh_to_dict.task_4 import task_4
from hh_import.raw_hh_to_dict.task_5 import task_5, order_hands_by_time
from hh_import.raw_hh_to_dict.task_6 import task_6
from hh_import.raw_hh_to_dict.task_7 import task_7

from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER, FAKE_TOURNAMENT_SUMMARY_FOLDER

from fake_data_tourneys.fake_data import FAKE_UNORDERED_HANDS
import sys

class test_dict_to_clean_data(unittest.TestCase):

    def test_task_1(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)

        self.assertCountEqual(task1, [
            "HH20210122 SITGOID-G23889488T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            'HH20201217 CASHID-G23130358T8 TN-Belleair GAMETYPE-Omaha LIMIT-no CUR-REAL OND-F BUYIN-0 MIN-1 MAX-2.txt',
            'HH20201217 CASHID-G23130355T1 TN-Mascoutah GAMETYPE-Omaha LIMIT-no CUR-REAL OND-F BUYIN-0 MIN-1 MAX-2.txt',
            "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            'HH20201217 CASHID-G23130358T9 TN-Conway Springs GAMETYPE-Omaha LIMIT-no CUR-REAL OND-F BUYIN-0 MIN-1 MAX-2.txt',
        ])

    def test_task_2(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        self.assertCountEqual(task2, [
            "HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"
        ])

    def test_task_3(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=['23140238'])
        self.assertCountEqual(task3, [
            "HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"
        ])

    def test_task_4(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=[])
        task4 = task_4(task3)
        self.assertEqual(len(task4.items()), 4)
        self.assertTrue('23140238' in task4)
        self.assertTrue('23140119' in task4)
        self.assertTrue('23140753' in task4)
        self.assertTrue('23889488' in task4)

    def test_task_5(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=[])
        task4 = task_4(task3)
        task5 = task_5(task4, FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        self.assertEqual(len(task5['23140753']['hands']), 29)

    def test_order_hands_by_time(self):
        self.assertTrue('21:20:15' in order_hands_by_time(FAKE_UNORDERED_HANDS)[0])
        self.assertTrue('21:23:06' in order_hands_by_time(FAKE_UNORDERED_HANDS)[1])
        self.assertTrue('21:24:15' in order_hands_by_time(FAKE_UNORDERED_HANDS)[2])

    def test_task_6(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=[])
        task4 = task_4(task3)
        task5 = task_5(task4, FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task6 = task_6(task5)
        self.assertEqual(len(task6['23140753']['hands']), 28)

    def test_task_7(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=[])
        task4 = task_4(task3)
        task5 = task_5(task4, FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task6 = task_6(task5)
        task7 = task_7(task6, FOR_TESTING_CUSTOM_FOLDER=FAKE_TOURNAMENT_SUMMARY_FOLDER)

        # no tourney summary
        self.assertEqual(task7['23140238']['title'],
            "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt")
        self.assertEqual(task7['23140238']['summary'], None)
        self.assertEqual(task7['23140238']['re_entries'], 1)

        # no tourney summary
        self.assertEqual(task7['23140753']['title'],
            "HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt")
        self.assertEqual(task7['23140238']['re_entries'], 1)

        # 2 tourney summaries
        self.assertEqual(task7['23889488']['title'],
            "HH20210122 SITGOID-G23889488T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt")
        self.assertEqual(task7['23889488']['re_entries'], 2)
        self.assertEqual(task7['23889488']['summary']['player_count'], 26)
