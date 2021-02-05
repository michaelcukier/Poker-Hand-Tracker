# from src.extract.hands.hands import get_hands_info
# from src.extract.tournament.opponents import extract_opponents_names
# from tournament.create_tournament import extract_new_tournament

# ------

from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER

#
# class TournamentFiles:
#     def __init__(self, tournament_id):
#         self.tournament_id = tournament_id
#         self.hand_history_filenames = []
#         self.tournament_summary_filename = []
#         self.re_entries = 0
#
#     def add_hand_history_filename(self, filename):
#         self.hand_history_filenames.append(filename)
#
#     def add_tournament_summary_filename(self, filename):
#         self.tournament_summary_filename.append(filename)
#
#     def set_re_entries(self, re_entries: int):
#         self.re_entries = re_entries
#
# from extract.tournament.Tournament import Tournament
# # from get_new_filenames.src.TournamentFiles.TournamentFiles import TournamentFiles
#
#
# # mock
# myT = TournamentFiles(23974830)
# myT.add_hand_history_filename("HH20210203 SITGOID-G23974830T1 TN-$0{FULLSTOP}50\xa0Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt")
# myT.add_tournament_summary_filename('TS20210203 T23974830 E216293469 NL Hold’em $0.50 + $0.05.ots')
# all_Ts = []
# all_Ts.append(myT)
#


from extract.tournament.Tournament import Tournament


def process_filenames(tournamentFilenamesList: list, parent_folder: str) -> list:
    processed = []

    for t in tournamentFilenamesList:
        processed_t = Tournament(
            hand_history_filenames=t.hand_history_filenames,
            tournament_summary_filename=t.tournament_summary_filename,
            re_entries=t.re_entries,
            parent_folder=parent_folder
        )
        processed_t.build_tournament()

        # for h in processed_t.hands:
        #     print(t.hand_history_filenames)
        #     print(h.time)
        #     print(h.level)
        #     print(h.my_cards)
        #     print(h.board_cards)
        #     print(h.tourney_id)
        #     print(h.hand_id)
        #     print(h.position)
        #     print(h.starting_stack_size_bb)
        #     print(h.main_pot_winner)
        #     print(h.side_pot_1_winner)
        #     print(h.side_pot_2_winner)
        #     print(h.side_pot_3_winner)
        #     print(h.main_pot_size_bb)
        #     print(h.side_pot_1_size_bb)
        #     print(h.side_pot_2_size_bb)
        #     print(h.side_pot_3_size_bb)
        #     print('-----------------------------------')

        processed.append(processed_t)

    return processed

# process_filenames(all_Ts, parent_folder=HAND_HISTORY_FOLDER)



#
# def run(raw_hh: dict, log_progress=False, early_stop_for_test=False) -> list:
#     extraction = []
#
#
#     idx = 0
#
#
#
#     for tourney_id, hh in raw_hh.items():
#         idx += 1
#
#
#         if log_progress:
#             print("Getting ", tourney_id, " data...", str(idx) + '/' + str(len(raw_hh.items())))
#
#
#         extraction.append({
#             'new_tournament': extract_new_tournament(hh['title'], hh['hands'], hh['summary'], hh['re_entries']),
#             'new_hands': get_hands_info(hh['hands']),
#             'new_opponents': extract_opponents_names(hh['summary'])
#         })
#
#         if early_stop_for_test:
#             if idx == 15:
#                 return extraction
#
#     return extraction