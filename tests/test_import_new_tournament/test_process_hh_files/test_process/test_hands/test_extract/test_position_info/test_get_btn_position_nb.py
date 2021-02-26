import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.position_info.get_btn_position_nb import get_btn_position_nb
from .fake_data import hands


class test(unittest.TestCase):
    def test_get_btn_position_nb(self):

        expected = [
            2,
            4,
            5,
            6,
            7,
            8,
            9,
            1,
            2,
            3,
            4,
            5,
            8,
            9,
            1]

        self.assertEqual(get_btn_position_nb(hands[0]), expected[0])
        self.assertEqual(get_btn_position_nb(hands[1]), expected[1])
        self.assertEqual(get_btn_position_nb(hands[2]), expected[2])
        self.assertEqual(get_btn_position_nb(hands[3]), expected[3])
        self.assertEqual(get_btn_position_nb(hands[4]), expected[4])
        self.assertEqual(get_btn_position_nb(hands[5]), expected[5])
        self.assertEqual(get_btn_position_nb(hands[6]), expected[6])
        self.assertEqual(get_btn_position_nb(hands[7]), expected[7])
        self.assertEqual(get_btn_position_nb(hands[8]), expected[8])
        self.assertEqual(get_btn_position_nb(hands[9]), expected[9])
        self.assertEqual(get_btn_position_nb(hands[10]), expected[10])
        self.assertEqual(get_btn_position_nb(hands[11]), expected[11])
        self.assertEqual(get_btn_position_nb(hands[12]), expected[12])
        self.assertEqual(get_btn_position_nb(hands[13]), expected[13])
        self.assertEqual(get_btn_position_nb(hands[14]), expected[14])
