import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.position_info.reorder_seats_with_btn_first import reorder_seats_with_btn_first


class test(unittest.TestCase):
    def test_reorder_seats_with_btn_first(self):

        input = [
            (['Seat 3: PokerPete24 (40518.00)',
            'Seat 4: taoDP (6595.00)',
            'Seat 5: joeyv (37808.00)',
            'Seat 6: pking69 (129924.00)',
            'Seat 7: first shirt (91195.00)',
            'Seat 9: PotNoodle99912 (47175.00)'], 2),

            (['Seat 3: PokerPete24 (40518.00)',
             'Seat 4: taoDP (6595.00)',
             'Seat 5: joeyv (37808.00)',
             'Seat 6: pking69 (129924.00)',
             'Seat 7: first shirt (91195.00)',
             'Seat 9: PotNoodle99912 (47175.00)'], 9),

            (['Seat 3: PokerPete24 (40518.00)',
             'Seat 4: taoDP (6595.00)',
             'Seat 5: joeyv (37808.00)',
             'Seat 6: pking69 (129924.00)',
             'Seat 7: first shirt (91195.00)',
             'Seat 9: PotNoodle99912 (47175.00)'], 5),

            (['Seat 3: PokerPete24 (40518.00)',
             'Seat 4: taoDP (6595.00)',
             'Seat 5: joeyv (37808.00)',
             'Seat 6: pking69 (129924.00)',
             'Seat 7: first shirt (91195.00)'], 9)]

        expected = [
            ['Seat 3: PokerPete24 (40518.00)', 'Seat 4: taoDP (6595.00)', 'Seat 5: joeyv (37808.00)', 'Seat 6: pking69 (129924.00)', 'Seat 7: first shirt (91195.00)', 'Seat 9: PotNoodle99912 (47175.00)'],
            ['Seat 9: PotNoodle99912 (47175.00)', 'Seat 3: PokerPete24 (40518.00)', 'Seat 4: taoDP (6595.00)', 'Seat 5: joeyv (37808.00)', 'Seat 6: pking69 (129924.00)', 'Seat 7: first shirt (91195.00)'],
            ['Seat 5: joeyv (37808.00)', 'Seat 6: pking69 (129924.00)', 'Seat 7: first shirt (91195.00)', 'Seat 9: PotNoodle99912 (47175.00)', 'Seat 3: PokerPete24 (40518.00)', 'Seat 4: taoDP (6595.00)'],
            ['Seat 3: PokerPete24 (40518.00)', 'Seat 4: taoDP (6595.00)', 'Seat 5: joeyv (37808.00)', 'Seat 6: pking69 (129924.00)', 'Seat 7: first shirt (91195.00)']

        ]

        self.assertEqual(reorder_seats_with_btn_first(input[0][0], input[0][1]), expected[0])
        self.assertEqual(reorder_seats_with_btn_first(input[1][0], input[1][1]), expected[1])
        self.assertEqual(reorder_seats_with_btn_first(input[2][0], input[2][1]), expected[2])
        self.assertEqual(reorder_seats_with_btn_first(input[3][0], input[3][1]), expected[3])
