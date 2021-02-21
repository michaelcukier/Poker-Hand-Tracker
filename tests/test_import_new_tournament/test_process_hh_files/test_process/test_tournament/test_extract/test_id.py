

from import_new_tournaments.process_hh_files.process.tournament.extract.id import get_id
import unittest


class test(unittest.TestCase):
    def test_id(self):

        fake_tournament_title = "HH20210112 SITGOID-G23315209T1 TN-$1{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"

        self.assertEqual(
            get_id(fake_tournament_title),
            23315209
        )