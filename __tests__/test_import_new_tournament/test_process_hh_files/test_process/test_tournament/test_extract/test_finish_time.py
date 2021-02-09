
from import_new_tournament.process_hh_files.process.tournament.extract.finish_time import finish_time
from import_new_tournament.process_hh_files.process.hands.Hand.Hand import Hand
import unittest


class test(unittest.TestCase):
    def test_elapsed_time(self):

        fake_hand = Hand(hand_txt='x')
        fake_hand.time = 'test'

        self.assertEqual(
            finish_time(fake_hand),
            'test'
        )