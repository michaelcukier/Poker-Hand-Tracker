import unittest
from hh_import.extract_data_from_raw_hh import *
from .fake_data import *

class test_extract_from_raw_hh(unittest.TestCase):

    def test_extract_price_from_title(self):
        self.assertEqual(extract_price_from_title(fake_data['title']), 0.55)

    def test_extract_id_from_content(self):
        self.assertEqual(extract_id_from_content(fake_data['content']), 23098704)

    def test_extract_finished_time_from_content(self):
        self.assertEqual(extract_finished_time_from_content(fake_data['content']), '2020/12/12 06:12:03 UTC')

    def test_extract_elapsed_time_from_content(self):
        self.assertEqual(extract_elapsed_time_from_content(fake_data['content']), 42)

    def test_extract_hands_from_content(self):
        self.assertEqual(len(extract_hands_from_content(fake_data['content'])), 38)

    def test_extract_opponents_names(self):
        self.assertEqual(len(extract_opponents_names(fake_tournament_summary)), 62)

    def test_extract_nb_of_participants(self):
        self.assertEqual(extract_nb_of_participants(fake_tournament_summary), 62)

    def test_extract_prize(self):
        self.assertEqual(extract_prize(fake_tournament_summary), 0.93)

    def test_extract_position(self):
        self.assertEqual(extract_position(fake_tournament_summary), 12)

    def test_extract_replayer_links(self):
        self.assertEqual(len(generate_hh_links_replayer(fake_data['content'])), 38)

    def test_extract_from_raw_hh(self):

        extraction = extract_from_raw_hh(fake_full_data)

        self.assertEqual(extraction[0]['new_hands'][0]['board_cards'], 'Kc Kh 2s')
        self.assertEqual(extraction[0]['new_hands'][0]['hand_type'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][0]['level'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][0]['my_cards'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][0]['pot_size'], 'xxx')
        self.assertIn(extraction[0]['new_hands'][0]['replayer_link'], 'https://pokeit.co/public/')
        self.assertEqual(extraction[0]['new_hands'][0]['time'], '2020/12/12 05:30:01 UT')

        self.assertEqual(extraction[0]['new_hands'][1]['board_cards'], 'Kc Kh 2s')
        self.assertEqual(extraction[0]['new_hands'][1]['hand_type'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][1]['level'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][1]['my_cards'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][1]['pot_size'], 'xxx')
        self.assertIn(extraction[0]['new_hands'][1]['replayer_link'], 'https://pokeit.co/public/')
        self.assertEqual(extraction[0]['new_hands'][1]['time'], '2020/12/12 05:30:01 UT')

        self.assertEqual(extraction[0]['new_hands'][1]['board_cards'], 'Kc Kh 2s')
        self.assertEqual(extraction[0]['new_hands'][1]['hand_type'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][1]['level'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][1]['my_cards'], 'xxx')
        self.assertEqual(extraction[0]['new_hands'][1]['pot_size'], 'xxx')
        self.assertIn(extraction[0]['new_hands'][1]['replayer_link'], 'https://pokeit.co/public/')

        self.assertEqual(len(extraction[0]['new_opponents']), 10000)
        self.assertTrue(len(extraction[0]['new_opponents']) == len(set(extraction[0]['new_opponents']())))

        self.assertTrue(len(extraction[0]['new_tournament']['elapsed_time']) == 100)
        self.assertTrue(len(extraction[0]['new_tournament']['finished_time']) == 100)
        self.assertTrue(len(extraction[0]['new_tournament']['id']) == 100)
        self.assertTrue(len(extraction[0]['new_tournament']['position']) == 100)
        self.assertTrue(len(extraction[0]['new_tournament']['price']) == 100)
        self.assertTrue(len(extraction[0]['new_tournament']['prize']) == 100)

        # self.assertEqual(
        #     extract_from_raw_hh(fake_full_data)['new_hands'],
        #     [{'new_hands': [{'board_cards': 'Kc Kh 2s',
        #                      'hand_type': None,
        #                      'level': ' 3 (500.00/1000.00)',
        #                      'my_cards': None,
        #                      'pot_size': 8600,
        #                      'replayer_link': 'https://pokeit.co/public/0qNRpE9/r',
        #                      'time': '2020/12/12 05:30:01 UTC'},
        #                     {'board_cards': '3h Kd Tc Jc',
        #                      'hand_type': None,
        #                      'level': ' 3 (500.00/1000.00)',
        #                      'my_cards': '6c Ac',
        #                      'pot_size': 7400,
        #                      'replayer_link': 'https://pokeit.co/public/4qNRpPb/r',
        #                      'time': '2020/12/12 05:30:37 UTC'}],
        #       'new_opponents': ['prettylady24',
        #                         'BarbaraLahey',
        #                         'AZabko007',
        #                         'Amp12',
        #                         'Shocmaka',
        #                         'CaptnKeyes',
        #                         'jjoyce',
        #                         'ricthepric',
        #                         'RJB2020',
        #                         'Zod42',
        #                         'lcz1996',
        #                         'PotNoodle99912',
        #                         'Dead_Money_007',
        #                         'SonicTurtle',
        #                         'EmoQQQ',
        #                         'Diigy',
        #                         'noizymind',
        #                         'Pirate Fish',
        #                         'crossjamie',
        #                         'Yodaveed',
        #                         'jujy42',
        #                         'RICKSAGA',
        #                         'Chingu',
        #                         '6jackl',
        #                         'CompDonk',
        #                         'KCiardiello',
        #                         'gamerfreak315',
        #                         'therealmre',
        #                         'jonlama',
        #                         'Hows_That_Fair',
        #                         'aRoyal Hand',
        #                         'Djohnic1',
        #                         'JoshGordon',
        #                         'kook1234',
        #                         'Tommy Naples',
        #                         'Iknownow1',
        #                         'coachmills',
        #                         'royal abe',
        #                         'jaybezee',
        #                         'WanHungLo',
        #                         'mizkitty',
        #                         'mattei',
        #                         'AZabko007',
        #                         'JoshGordon',
        #                         'Silhouette415',
        #                         'THE RVRS ACE',
        #                         'Barney Boy',
        #                         'aRoyal Hand',
        #                         'Pocket7s77',
        #                         'crossjamie',
        #                         'Zees40660',
        #                         'LILSOJU',
        #                         'cluster phuck',
        #                         'mizkitty',
        #                         'Hows_That_Fair',
        #                         'therealmre',
        #                         'mattei',
        #                         'lcz1996',
        #                         'Zees40660',
        #                         'WanHungLo',
        #                         'WanHungLo',
        #                         'Iknownow1'],
        #       'new_tournament': {'elapsed_time': 1,
        #                          'finished_time': '2020/12/12 05:30:37 UTC',
        #                          'id': 23098704,
        #                          'position': 12,
        #                          'price': 0.55,
        #                          'prize': 0.93}}]
        # )


if __name__ == '__main__':
    unittest.main()
