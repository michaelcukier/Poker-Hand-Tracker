
import unittest

from import_new_tournaments.process_hh_files.process.tournament.extract.price import price

class test(unittest.TestCase):
    def test_price(self):

        filename = "HH20201217 SITGOID-G23140238T1 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"

        self.assertEqual(
            price(filename),
            0.55)
