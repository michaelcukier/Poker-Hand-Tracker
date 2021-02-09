

from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER, TOURNEY_SUMMARY_FOLDER, DATABASE_LOCATION

# 1- get the new filenames
from import_new_tournament.get_new_hh_files.get_new_filenames import get_new_filenames
new_tourneys_filenames = get_new_filenames(
    HAND_HISTORY_FOLDER,
    TOURNEY_SUMMARY_FOLDER,
    DATABASE_LOCATION)


# 2- process the filenames
from process_filenames import process_filenames
processed_tournaments = process_filenames(
    new_tourneys_filenames,
    parent_folder_hand_history=HAND_HISTORY_FOLDER,
    parent_folder_tournament_summary=TOURNEY_SUMMARY_FOLDER)


print(len(processed_tournaments))

#
# # 2- process
# tournaments = []
# for tourney_filename in new_tourneys_filenames:
#
#     t = Tournament(filename=tourney_filename)
#
#     t.get_other_filenames()
#
#     t.get_hands()  # t.hands = [Hands(), Hands(), ... ]
#     t.get_re_entries()
#     t.get_buyin()
#     t.get_finish_time()
#     t.get_prize()
#     t.get_tourney_id()
#     t.get_position()
#     t.get_nb_of_participants()
#     t.get_elapsed_time()
#     t.get_opponents()
#
#     tournaments.append(t)
#
# # 3- save
# for t in tournaments:
#     save_tourney_to_db(t)
#
#



# # ---- 1. Update the db with new data, if there's any
# from test_hh_import.run import wrapper_import_new as run
# run()
#
# #
# # ---- 2. Play with the API
# from update_all_plots import update_all_plots
# update_all_plots()


# from test_db_api.plots.plot_relationship_between_regging_time_and_position import plot_relationship_between_regging_time_and_position

#
# from test_db_api.plots.plot_chips_won_lost_for_tournament import plot_chips_won_lost_for_tournament
# # plot_chips_won_lost_for_tournament(23115737, width=50)
#
