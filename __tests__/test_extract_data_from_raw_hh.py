import unittest

from hh_import.dict_to_clean_data.new_hands import *
from hh_import.dict_to_clean_data.new_opponents import *
from hh_import.dict_to_clean_data.new_tournaments import *


from fake_data import *


class test_extract_from_raw_hh(unittest.TestCase):

    # tests for new_hands.py
    def test_extract_hands_from_content_to_list(self):
        self.assertEqual(len(extract_hands_from_content_to_list(fake_tournament['content'])), 2)

    def test_get_hand_time(self):
        hands = extract_hands_from_content_to_list(fake_tournament['content'])
        self.assertEqual(get_hand_time(hands[0]), '2020/12/12 05:30:37 UTC')  # hand 2
        self.assertEqual(get_hand_time(hands[1]), '2020/12/12 05:36:34 UTC')  # hand 2

    def test_get_hand_pot_size(self):
        hands = extract_hands_from_content_to_list(fake_tournament['content'])
        self.assertEqual(get_hand_pot_size(hands[0]), 7400)  # hand 1
        self.assertEqual(get_hand_pot_size(hands[1]), 61800)  # hand 2

    def test_get_hand_level(self):
        hands = extract_hands_from_content_to_list(fake_tournament['content'])
        self.assertEqual(get_hand_level(hands[0]), '3 (500.00/1000.00)')  # hand 1
        self.assertEqual(get_hand_level(hands[1]), '3 (500.00/1000.00)')  # hand 2

    def test_get_hand_my_cards(self):
        hands = extract_hands_from_content_to_list(fake_tournament['content'])
        self.assertEqual(get_hand_my_cards(hands[0]), '6c Ac')  # hand 1
        self.assertEqual(get_hand_my_cards(hands[1]), '2h 7h')  # hand 2

    def test_get_hand_board_cards(self):
        hands = extract_hands_from_content_to_list(fake_tournament['content'])
        self.assertEqual(get_hand_board_cards(hands[0]), '3h Kd Tc Jc')  # hand 1
        self.assertEqual(get_hand_board_cards(hands[1]), 'Qc 3d 5h 3c 5c')  # hand 2

    def test_get_hand_type(self):
        hands = extract_hands_from_content_to_list(fake_tournament['content'])
        self.assertEqual(get_hand_type(hands[0]), 'hand-type')  # hand 1
        self.assertEqual(get_hand_type(hands[1]), 'hand-type')  # hand 2

    # tests for new_opponents.py
    def test_extract_opponents_names(self):
        extraction = extract_opponents_names(fake_tournament['tourney_summary'])
        self.assertEqual(len(extraction), 49)
        self.assertTrue(len(extraction) == len(set(extraction)))

    # tests for new_tournaments.py
    def test_extract_price_from_title(self):
        self.assertEqual(extract_price_from_title(fake_tournament['title']), 0.55)

    def test_extract_id_from_content(self):
        self.assertEqual(extract_id_from_content(fake_tournament['content']), 23098704)

    def test_extract_finished_time_from_content(self):
        self.assertEqual(extract_finished_time_from_content(fake_tournament['content']), '2020/12/12 05:36:34')

    def test_extract_elapsed_time_from_content(self):
        self.assertEqual(extract_elapsed_time_from_content(fake_tournament['content']), 7)

    def test_extract_prize(self):
        self.assertEqual(extract_prize(fake_tournament['tourney_summary']), 0.93)

    def test_extract_position(self):
        self.assertEqual(extract_position(fake_tournament['tourney_summary']), 12)


if __name__ == '__main__':
    unittest.main()

