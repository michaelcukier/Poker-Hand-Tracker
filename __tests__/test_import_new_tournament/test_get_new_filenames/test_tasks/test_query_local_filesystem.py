import unittest


from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from import_new_tournament.get_new_filenames.tasks.query_local_filesystem import query_local_filesystem


class test(unittest.TestCase):
    def test_query_local_filesystem(self):
        files = query_local_filesystem(FAKE_HAND_HISTORY_FOLDER)

        self.assertEqual(
            len(files),
            12)

        self.assertCountEqual(
            ["HH20201217 CASHID-G23130355T1 TN-Mascoutah GAMETYPE-Omaha LIMIT-no CUR-REAL OND-F BUYIN-0 MIN-1 MAX-2.txt",
            "HH20201217 CASHID-G23130358T8 TN-Belleair GAMETYPE-Omaha LIMIT-no CUR-REAL OND-F BUYIN-0 MIN-1 MAX-2.txt",
            "HH20201217 CASHID-G23130358T9 TN-Conway Springs GAMETYPE-Omaha LIMIT-no CUR-REAL OND-F BUYIN-0 MIN-1 MAX-2.txt",
            "HH20201217 SITGOID-G23140119T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T2 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210112 SITGOID-G23315209T1 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210112 SITGOID-G23315209T3 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt",
            "HH20210122 SITGOID-G23889488T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"],
            files)
