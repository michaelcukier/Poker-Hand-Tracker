import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.position_info.extract_name_from_seat_line import extract_name_from_seat_line


class test(unittest.TestCase):
    def test_extract_name_from_seat_line(self):

        examples = [
            'Seat 3: PokerPete24 (40518.00)',
            'Seat 3: joeyv will be allowed to play after the button'
        ]

        expected = [
            'PokerPete24',
            None
        ]

        self.assertEqual(extract_name_from_seat_line(examples[0]), expected[0])
        self.assertEqual(extract_name_from_seat_line(examples[1]), expected[1])
