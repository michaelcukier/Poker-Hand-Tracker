
import unittest
from import_new_tournament.process_filenames.process.tournament.extract.elapsed_time import elapsed_time
from import_new_tournament.process_filenames.process.hands.Hand.Hand import Hand


class test(unittest.TestCase):
    def test_elapsed_time(self):

        first_hand = Hand(hand_txt='x')
        first_hand.time = '2020/12/17 22:00:00 UTC'

        last_hand = Hand(hand_txt='y')
        last_hand.time = '2020/12/17 22:23:00 UTC'

        self.assertEqual(
            elapsed_time(
                first_hand=first_hand,
                last_hand=last_hand),
            23
        )
