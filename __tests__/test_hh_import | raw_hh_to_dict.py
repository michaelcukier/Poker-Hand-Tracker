import unittest

from hh_import.raw_hh_to_dict.task_1 import task_1
from hh_import.raw_hh_to_dict.task_2 import task_2
from hh_import.raw_hh_to_dict.task_3 import task_3
from hh_import.raw_hh_to_dict.task_4 import task_4
from hh_import.raw_hh_to_dict.task_5 import task_5, order_hands_by_time
from hh_import.raw_hh_to_dict.task_6 import task_6
from hh_import.raw_hh_to_dict.task_7 import task_7

FAKE_HAND_HISTORY_FOLDER = '/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/__tests__/fake_data_tourneys/handHistory/PotNoodle99912/'
FAKE_TOURNAMENT_SUMMARY_FOLDER = '/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/__tests__/fake_data_tourneys/TournamentSummary/PotNoodle99912/'


class test_dict_to_clean_data(unittest.TestCase):

    def test_task_1(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        self.assertEqual(task1, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
        "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
        'HH20201217 CASHID-G23130358T8 TN-Belleair GAMETYPE-Omaha LIMIT-no CUR-REAL '
        'OND-F BUYIN-0 MIN-1 MAX-2.txt',
        'HH20201217 CASHID-G23130355T1 TN-Mascoutah GAMETYPE-Omaha LIMIT-no CUR-REAL '
        'OND-F BUYIN-0 MIN-1 MAX-2.txt',
        "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
        "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
        "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
        "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
        "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
        "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
        "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
        "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
        'HH20201217 CASHID-G23130358T9 TN-Conway Springs GAMETYPE-Omaha LIMIT-no '
        'CUR-REAL OND-F BUYIN-0 MIN-1 MAX-2.txt'])

    def test_task_2(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        self.assertEqual(task2, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
       "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
       "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
       "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
       "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
       "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
       "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
       "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
       "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On "
       "Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

    def test_task_3(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=True)
        self.assertEqual(task3, [
            "HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"
        ])

    def test_task_4(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=True)
        task4 = task_4(task3)
        self.assertEqual(len(task4.items()), 3)
        self.assertTrue('23140238' in task4)
        self.assertTrue('23140119' in task4)
        self.assertTrue('23140753' in task4)

    def test_task_5(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=True)
        task4 = task_4(task3)
        task5 = task_5(task4, FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        self.assertEqual(len(task5['23140753']['hands']), 29)

    def test_order_hands_by_time(self):
        test_hands = [
            '''Game Hand #613502712 - Tournament #23060933 - Holdem(No Limit) - Level 3 (500.00/1000.00)- 2020/12/06 21:23:06 UTC
            Table '2' 9-max Seat #3 is the button''',

            '''Game Hand #613505310 - Tournament #23060933 - Holdem(No Limit) - Level 3 (500.00/1000.00)- 2020/12/06 21:24:15 UTC
            Table '2' 9-max Seat #4 is the button
            Seat 1: SCHENCK101 (27495.00)
            Seat 2: PotNoodle99912 (29900.00)
            Seat 3: meatbro (15170.00)''',

            '''Game Hand #613505310 - Tournament #23060933 - Holdem(No Limit) - Level 3 (500.00/1000.00)- 2020/12/06 21:20:15 UTC
            Table '2' 9-max Seat #4 is the button
            Seat 1: SCHENCK101 (27495.00)''']
        self.assertTrue('21:20:15' in order_hands_by_time(test_hands)[0].split('\n')[0])
        self.assertTrue('21:23:06' in order_hands_by_time(test_hands)[1].split('\n')[0])
        self.assertTrue('21:24:15' in order_hands_by_time(test_hands)[2].split('\n')[0])

    def test_task_6(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=True)
        task4 = task_4(task3)
        task5 = task_5(task4, FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task6 = task_6(task5)
        self.assertEqual(len(task6['23140753']['hands']), 28)

    def test_task_7(self):
        task1 = task_1(FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task2 = task_2(task1)
        task3 = task_3(task2, FOR_TESTING_MOCK_EMPTY_DB=True)
        task4 = task_4(task3)
        task5 = task_5(task4, FOR_TESTING_CUSTOM_FOLDER=FAKE_HAND_HISTORY_FOLDER)
        task6 = task_6(task5)
        task7 = task_7(task6, FOR_TESTING_CUSTOM_FOLDER=FAKE_TOURNAMENT_SUMMARY_FOLDER)
        self.assertEqual(task7['23140238']['summary'], None)
        self.assertTrue(type(task7['23140119']['summary']) == dict)
        self.assertTrue(type(task7['23140753']['summary']) == dict)
