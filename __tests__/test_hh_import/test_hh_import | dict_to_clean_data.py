import unittest

from fake_data_tourneys.fake_data import *

import copy


class test_dict_to_clean_data(unittest.TestCase):

    def test_get_hand_time(self):
        self.assertEqual(get_hand_time(fake_tournament['hands'][0]), '2020/12/12 05:30:01 UTC')  # hand 2
        self.assertEqual(get_hand_time(fake_tournament['hands'][1]), '2020/12/12 05:30:37 UTC')  # hand 2
        self.assertEqual(get_hand_time(fake_tournament['hands'][2]), '2020/12/12 05:36:34 UTC')  # hand 2

    def test_get_hand_pot_size_chips(self):
        self.assertEqual(get_hand_pot_size_chips(fake_tournament['hands'][0]), 8600)  # hand 1
        self.assertEqual(get_hand_pot_size_chips(fake_tournament['hands'][1]), 7400)  # hand 2
        self.assertEqual(get_hand_pot_size_chips(fake_tournament['hands'][2]), 61800)  # hand 2

    def test_get_hand_pot_size_bb(self):
        self.assertEqual(get_hand_pot_size_bb(fake_tournament['hands'][0]), 8.6)  # hand 1
        self.assertEqual(get_hand_pot_size_bb(fake_tournament['hands'][1]), 7.4)  # hand 2
        self.assertEqual(get_hand_pot_size_bb(fake_tournament['hands'][2]), 61.8)  # hand 3

    def test_get_hand_level(self):
        self.assertEqual(get_hand_level(fake_tournament['hands'][0]), '3 (500.00/1000.00)')  # hand 1
        self.assertEqual(get_hand_level(fake_tournament['hands'][1]), '3 (500.00/1000.00)')  # hand 2
        self.assertEqual(get_hand_level(fake_tournament['hands'][2]), '233 (4500.00/1000.00)')  # hand 3

    def test_get_hand_my_cards(self):
        self.assertEqual(get_hand_my_cards(fake_tournament['hands'][0]), None)  # hand 1, dealt after button
        self.assertEqual(get_hand_my_cards(fake_tournament['hands'][1]), '6c Ac')  # hand 2
        self.assertEqual(get_hand_my_cards(fake_tournament['hands'][2]), '2h 7h')  # hand 3

    def test_get_hand_board_cards(self):
        self.assertEqual(get_hand_board_cards(fake_tournament['hands'][0]), 'Kc Kh 2s')  # hand 1
        self.assertEqual(get_hand_board_cards(fake_tournament['hands'][1]), '3h Kd Tc Jc')  # hand 2
        self.assertEqual(get_hand_board_cards(fake_tournament['hands'][2]), 'Qc 3d 5h 3c 5c')  # hand 3

    def test_get_tourney_id(self):
        self.assertEqual(get_tourney_id(fake_tournament['hands'][0]), 23098704)
        self.assertEqual(get_tourney_id(fake_tournament['hands'][1]), 23098704)
        self.assertEqual(get_tourney_id(fake_tournament['hands'][2]), 23098704)

    def test_get_hand_id(self):
        self.assertEqual(get_hand_id(fake_tournament['hands'][0]), 620221089)
        self.assertEqual(get_hand_id(fake_tournament['hands'][1]), 620221751)
        self.assertEqual(get_hand_id(fake_tournament['hands'][2]), 620222790)

    # def test_get_winner_of_hand(self):
    #     self.assertEqual(get_winners_of_hand(fake_tournament['hands'][0]), 'RJB2020')
    #     self.assertEqual(get_winners_of_hand(fake_tournament['hands'][1]), 'Hows_That_Fair')
    #     self.assertEqual(get_winners_of_hand(fake_tournament['hands'][2]), 'ricthepric')
    #     self.assertEqual(get_winners_of_hand(fake_tournament['hands'][3]), 'solving4what,PotNoodle99912')

    def test_get_winner_of_side_pot(self):

        # load hands from long txt file
        hands = []
        with open('./fake_data_tourneys/long_hand_history_for_tests.txt', 'r') as f:
            data = f.read()
            hhtext = copy.deepcopy(data)
        str_to_hands = hhtext.split('\n\n')
        for hand_ in str_to_hands:
            hands.append(hand_)

        results = [
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'no-side-pot',
            'Bubbazinitty',
            'slbetters'
        ]

        for hand, result in zip(hands, results):
            self.assertEqual(get_winner_of_side_pot(hand, pot_nb=1), result)

        # TEST FOR POT NB 2 AND 3 !!!



    def test_get_side_pot_size(self):
        # load hands from long txt file
        hands = []
        with open('./fake_data_tourneys/long_hand_history_for_tests.txt', 'r') as f:
            data = f.read()
            hhtext = copy.deepcopy(data)
        str_to_hands = hhtext.split('\n\n')
        for hand_ in str_to_hands:
            hands.append(hand_)

        # side pot 1
        results = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1.59,
            2.05,
            1.93,
            5.83,
        ]
        for hand, result in zip(hands, results):
            self.assertEqual(get_side_pot_size(hand, pot_nb=1), result)

        # side pot 2
        results = [
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            8.13
        ]
        for hand, result in zip(hands, results):
            self.assertEqual(get_side_pot_size(hand, pot_nb=2), result)

        # side pot 3
        results = [
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            1.67
        ]
        for hand, result in zip(hands, results):
            self.assertEqual(get_side_pot_size(hand, pot_nb=3), result)


    def test_get_main_pot_size(self):
        # load hands from long txt file
        hands = []
        with open('./fake_data_tourneys/long_hand_history_for_tests.txt', 'r') as f:
            data = f.read()
            hhtext = copy.deepcopy(data)
        str_to_hands = hhtext.split('\n\n')
        for hand_ in str_to_hands:
            hands.append(hand_)

        results = [2.2, 3.3, 37.05, 2.3, 7.95, 5.6,
                   30.1, 3.3, 3.3, 11.62, 3.8, 8.73,
                   19.57, 3.2, 27.67, 10.29, 17.84,
                   3.2, 3.2, 43.92, 2.7, 1.42, 3.45]

        for hand, result in zip(hands, results):
            self.assertEqual(get_main_pot_size(hand), result)


    def test_get_winner_of_main_pot(self):

        # load hands from long txt file
        hands = []
        with open('./fake_data_tourneys/long_hand_history_for_tests.txt', 'r') as f:
            data = f.read()
            hhtext = copy.deepcopy(data)
        str_to_hands = hhtext.split('\n\n')
        for hand_ in str_to_hands:
            hands.append(hand_)

        self.assertEqual(get_winner_of_main_pot(hands[0]), 'PotNoodle99912')
        self.assertEqual(get_winner_of_main_pot(hands[1]), 'yaya12')
        self.assertEqual(get_winner_of_main_pot(hands[2]), 'Didlo1987')
        self.assertEqual(get_winner_of_main_pot(hands[3]), 'yaya12')
        self.assertEqual(get_winner_of_main_pot(hands[4]), 'seamynutz')
        self.assertEqual(get_winner_of_main_pot(hands[5]), 'xiooong')
        self.assertEqual(get_winner_of_main_pot(hands[6]), 'omc7272')
        self.assertEqual(get_winner_of_main_pot(hands[7]), 'jbgutrock')
        self.assertEqual(get_winner_of_main_pot(hands[8]), 'yaya12')
        self.assertEqual(get_winner_of_main_pot(hands[9]),  '**[CHOP-CHOP]**')
        self.assertEqual(get_winner_of_main_pot(hands[10]), 'Sgt. Fury')
        self.assertEqual(get_winner_of_main_pot(hands[11]), 'seamynutz')
        self.assertEqual(get_winner_of_main_pot(hands[12]), 'jbgutrock')
        self.assertEqual(get_winner_of_main_pot(hands[13]), 'yaya12')
        self.assertEqual(get_winner_of_main_pot(hands[14]), 'xiooong')
        self.assertEqual(get_winner_of_main_pot(hands[15]), 'Vadims')
        self.assertEqual(get_winner_of_main_pot(hands[16]), 'PotNoodle99912')
        self.assertEqual(get_winner_of_main_pot(hands[17]), 'Didlo1987')
        self.assertEqual(get_winner_of_main_pot(hands[18]), 'PotNoodle99912')
        self.assertEqual(get_winner_of_main_pot(hands[19]), 'jbgutrock')
        self.assertEqual(get_winner_of_main_pot(hands[20]), 'Sgt. Fury')
        self.assertEqual(get_winner_of_main_pot(hands[21]), 'Ginijo')
        self.assertEqual(get_winner_of_main_pot(hands[22]), 'slbetters')


    def test_get_stack_size_start_of_hand(self):
        self.assertEqual(get_stack_size_start_of_hand(fake_tournament['hands'][0]), None)
        self.assertEqual(get_stack_size_start_of_hand(fake_tournament['hands'][1]), 30.0)
        self.assertEqual(get_stack_size_start_of_hand(fake_tournament['hands'][2]), 29.9)

    # tests for opponents.py
    def test_extract_opponents_names(self):
        extraction = extract_opponents_names(fake_tournament['summary'])
        self.assertEqual(len(extraction), 48)
        self.assertTrue(len(extraction) == len(set(extraction)))

    # tests for create_tournament.py
    def test_extract_price_from_title(self):
        self.assertEqual(extract_price_from_title(fake_tournament['title']), 0.55)

    def test_extract_id_from_content(self):
        self.assertEqual(extract_id_from_content(fake_tournament['hands'][0]), 23098704)

    def test_extract_finished_time_from_content(self):
        self.assertEqual(extract_finished_time_from_content(fake_tournament['hands'][-1]), '2020/12/12 05:36:34')

    def test_extract_elapsed_time_from_content(self):
        self.assertEqual(extract_elapsed_time_from_content(fake_tournament['hands'][0] + fake_tournament['hands'][-1]), 7)

    def test_extract_prize(self):
        self.assertEqual(extract_prize(fake_tournament['summary']), 0.93)

    def test_extract_position(self):
        self.assertEqual(extract_position(fake_tournament['summary']), 12)


if __name__ == '__main__':
    unittest.main()

