import unittest
from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_Hand(self):
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])
        hand = hands[0]

        myH = Hand(hand_txt=hand)
        myH.build_hand()

        expected_attributes = [
            "board_cards",
            "build_hand",
            "hand_txt",
            "id",
            "level",
            "main_pot_size_bb",
            "main_pot_winner",
            "my_cards",
            "nb_occupied_seats",
            "side_pot_1_size_bb",
            "side_pot_1_winner",
            "side_pot_2_size_bb",
            "side_pot_2_winner",
            "side_pot_3_size_bb",
            "side_pot_3_winner",
            "starting_stack_size_bb",
            "time",
            "tournament_id",
            "table_type",
            "position_and_player"]

        all_attributes = []
        for attribute in dir(myH):
            if attribute[0] is not '_':
                all_attributes.append(attribute)

        self.assertCountEqual(all_attributes, expected_attributes)

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
        self.assertEqual(myH.nb_occupied_seats, 5)
        self.assertEqual(myH.table_type, '9-max')
        self.assertEqual(myH.position_and_player,
                         {'BTN': 'PotNoodle99912',
                          'SB': 'rldes',
                          'BB': 'bacchus5555',
                          'UTG': 'WBRoy',
                          'UTG+1': None,
                          'MP': None,
                          'MP+1': None,
                          'MP+2': None,
                          'CO': 'Naruba80'})


