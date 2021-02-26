import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.position_info.assign_position_to_name_and_stack import assign_position_to_name_and_stack


class test(unittest.TestCase):
    def test_assign_position_to_name_and_stack(self):

        input_seats_list_wth_btn_first = [
            ['Seat 2: joeyv will be allowed to play after the button', 'Seat 3: first shirt will be allowed to play after the button', 'Seat 4: FishKabob (27300.00)', 'Seat 5: bootlegger11 (82150.00)', 'Seat 6: MemphisGrind (80315.00)', 'Seat 7: Dcin2020 (17200.00)', 'Seat 8: luckiedar (93900.00)', 'Seat 9: PotNoodle99912 (46475.00)', 'Seat 1: Zees40660 (209570.00)'],
            ['Seat 4: FishKabob (24900.00)', 'Seat 5: bootlegger11 (77750.00)', 'Seat 6: MemphisGrind (79915.00)', 'Seat 7: Dcin2020 (16800.00) is sitting out', 'Seat 8: luckiedar (85500.00)', 'Seat 9: PotNoodle99912 (46075.00)', 'Seat 1: Zees40660 (225970.00)', 'Seat 2: joeyv (42403.00)', 'Seat 3: first shirt (90495.00)'],
            ['Seat 5: bootlegger11 (75350.00)', 'Seat 6: MemphisGrind (55015.00)', 'Seat 7: Dcin2020 (16400.00)', 'Seat 8: luckiedar (85100.00)', 'Seat 9: PotNoodle99912 (45675.00)', 'Seat 1: Zees40660 (225570.00)', 'Seat 2: joeyv (42003.00)', 'Seat 3: first shirt (90095.00)', 'Seat 4: FishKabob (54600.00)'],
            ['Seat 6: MemphisGrind (415.00)', 'Seat 7: Dcin2020 (12000.00)', 'Seat 8: luckiedar (84700.00)', 'Seat 9: PotNoodle99912 (45275.00)', 'Seat 1: Zees40660 (225170.00)', 'Seat 2: joeyv (41603.00)', 'Seat 3: first shirt (89695.00)', 'Seat 4: FishKabob (116000.00)', 'Seat 5: bootlegger11 (74950.00)'],
            ['Seat 7: Dcin2020 (9600.00) is sitting out', 'Seat 8: luckiedar (89900.00)', 'Seat 9: PotNoodle99912 (44875.00)', 'Seat 1: Zees40660 (224770.00)', 'Seat 2: joeyv (41203.00)', 'Seat 3: first shirt (89295.00)', 'Seat 4: FishKabob (115600.00)', 'Seat 5: bootlegger11 (74550.00)', 'Seat 6: MemphisGrind (15.00)'],
            ['Seat 8: luckiedar (87500.00)', 'Seat 9: PotNoodle99912 (62298.00)', 'Seat 1: Zees40660 (211762.00)', 'Seat 2: joeyv (40803.00)', 'Seat 3: first shirt (88895.00)', 'Seat 4: FishKabob (115200.00)', 'Seat 5: bootlegger11 (74150.00)', 'Seat 7: Dcin2020 (9200.00)'],
            ['Seat 9: PotNoodle99912 (75798.00)', 'Seat 1: Zees40660 (206262.00)', 'Seat 2: joeyv (40303.00)', 'Seat 3: first shirt (88395.00)', 'Seat 4: FishKabob (114700.00)', 'Seat 5: bootlegger11 (73650.00)', 'Seat 7: Dcin2020 (3700.00) is sitting out', 'Seat 8: luckiedar (87000.00)'],
            ['Seat 1: Zees40660 (203262.00)', 'Seat 2: joeyv (34803.00)', 'Seat 3: first shirt (72895.00)', 'Seat 4: FishKabob (114200.00)', 'Seat 5: bootlegger11 (73150.00)', 'Seat 7: Dcin2020 (3200.00)', 'Seat 8: luckiedar (113000.00)', 'Seat 9: PotNoodle99912 (75298.00)'],
            ['Seat 2: joeyv (31803.00)', 'Seat 3: first shirt (67395.00)', 'Seat 4: FishKabob (113700.00)', 'Seat 5: bootlegger11 (72650.00)', 'Seat 7: Dcin2020 (2700.00)', 'Seat 8: luckiedar (112500.00)', 'Seat 9: PotNoodle99912 (74798.00)', 'Seat 1: Zees40660 (214262.00)'],
            ['Seat 3: first shirt (64395.00)', 'Seat 4: FishKabob (108200.00)', 'Seat 5: bootlegger11 (72150.00)', 'Seat 7: Dcin2020 (2200.00)', 'Seat 8: luckiedar (112000.00)', 'Seat 9: PotNoodle99912 (74298.00)', 'Seat 1: Zees40660 (182459.00)', 'Seat 2: joeyv (74106.00)'],
            ['Seat 4: FishKabob (104600.00)', 'Seat 5: bootlegger11 (65550.00)', 'Seat 8: luckiedar (111400.00)', 'Seat 9: PotNoodle99912 (73698.00)', 'Seat 1: Zees40660 (197259.00)', 'Seat 2: joeyv (73506.00)', 'Seat 3: first shirt (63795.00)'],
            ['Seat 5: bootlegger11 (61950.00)', 'Seat 8: luckiedar (104800.00)', 'Seat 9: PotNoodle99912 (73098.00)', 'Seat 1: Zees40660 (196659.00)', 'Seat 2: joeyv (86106.00)', 'Seat 3: first shirt (63195.00)', 'Seat 4: FishKabob (104000.00)'],
            ['Seat 8: luckiedar (101200.00)', 'Seat 9: PotNoodle99912 (152196.00)', 'Seat 1: Zees40660 (123561.00)', 'Seat 2: joeyv (85506.00)', 'Seat 3: first shirt (62595.00)', 'Seat 4: FishKabob (103400.00)', 'Seat 5: bootlegger11 (61350.00)'],
            ['Seat 9: PotNoodle99912 (148596.00)', 'Seat 1: Zees40660 (116961.00)', 'Seat 2: joeyv (84906.00)', 'Seat 3: first shirt (61995.00)', 'Seat 4: FishKabob (116000.00)', 'Seat 5: bootlegger11 (60750.00)', 'Seat 8: luckiedar (100600.00)'],
            ['Seat 1: Zees40660 (138561.00)', 'Seat 2: joeyv (66306.00)', 'Seat 3: first shirt (61395.00)', 'Seat 4: FishKabob (115400.00)', 'Seat 5: bootlegger11 (60150.00)', 'Seat 8: luckiedar (100000.00)', 'Seat 9: PotNoodle99912 (147996.00)']
        ]

        input_nb_of_players = [
            9,
            9,
            9,
            9,
            9,
            8,
            8,
            8,
            8,
            8,
            7,
            7,
            7,
            7,
            7
        ]

        expected_output = [
            {'BTN': {'Name': None, 'Stack': None, 'Cards': None}, 'SB': {'Name': None, 'Stack': None, 'Cards': None}, 'BB': {'Name': 'FishKabob', 'Stack': 27300.0, 'Cards': None}, 'UTG': {'Name': 'bootlegger11', 'Stack': 82150.0, 'Cards': None}, 'UTG+1': {'Name': 'MemphisGrind', 'Stack': 80315.0, 'Cards': None}, 'MP': {'Name': 'Dcin2020', 'Stack': 17200.0, 'Cards': None}, 'MP+1': {'Name': 'luckiedar', 'Stack': 93900.0, 'Cards': None},
             'MP+2': {'Name': 'PotNoodle99912', 'Stack': 46475.0, 'Cards': None}, 'CO': {'Name': 'Zees40660', 'Stack': 209570.0, 'Cards': None}},
            {'BTN': {'Name': 'FishKabob', 'Stack': 24900.0, 'Cards': None}, 'SB': {'Name': 'bootlegger11', 'Stack': 77750.0, 'Cards': None}, 'BB': {'Name': 'MemphisGrind', 'Stack': 79915.0, 'Cards': None}, 'UTG': {'Name': 'Dcin2020', 'Stack': 16800.0, 'Cards': None}, 'UTG+1': {'Name': 'luckiedar', 'Stack': 85500.0, 'Cards': None}, 'MP': {'Name': 'PotNoodle99912', 'Stack': 46075.0, 'Cards': None}, 'MP+1': {'Name': 'Zees40660', 'Stack': 225970.0, 'Cards': None},
             'MP+2': {'Name': 'joeyv', 'Stack': 42403.0, 'Cards': None}, 'CO': {'Name': 'first shirt', 'Stack': 90495.0, 'Cards': None}},
            {'BTN': {'Name': 'bootlegger11', 'Stack': 75350.0, 'Cards': None}, 'SB': {'Name': 'MemphisGrind', 'Stack': 55015.0, 'Cards': None}, 'BB': {'Name': 'Dcin2020', 'Stack': 16400.0, 'Cards': None}, 'UTG': {'Name': 'luckiedar', 'Stack': 85100.0, 'Cards': None}, 'UTG+1': {'Name': 'PotNoodle99912', 'Stack': 45675.0, 'Cards': None}, 'MP': {'Name': 'Zees40660', 'Stack': 225570.0, 'Cards': None}, 'MP+1': {'Name': 'joeyv', 'Stack': 42003.0, 'Cards': None},
             'MP+2': {'Name': 'first shirt', 'Stack': 90095.0, 'Cards': None}, 'CO': {'Name': 'FishKabob', 'Stack': 54600.0, 'Cards': None}},
            {'BTN': {'Name': 'MemphisGrind', 'Stack': 415.0, 'Cards': None}, 'SB': {'Name': 'Dcin2020', 'Stack': 12000.0, 'Cards': None}, 'BB': {'Name': 'luckiedar', 'Stack': 84700.0, 'Cards': None}, 'UTG': {'Name': 'PotNoodle99912', 'Stack': 45275.0, 'Cards': None}, 'UTG+1': {'Name': 'Zees40660', 'Stack': 225170.0, 'Cards': None}, 'MP': {'Name': 'joeyv', 'Stack': 41603.0, 'Cards': None}, 'MP+1': {'Name': 'first shirt', 'Stack': 89695.0, 'Cards': None},
             'MP+2': {'Name': 'FishKabob', 'Stack': 116000.0, 'Cards': None}, 'CO': {'Name': 'bootlegger11', 'Stack': 74950.0, 'Cards': None}},
            {'BTN': {'Name': 'Dcin2020', 'Stack': 9600.0, 'Cards': None}, 'SB': {'Name': 'luckiedar', 'Stack': 89900.0, 'Cards': None}, 'BB': {'Name': 'PotNoodle99912', 'Stack': 44875.0, 'Cards': None}, 'UTG': {'Name': 'Zees40660', 'Stack': 224770.0, 'Cards': None}, 'UTG+1': {'Name': 'joeyv', 'Stack': 41203.0, 'Cards': None}, 'MP': {'Name': 'first shirt', 'Stack': 89295.0, 'Cards': None}, 'MP+1': {'Name': 'FishKabob', 'Stack': 115600.0, 'Cards': None},
             'MP+2': {'Name': 'bootlegger11', 'Stack': 74550.0, 'Cards': None}, 'CO': {'Name': 'MemphisGrind', 'Stack': 15.0, 'Cards': None}},
            {'BTN': {'Name': 'luckiedar', 'Stack': 87500.0, 'Cards': None}, 'SB': {'Name': 'PotNoodle99912', 'Stack': 62298.0, 'Cards': None}, 'BB': {'Name': 'Zees40660', 'Stack': 211762.0, 'Cards': None}, 'UTG': {'Name': 'joeyv', 'Stack': 40803.0, 'Cards': None}, 'UTG+1': {'Name': 'first shirt', 'Stack': 88895.0, 'Cards': None}, 'MP': {'Name': 'FishKabob', 'Stack': 115200.0, 'Cards': None}, 'MP+1': {'Name': 'bootlegger11', 'Stack': 74150.0, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'Dcin2020', 'Stack': 9200.0, 'Cards': None}},
            {'BTN': {'Name': 'PotNoodle99912', 'Stack': 75798.0, 'Cards': None}, 'SB': {'Name': 'Zees40660', 'Stack': 206262.0, 'Cards': None}, 'BB': {'Name': 'joeyv', 'Stack': 40303.0, 'Cards': None}, 'UTG': {'Name': 'first shirt', 'Stack': 88395.0, 'Cards': None}, 'UTG+1': {'Name': 'FishKabob', 'Stack': 114700.0, 'Cards': None}, 'MP': {'Name': 'bootlegger11', 'Stack': 73650.0, 'Cards': None}, 'MP+1': {'Name': 'Dcin2020', 'Stack': 3700.0, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'luckiedar', 'Stack': 87000.0, 'Cards': None}},
            {'BTN': {'Name': 'Zees40660', 'Stack': 203262.0, 'Cards': None}, 'SB': {'Name': 'joeyv', 'Stack': 34803.0, 'Cards': None}, 'BB': {'Name': 'first shirt', 'Stack': 72895.0, 'Cards': None}, 'UTG': {'Name': 'FishKabob', 'Stack': 114200.0, 'Cards': None}, 'UTG+1': {'Name': 'bootlegger11', 'Stack': 73150.0, 'Cards': None}, 'MP': {'Name': 'Dcin2020', 'Stack': 3200.0, 'Cards': None}, 'MP+1': {'Name': 'luckiedar', 'Stack': 113000.0, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'PotNoodle99912', 'Stack': 75298.0, 'Cards': None}},
            {'BTN': {'Name': 'joeyv', 'Stack': 31803.0, 'Cards': None}, 'SB': {'Name': 'first shirt', 'Stack': 67395.0, 'Cards': None}, 'BB': {'Name': 'FishKabob', 'Stack': 113700.0, 'Cards': None}, 'UTG': {'Name': 'bootlegger11', 'Stack': 72650.0, 'Cards': None}, 'UTG+1': {'Name': 'Dcin2020', 'Stack': 2700.0, 'Cards': None}, 'MP': {'Name': 'luckiedar', 'Stack': 112500.0, 'Cards': None}, 'MP+1': {'Name': 'PotNoodle99912', 'Stack': 74798.0, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'Zees40660', 'Stack': 214262.0, 'Cards': None}},
            {'BTN': {'Name': 'first shirt', 'Stack': 64395.0, 'Cards': None}, 'SB': {'Name': 'FishKabob', 'Stack': 108200.0, 'Cards': None}, 'BB': {'Name': 'bootlegger11', 'Stack': 72150.0, 'Cards': None}, 'UTG': {'Name': 'Dcin2020', 'Stack': 2200.0, 'Cards': None}, 'UTG+1': {'Name': 'luckiedar', 'Stack': 112000.0, 'Cards': None}, 'MP': {'Name': 'PotNoodle99912', 'Stack': 74298.0, 'Cards': None}, 'MP+1': {'Name': 'Zees40660', 'Stack': 182459.0, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'joeyv', 'Stack': 74106.0, 'Cards': None}},
            {'BTN': {'Name': 'FishKabob', 'Stack': 104600.0, 'Cards': None}, 'SB': {'Name': 'bootlegger11', 'Stack': 65550.0, 'Cards': None}, 'BB': {'Name': 'luckiedar', 'Stack': 111400.0, 'Cards': None}, 'UTG': {'Name': 'PotNoodle99912', 'Stack': 73698.0, 'Cards': None}, 'UTG+1': {'Name': 'Zees40660', 'Stack': 197259.0, 'Cards': None}, 'MP': {'Name': 'joeyv', 'Stack': 73506.0, 'Cards': None}, 'MP+1': {'Name': None, 'Stack': None, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'first shirt', 'Stack': 63795.0, 'Cards': None}},
            {'BTN': {'Name': 'bootlegger11', 'Stack': 61950.0, 'Cards': None}, 'SB': {'Name': 'luckiedar', 'Stack': 104800.0, 'Cards': None}, 'BB': {'Name': 'PotNoodle99912', 'Stack': 73098.0, 'Cards': None}, 'UTG': {'Name': 'Zees40660', 'Stack': 196659.0, 'Cards': None}, 'UTG+1': {'Name': 'joeyv', 'Stack': 86106.0, 'Cards': None}, 'MP': {'Name': 'first shirt', 'Stack': 63195.0, 'Cards': None}, 'MP+1': {'Name': None, 'Stack': None, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'FishKabob', 'Stack': 104000.0, 'Cards': None}},
            {'BTN': {'Name': 'luckiedar', 'Stack': 101200.0, 'Cards': None}, 'SB': {'Name': 'PotNoodle99912', 'Stack': 152196.0, 'Cards': None}, 'BB': {'Name': 'Zees40660', 'Stack': 123561.0, 'Cards': None}, 'UTG': {'Name': 'joeyv', 'Stack': 85506.0, 'Cards': None}, 'UTG+1': {'Name': 'first shirt', 'Stack': 62595.0, 'Cards': None}, 'MP': {'Name': 'FishKabob', 'Stack': 103400.0, 'Cards': None}, 'MP+1': {'Name': None, 'Stack': None, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'bootlegger11', 'Stack': 61350.0, 'Cards': None}},
            {'BTN': {'Name': 'PotNoodle99912', 'Stack': 148596.0, 'Cards': None}, 'SB': {'Name': 'Zees40660', 'Stack': 116961.0, 'Cards': None}, 'BB': {'Name': 'joeyv', 'Stack': 84906.0, 'Cards': None}, 'UTG': {'Name': 'first shirt', 'Stack': 61995.0, 'Cards': None}, 'UTG+1': {'Name': 'FishKabob', 'Stack': 116000.0, 'Cards': None}, 'MP': {'Name': 'bootlegger11', 'Stack': 60750.0, 'Cards': None}, 'MP+1': {'Name': None, 'Stack': None, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'luckiedar', 'Stack': 100600.0, 'Cards': None}},
            {'BTN': {'Name': 'Zees40660', 'Stack': 138561.0, 'Cards': None}, 'SB': {'Name': 'joeyv', 'Stack': 66306.0, 'Cards': None}, 'BB': {'Name': 'first shirt', 'Stack': 61395.0, 'Cards': None}, 'UTG': {'Name': 'FishKabob', 'Stack': 115400.0, 'Cards': None}, 'UTG+1': {'Name': 'bootlegger11', 'Stack': 60150.0, 'Cards': None}, 'MP': {'Name': 'luckiedar', 'Stack': 100000.0, 'Cards': None}, 'MP+1': {'Name': None, 'Stack': None, 'Cards': None},
             'MP+2': {'Name': None, 'Stack': None, 'Cards': None}, 'CO': {'Name': 'PotNoodle99912', 'Stack': 147996.0, 'Cards': None}}
        ]

        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[0], nb_of_players=input_nb_of_players[0]), expected_output[0])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[1], nb_of_players=input_nb_of_players[1]), expected_output[1])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[2], nb_of_players=input_nb_of_players[2]), expected_output[2])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[3], nb_of_players=input_nb_of_players[3]), expected_output[3])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[4], nb_of_players=input_nb_of_players[4]), expected_output[4])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[5], nb_of_players=input_nb_of_players[5]), expected_output[5])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[6], nb_of_players=input_nb_of_players[6]), expected_output[6])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[7], nb_of_players=input_nb_of_players[7]), expected_output[7])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[8], nb_of_players=input_nb_of_players[8]), expected_output[8])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[9], nb_of_players=input_nb_of_players[9]), expected_output[9])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[10], nb_of_players=input_nb_of_players[10]), expected_output[10])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[11], nb_of_players=input_nb_of_players[11]), expected_output[11])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[12], nb_of_players=input_nb_of_players[12]), expected_output[12])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[13], nb_of_players=input_nb_of_players[13]), expected_output[13])
        self.assertEqual(assign_position_to_name_and_stack(seats=input_seats_list_wth_btn_first[14], nb_of_players=input_nb_of_players[14]), expected_output[14])
