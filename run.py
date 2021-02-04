

from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER

# 1- get the new filenames
from hh_import.get_new_filenames.get_new_filenames import get_new_filenames
new_tourneys_filenames = get_new_filenames(HAND_HISTORY_FOLDER)


for t in new_tourneys_filenames:
    print(t.__dict__)

quit()

#
# # 2- extract
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
