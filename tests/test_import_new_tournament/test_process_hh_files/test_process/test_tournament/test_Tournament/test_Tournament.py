
import unittest
from import_new_tournaments.process_hh_files.process.tournament.Tournament.Tournament import Tournament
from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER, FAKE_TOURNAMENT_SUMMARY_FOLDER


class test(unittest.TestCase):
    def test_Tournament(self):

        t = Tournament(
            hand_history_filenames=["HH20201217 SITGOID-G23140753T4 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"],
            tournament_summary_filename="TS20201217 T23140753 E197540971 NL Hold’em $0.50 + $0.05.ots",
            re_entries=1,
            parent_folder_hand_history=FAKE_HAND_HISTORY_FOLDER,
            parent_folder_tournament_summary=FAKE_TOURNAMENT_SUMMARY_FOLDER)

        t.build_tournament()

        self.assertEqual(t.elapsed_time, 1)
        self.assertEqual(t.finish_time, '2020/12/17 22:17:10 UTC')
        self.assertEqual(t.id, 23140753)
        self.assertEqual(t.nb_of_participants, 20)
        self.assertEqual(t.opponents,
                         [
                             'twomil',
                             'rldes',
                             'sanctuary',
                             'KINGGS',
                             'Jhop55',
                             'Mojibest',
                             'Henry1953',
                             'Burn Card',
                             'bacchus5555',
                             'WBRoy',
                             'OffMyMedz',
                             'Naruba80',
                             'Reno-Randy',
                             'slambamhappy',
                             'royal abe',
                             'AlpacaGuy',
                             'JaumduCaminhao',
                             'masterluke0829'])
        self.assertEqual(t.position, 12)
        self.assertEqual(t.price, 0.55)
        self.assertEqual(t.prize, 0)

