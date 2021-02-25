import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.position_player_name import *
from GLOBAL_VARIABLES import TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):

    def test_get_seats_and_nb_of_players(self):
        hands = get_hands_in_list(
            TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER,
            ["HH20210220 SITGOID-G24095328T3 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 -- for position from 9 to 2.txt"])

        expected = [
            {'lst': ['Seat 1: MateusVR (146796.00)', 'Seat 2: PotNoodle99912 (155072.00)', 'Seat 3: Frank126 (97418.00)', 'Seat 4: TiltedMILF (53800.00)', 'Seat 5: What_Truth (43825.00)', 'Seat 6: VUSEDSV (54225.00)', 'Seat 7: coog (59284.00)', 'Seat 8: dartdog (91180.00)', 'Seat 9: JokesyWales (48400.00)'], 'nb_of_players': 9},
            {'lst': ['Seat 1: MateusVR (146296.00)', 'Seat 2: PotNoodle99912 (154572.00)', 'Seat 3: Frank126 (94418.00)', 'Seat 4: TiltedMILF (48300.00)', 'Seat 6: VUSEDSV (53725.00)', 'Seat 7: coog (114109.00)', 'Seat 8: dartdog (90680.00)', 'Seat 9: JokesyWales (47900.00)'], 'nb_of_players': 8},
            {'lst': ['Seat 1: MateusVR (135796.00)', 'Seat 2: PotNoodle99912 (223797.00)', 'Seat 3: Frank126 (93918.00)', 'Seat 4: TiltedMILF (45300.00)', 'Seat 7: coog (113609.00)', 'Seat 8: dartdog (90180.00)', 'Seat 9: JokesyWales (47400.00)'], 'nb_of_players': 7},
            {'lst': ['Seat 1: MateusVR (125696.00)', 'Seat 2: PotNoodle99912 (238797.00)', 'Seat 3: Frank126 (91818.00)', 'Seat 4: TiltedMILF (43200.00)', 'Seat 7: coog (159409.00)', 'Seat 8: dartdog (91080.00)'], 'nb_of_players': 6},
            {'lst': ['Seat 1: MateusVR (111796.00)', 'Seat 2: PotNoodle99912 (376715.00)', 'Seat 4: TiltedMILF (49800.00)', 'Seat 7: coog (152009.00)', 'Seat 8: dartdog (59680.00)'], 'nb_of_players': 5},
            {'lst': ['Seat 2: PotNoodle99912 (518611.00)', 'Seat 4: TiltedMILF (36500.00)', 'Seat 7: coog (138709.00)', 'Seat 8: dartdog (56180.00)'], 'nb_of_players': 4},
            {'lst': ['Seat 2: PotNoodle99912 (580611.00)', 'Seat 7: coog (125009.00)', 'Seat 8: dartdog (44380.00)'], 'nb_of_players': 3},
            {'lst': ['Seat 2: PotNoodle99912 (697201.00)', 'Seat 7: coog (52799.00)'], 'nb_of_players': 2}]

        for idx, h in enumerate(hands):
            self.assertEqual(get_seats_and_nb_of_players(h), expected[idx])

    def test_get_btn_position_nb(self):
        hands = get_hands_in_list(
            TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER,
            ["HH20210220 SITGOID-G24095328T3 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 -- for position from 9 to 2.txt"])
        expected = [2, 3, 4, 1, 2, 2, 2, 7]
        for idx, h in enumerate(hands):
            self.assertEqual(get_btn_position_nb(h), expected[idx])

    def test_position_player_name(self):
        hands = get_hands_in_list(
            TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER,
            ["HH20210220 SITGOID-G24095328T3 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 -- for position from 9 to 2.txt"])


        # for x in hands:
        #     print(x)
        #     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #
        # quit()

        expected = [
            {
                'BTN': 'PotNoodle99912',
                'SB': 'Frank126',
                'BB': 'TiltedMILF',
                'UTG': 'What_Truth',
                'UTG+1': 'VUSEDSV',
                'MP': 'coog',
                'MP+1': 'dartdog',
                'MP+2': 'JokesyWales',
                'CO': 'MateusVR'
            },

            {
                "BTN": 'Frank126',
                "SB": 'TiltedMILF',
                "BB": 'VUSEDSV',
                "UTG": 'coog',
                "UTG+1": 'dartdog',
                "MP": 'JokesyWales',
                "MP+1": 'MateusVR',
                'MP+2': None,
                "CO": 'PotNoodle99912',
            },

            {
                "BTN": 'TiltedMILF',
                "SB": 'coog',
                "BB": 'dartdog',
                "UTG": 'JokesyWales',
                "UTG+1": 'MateusVR',
                "MP": 'PotNoodle99912',
                "MP+1": None,
                'MP+2': None,
                "CO": 'Frank126'
            },

            {
                "BTN": 'MateusVR',
                "SB": 'PotNoodle99912',
                "BB": 'Frank126',
                "UTG": 'TiltedMILF',
                "UTG+1": None,
                "MP": 'coog',
                "MP+1": None,
                'MP+2': None,
                "CO": 'dartdog'
            },

            {
                "BTN": 'PotNoodle99912',
                "SB": 'TiltedMILF',
                "BB": 'coog',
                "UTG": 'dartdog',
                "UTG+1": None,
                "MP": None,
                "MP+1": None,
                'MP+2': None,
                "CO": 'MateusVR',
             },


            {
                "BTN": 'PotNoodle99912',
                "SB": 'TiltedMILF',
                "BB": 'coog',
                "UTG": None,
                "UTG+1": None,
                "MP": None,
                "MP+1": None,
                'MP+2': None,
                "CO": 'dartdog'
            },

            {
                "BTN": 'PotNoodle99912',
                "SB": 'coog',
                "BB": 'dartdog',
                "UTG": None,
                "UTG+1": None,
                "MP": None,
                "MP+1": None,
                'MP+2': None,
                "CO": None
            },

            {
                'BTN': None,
                "SB": 'coog',
                "BB": 'PotNoodle99912',
                "UTG": None,
                "UTG+1": None,
                "MP": None,
                "MP+1": None,
                'MP+2': None,
                "CO": None
            }
        ]


        self.assertEqual(position_player_name(hands[0]), expected[0])
        self.assertEqual(position_player_name(hands[1]), expected[1])
        self.assertEqual(position_player_name(hands[2]), expected[2])
        self.assertEqual(position_player_name(hands[3]), expected[3])
        self.assertEqual(position_player_name(hands[4]), expected[4])
        self.assertEqual(position_player_name(hands[5]), expected[5])
        self.assertEqual(position_player_name(hands[6]), expected[6])
        self.assertEqual(position_player_name(hands[7]), expected[7])
