
import unittest
from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
from os import listdir
from os.path import isfile, join
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_Hand(self):

        new_filenames = [f for f in listdir(FAKE_HAND_HISTORY_FOLDER) if isfile(join(FAKE_HAND_HISTORY_FOLDER, f))]
        new_filenames = new_filenames[1:2]  # just select 11 hands from 1 hh
        hands = get_hands_in_list(FAKE_HAND_HISTORY_FOLDER, new_filenames)
        hand = hands[0]

        myH = Hand(hand_txt=hand)
        myH.build_hand()

        self.assertEqual(myH.time, '2020/12/17 22:17:35 UTC')
        self.assertEqual(myH.level, '6 (1250.00/2500.00)')
        self.assertEqual(myH.my_cards, '4s Qs')
        self.assertEqual(myH.board_cards, 'Jd 5h 6d 3h Kh')
        self.assertEqual(myH.tournament_id, 23140753)
        self.assertEqual(myH.id, 627325357)
        self.assertEqual(myH.starting_stack_size_bb, 7.3)
        self.assertEqual(myH.main_pot_winner, 'bacchus5555')
        self.assertEqual(myH.side_pot_1_winner, None)
        self.assertEqual(myH.side_pot_2_winner, None)
        self.assertEqual(myH.side_pot_3_winner, None)
        self.assertEqual(myH.main_pot_size_bb, 24.6)
        self.assertEqual(myH.side_pot_1_size_bb, 0)
        self.assertEqual(myH.side_pot_2_size_bb, 0)
        self.assertEqual(myH.side_pot_3_size_bb, 0)

