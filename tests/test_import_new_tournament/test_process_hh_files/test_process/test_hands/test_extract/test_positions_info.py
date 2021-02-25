import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.positions_info import *
from GLOBAL_VARIABLES import TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):

    # def test_get_seats_and_nb_of_players(self):
    #     hands = get_hands_in_list(
    #         TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER,
    #         ["HH20210220 SITGOID-G24095328T3 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 -- for position from 9 to 2.txt"])
    #
    #     expected = [
    #         {'lst': ['Seat 1: MateusVR (146796.00)', 'Seat 2: PotNoodle99912 (155072.00)', 'Seat 3: Frank126 (97418.00)', 'Seat 4: TiltedMILF (53800.00)', 'Seat 5: What_Truth (43825.00)', 'Seat 6: VUSEDSV (54225.00)', 'Seat 7: coog (59284.00)', 'Seat 8: dartdog (91180.00)', 'Seat 9: JokesyWales (48400.00)'], 'nb_of_players': 9},
    #         {'lst': ['Seat 1: MateusVR (146296.00)', 'Seat 2: PotNoodle99912 (154572.00)', 'Seat 3: Frank126 (94418.00)', 'Seat 4: TiltedMILF (48300.00)', 'Seat 6: VUSEDSV (53725.00)', 'Seat 7: coog (114109.00)', 'Seat 8: dartdog (90680.00)', 'Seat 9: JokesyWales (47900.00)'], 'nb_of_players': 8},
    #         {'lst': ['Seat 1: MateusVR (135796.00)', 'Seat 2: PotNoodle99912 (223797.00)', 'Seat 3: Frank126 (93918.00)', 'Seat 4: TiltedMILF (45300.00)', 'Seat 7: coog (113609.00)', 'Seat 8: dartdog (90180.00)', 'Seat 9: JokesyWales (47400.00)'], 'nb_of_players': 7},
    #         {'lst': ['Seat 1: MateusVR (125696.00)', 'Seat 2: PotNoodle99912 (238797.00)', 'Seat 3: Frank126 (91818.00)', 'Seat 4: TiltedMILF (43200.00)', 'Seat 7: coog (159409.00)', 'Seat 8: dartdog (91080.00)'], 'nb_of_players': 6},
    #         {'lst': ['Seat 1: MateusVR (111796.00)', 'Seat 2: PotNoodle99912 (376715.00)', 'Seat 4: TiltedMILF (49800.00)', 'Seat 7: coog (152009.00)', 'Seat 8: dartdog (59680.00)'], 'nb_of_players': 5},
    #         {'lst': ['Seat 2: PotNoodle99912 (518611.00)', 'Seat 4: TiltedMILF (36500.00)', 'Seat 7: coog (138709.00)', 'Seat 8: dartdog (56180.00)'], 'nb_of_players': 4},
    #         {'lst': ['Seat 2: PotNoodle99912 (580611.00)', 'Seat 7: coog (125009.00)', 'Seat 8: dartdog (44380.00)'], 'nb_of_players': 3},
    #         {'lst': ['Seat 2: PotNoodle99912 (697201.00)', 'Seat 7: coog (52799.00)'], 'nb_of_players': 2}]
    #
    #     for idx, h in enumerate(hands):
    #         self.assertEqual(get_seats_and_nb_of_players(h), expected[idx])
    #
    # def test_get_btn_position_nb(self):
    #     hands = get_hands_in_list(
    #         TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER,
    #         ["HH20210220 SITGOID-G24095328T3 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 -- for position from 9 to 2.txt"])
    #     expected = [2, 3, 4, 1, 2, 2, 2, 7]
    #     for idx, h in enumerate(hands):
    #         self.assertEqual(get_btn_position_nb(h), expected[idx])

    def test_position_info(self):
        hands = get_hands_in_list(
            TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER,
            ["HH20210220 SITGOID-G24095328T3 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0 -- for position from 9 to 2.txt"])


        expected = [
            {
                'BTN': {'Name': 'PotNoodle99912', 'Stack': 155072.00, 'Cards': 'Qc 6s'},
                'SB':  {'Name': 'Frank126', 'Stack': 97418.00, 'Cards': None},
                'BB':  {'Name': 'TiltedMILF', 'Stack': 53800.00, 'Cards': None},
                'UTG':  {'Name': 'What_Truth', 'Stack': 43825.00, 'Cards': 'Ad Tc'},
                'UTG+1':  {'Name': 'VUSEDSV', 'Stack': 54225.00, 'Cards': None},
                'MP':  {'Name': 'coog', 'Stack': 59284.00, 'Cards': 'Td Th'},
                'MP+1':  {'Name': 'dartdog', 'Stack': 91180.00, 'Cards': None},
                'MP+2':  {'Name': 'JokesyWales', 'Stack': 48400.00, 'Cards': None},
                'CO':  {'Name': 'MateusVR', 'Stack': 146796.00, 'Cards': None}
            },

            {
                "BTN":  {'Name': 'Frank126', 'Stack': 94418.00, 'Cards': None},
                "SB":  {'Name': 'TiltedMILF', 'Stack': 48300.00, 'Cards': None},
                "BB":  {'Name': 'VUSEDSV', 'Stack': 53725.00, 'Cards': 'Qd Qs'},
                "UTG":  {'Name': 'coog', 'Stack': 114109.00, 'Cards': None},
                "UTG+1":  {'Name': 'dartdog', 'Stack': 90680.00, 'Cards': None},
                "MP":  {'Name': 'JokesyWales', 'Stack': 47900.00, 'Cards': None},
                "MP+1":  {'Name': 'MateusVR', 'Stack': 146296.00, 'Cards': None},
                'MP+2':  {'Name': None, 'Stack': None, 'Cards': None},
                "CO":  {'Name': 'PotNoodle99912', 'Stack': 154572.00, 'Cards': 'Ad Ac'},
            },

            {
                "BTN":  {'Name': 'TiltedMILF', 'Stack': 45300.00, 'Cards': None},
                "SB":  {'Name': 'coog', 'Stack': 113609.00, 'Cards': 'Kh Ac'},
                "BB":  {'Name': 'dartdog', 'Stack': 90180.00, 'Cards': None},
                "UTG":  {'Name': 'JokesyWales', 'Stack': 47400.00, 'Cards': '5s As'},
                "UTG+1":  {'Name': 'MateusVR', 'Stack': 135796.00, 'Cards': None},
                "MP":  {'Name': 'PotNoodle99912', 'Stack': 223797.00, 'Cards': '9d 8c'},
                "MP+1":  {'Name': None, 'Stack': None, 'Cards': None},
                'MP+2':  {'Name': None, 'Stack': None, 'Cards': None},
                "CO":  {'Name': 'Frank126', 'Stack': 93918.00, 'Cards': None}
            },

            {
                "BTN":  {'Name': 'MateusVR', 'Stack': 125696.00, 'Cards': None},
                "SB":  {'Name': 'PotNoodle99912', 'Stack': 238797.00, 'Cards': 'Kh 8d'},
                "BB":  {'Name': 'Frank126', 'Stack': 91818.00, 'Cards': 'Jh Js'},
                "UTG":  {'Name': 'TiltedMILF', 'Stack': 43200.00, 'Cards': None},
                "UTG+1":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP":  {'Name': 'coog', 'Stack': 159409.00, 'Cards': None},
                "MP+1":  {'Name': None, 'Stack': None, 'Cards': None},
                'MP+2':  {'Name': None, 'Stack': None, 'Cards': None},
                "CO":  {'Name': 'dartdog', 'Stack': 91080.00, 'Cards': None}
            },

            {
                "BTN":  {'Name': 'PotNoodle99912', 'Stack': 376715.00, 'Cards': 'Qs Ad'},
                "SB":  {'Name': 'TiltedMILF', 'Stack': 49800.00, 'Cards': None},
                "BB":  {'Name': 'coog', 'Stack': 152009.00, 'Cards': None},
                "UTG":  {'Name': 'dartdog', 'Stack': 59680.00, 'Cards': None},
                "UTG+1":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP+1":  {'Name': None, 'Stack': None, 'Cards': None},
                'MP+2':  {'Name': None, 'Stack': None, 'Cards': None},
                "CO":  {'Name': 'MateusVR', 'Stack': 111796.00, 'Cards': 'Kd Ac'}
             },


            {
                "BTN":  {'Name': 'PotNoodle99912', 'Stack': 518611.00, 'Cards': '8s 3d'},
                "SB":  {'Name': 'TiltedMILF', 'Stack': 36500.00, 'Cards': 'Qs Ah'},
                "BB":  {'Name': 'coog', 'Stack': 138709.00, 'Cards': 'Ad 9c'},
                "UTG":  {'Name': None, 'Stack': None, 'Cards': None},
                "UTG+1":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP+1":  {'Name': None, 'Stack': None, 'Cards': None},
                'MP+2':  {'Name': None, 'Stack': None, 'Cards': None},
                "CO":  {'Name': 'dartdog', 'Stack': 56180.00, 'Cards': None}
            },

            {
                "BTN":  {'Name': 'PotNoodle99912', 'Stack': 580611.00, 'Cards': 'As Qs'},
                "SB":  {'Name': 'coog', 'Stack': 125009.00, 'Cards': 'Ad Qc'},
                "BB":  {'Name': 'dartdog', 'Stack': 44380.00, 'Cards': 'Js Ac'},
                "UTG":  {'Name': None, 'Stack': None, 'Cards': None},
                "UTG+1":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP+1":  {'Name': None, 'Stack': None, 'Cards': None},
                'MP+2':  {'Name': None, 'Stack': None, 'Cards': None},
                "CO":  {'Name': None, 'Stack': None, 'Cards': None}
            },

            {
                'BTN':  {'Name': None, 'Stack': None, 'Cards': None},
                "SB":  {'Name': 'coog', 'Stack': 52799.00, 'Cards': 'Js Kh'},
                "BB":  {'Name': 'PotNoodle99912', 'Stack': 697201.00, 'Cards': '7s As'},
                "UTG":  {'Name': None, 'Stack': None, 'Cards': None},
                "UTG+1":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP":  {'Name': None, 'Stack': None, 'Cards': None},
                "MP+1":  {'Name': None, 'Stack': None, 'Cards': None},
                'MP+2':  {'Name': None, 'Stack': None, 'Cards': None},
                "CO":  {'Name': None, 'Stack': None, 'Cards': None}
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
