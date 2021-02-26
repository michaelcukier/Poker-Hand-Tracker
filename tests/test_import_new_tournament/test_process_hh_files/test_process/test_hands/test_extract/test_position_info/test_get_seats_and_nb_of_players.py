import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.position_info.get_seats_and_nb_of_players import get_seats_and_nb_of_players
from .fake_data import hands


class test(unittest.TestCase):
    def test_get_seats_and_nb_of_players(self):

        expected = [
            {'lst': ['Seat 1: Zees40660 (209570.00)', 'Seat 2: joeyv will be allowed to play after the button', 'Seat 3: first shirt will be allowed to play after the button', 'Seat 4: FishKabob (27300.00)', 'Seat 5: bootlegger11 (82150.00)', 'Seat 6: MemphisGrind (80315.00)', 'Seat 7: Dcin2020 (17200.00)', 'Seat 8: luckiedar (93900.00)', 'Seat 9: PotNoodle99912 (46475.00)'], 'nb_of_players': 9},
            {'lst': ['Seat 1: Zees40660 (225970.00)', 'Seat 2: joeyv (42403.00)', 'Seat 3: first shirt (90495.00)', 'Seat 4: FishKabob (24900.00)', 'Seat 5: bootlegger11 (77750.00)', 'Seat 6: MemphisGrind (79915.00)', 'Seat 7: Dcin2020 (16800.00) is sitting out', 'Seat 8: luckiedar (85500.00)', 'Seat 9: PotNoodle99912 (46075.00)'], 'nb_of_players': 9},
            {'lst': ['Seat 1: Zees40660 (225570.00)', 'Seat 2: joeyv (42003.00)', 'Seat 3: first shirt (90095.00)', 'Seat 4: FishKabob (54600.00)', 'Seat 5: bootlegger11 (75350.00)', 'Seat 6: MemphisGrind (55015.00)', 'Seat 7: Dcin2020 (16400.00)', 'Seat 8: luckiedar (85100.00)', 'Seat 9: PotNoodle99912 (45675.00)'], 'nb_of_players': 9},
            {'lst': ['Seat 1: Zees40660 (225170.00)', 'Seat 2: joeyv (41603.00)', 'Seat 3: first shirt (89695.00)', 'Seat 4: FishKabob (116000.00)', 'Seat 5: bootlegger11 (74950.00)', 'Seat 6: MemphisGrind (415.00)', 'Seat 7: Dcin2020 (12000.00)', 'Seat 8: luckiedar (84700.00)', 'Seat 9: PotNoodle99912 (45275.00)'], 'nb_of_players': 9},
            {'lst': ['Seat 1: Zees40660 (224770.00)', 'Seat 2: joeyv (41203.00)', 'Seat 3: first shirt (89295.00)', 'Seat 4: FishKabob (115600.00)', 'Seat 5: bootlegger11 (74550.00)', 'Seat 6: MemphisGrind (15.00)', 'Seat 7: Dcin2020 (9600.00) is sitting out', 'Seat 8: luckiedar (89900.00)', 'Seat 9: PotNoodle99912 (44875.00)'], 'nb_of_players': 9},
            {'lst': ['Seat 1: Zees40660 (211762.00)', 'Seat 2: joeyv (40803.00)', 'Seat 3: first shirt (88895.00)', 'Seat 4: FishKabob (115200.00)', 'Seat 5: bootlegger11 (74150.00)', 'Seat 7: Dcin2020 (9200.00)', 'Seat 8: luckiedar (87500.00)', 'Seat 9: PotNoodle99912 (62298.00)'], 'nb_of_players': 8},
            {'lst': ['Seat 1: Zees40660 (206262.00)', 'Seat 2: joeyv (40303.00)', 'Seat 3: first shirt (88395.00)', 'Seat 4: FishKabob (114700.00)', 'Seat 5: bootlegger11 (73650.00)', 'Seat 7: Dcin2020 (3700.00) is sitting out', 'Seat 8: luckiedar (87000.00)', 'Seat 9: PotNoodle99912 (75798.00)'], 'nb_of_players': 8},
            {'lst': ['Seat 1: Zees40660 (203262.00)', 'Seat 2: joeyv (34803.00)', 'Seat 3: first shirt (72895.00)', 'Seat 4: FishKabob (114200.00)', 'Seat 5: bootlegger11 (73150.00)', 'Seat 7: Dcin2020 (3200.00)', 'Seat 8: luckiedar (113000.00)', 'Seat 9: PotNoodle99912 (75298.00)'], 'nb_of_players': 8},
            {'lst': ['Seat 1: Zees40660 (214262.00)', 'Seat 2: joeyv (31803.00)', 'Seat 3: first shirt (67395.00)', 'Seat 4: FishKabob (113700.00)', 'Seat 5: bootlegger11 (72650.00)', 'Seat 7: Dcin2020 (2700.00)', 'Seat 8: luckiedar (112500.00)', 'Seat 9: PotNoodle99912 (74798.00)'], 'nb_of_players': 8},
            {'lst': ['Seat 1: Zees40660 (182459.00)', 'Seat 2: joeyv (74106.00)', 'Seat 3: first shirt (64395.00)', 'Seat 4: FishKabob (108200.00)', 'Seat 5: bootlegger11 (72150.00)', 'Seat 7: Dcin2020 (2200.00)', 'Seat 8: luckiedar (112000.00)', 'Seat 9: PotNoodle99912 (74298.00)'], 'nb_of_players': 8},
            {'lst': ['Seat 1: Zees40660 (197259.00)', 'Seat 2: joeyv (73506.00)', 'Seat 3: first shirt (63795.00)', 'Seat 4: FishKabob (104600.00)', 'Seat 5: bootlegger11 (65550.00)', 'Seat 8: luckiedar (111400.00)', 'Seat 9: PotNoodle99912 (73698.00)'], 'nb_of_players': 7},
            {'lst': ['Seat 1: Zees40660 (196659.00)', 'Seat 2: joeyv (86106.00)', 'Seat 3: first shirt (63195.00)', 'Seat 4: FishKabob (104000.00)', 'Seat 5: bootlegger11 (61950.00)', 'Seat 8: luckiedar (104800.00)', 'Seat 9: PotNoodle99912 (73098.00)'], 'nb_of_players': 7},
            {'lst': ['Seat 1: Zees40660 (123561.00)', 'Seat 2: joeyv (85506.00)', 'Seat 3: first shirt (62595.00)', 'Seat 4: FishKabob (103400.00)', 'Seat 5: bootlegger11 (61350.00)', 'Seat 8: luckiedar (101200.00)', 'Seat 9: PotNoodle99912 (152196.00)'], 'nb_of_players': 7},
            {'lst': ['Seat 1: Zees40660 (116961.00)', 'Seat 2: joeyv (84906.00)', 'Seat 3: first shirt (61995.00)', 'Seat 4: FishKabob (116000.00)', 'Seat 5: bootlegger11 (60750.00)', 'Seat 8: luckiedar (100600.00)', 'Seat 9: PotNoodle99912 (148596.00)'], 'nb_of_players': 7},
            {'lst': ['Seat 1: Zees40660 (138561.00)', 'Seat 2: joeyv (66306.00)', 'Seat 3: first shirt (61395.00)', 'Seat 4: FishKabob (115400.00)', 'Seat 5: bootlegger11 (60150.00)', 'Seat 8: luckiedar (100000.00)', 'Seat 9: PotNoodle99912 (147996.00)'], 'nb_of_players': 7},]

        self.assertEqual(get_seats_and_nb_of_players(hands[0]), expected[0])
        self.assertEqual(get_seats_and_nb_of_players(hands[1]), expected[1])
        self.assertEqual(get_seats_and_nb_of_players(hands[2]), expected[2])
        self.assertEqual(get_seats_and_nb_of_players(hands[3]), expected[3])
        self.assertEqual(get_seats_and_nb_of_players(hands[4]), expected[4])
        self.assertEqual(get_seats_and_nb_of_players(hands[5]), expected[5])
        self.assertEqual(get_seats_and_nb_of_players(hands[6]), expected[6])
        self.assertEqual(get_seats_and_nb_of_players(hands[7]), expected[7])
        self.assertEqual(get_seats_and_nb_of_players(hands[8]), expected[8])
        self.assertEqual(get_seats_and_nb_of_players(hands[9]), expected[9])
        self.assertEqual(get_seats_and_nb_of_players(hands[10]), expected[10])
        self.assertEqual(get_seats_and_nb_of_players(hands[11]), expected[11])
        self.assertEqual(get_seats_and_nb_of_players(hands[12]), expected[12])
        self.assertEqual(get_seats_and_nb_of_players(hands[13]), expected[13])
        self.assertEqual(get_seats_and_nb_of_players(hands[14]), expected[14])
