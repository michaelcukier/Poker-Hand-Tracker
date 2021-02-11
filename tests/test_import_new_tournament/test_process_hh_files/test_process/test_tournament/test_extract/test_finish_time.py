
from import_new_tournaments.process_hh_files.process.tournament.extract.finish_time import finish_time
from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand
import unittest


class test(unittest.TestCase):
    def test_finish_time(self):

        fake_hand = Hand(hand_txt='x')
        fake_hand.time = 'tests'

        self.assertEqual(
            finish_time(fake_hand),
            'tests'
        )