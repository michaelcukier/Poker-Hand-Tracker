import unittest

from hh_import.dict_to_clean_data.new_hands import *
from hh_import.dict_to_clean_data.new_opponents import *
from hh_import.dict_to_clean_data.new_tournaments import *

from fake_data_tourneys.fake_data import *


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

    # tests for new_opponents.py
    def test_extract_opponents_names(self):
        extraction = extract_opponents_names(fake_tournament['summary'])
        self.assertEqual(len(extraction), 49)
        self.assertTrue(len(extraction) == len(set(extraction)))

    # tests for new_tournaments.py
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

