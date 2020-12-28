

# ---- 1. Update the db with new data, if there's any
# from hh_import.run import wrapper_import_new as run
# run()


# ---- 2. Play with the API
# from db_api.plots.plot_money_won_lost_per_buyin import plot_money_won_lost_per_buyin
#
# plot_money_won_lost_per_buyin(buyin=0.55, sigma=3)

from db_api.plots.plot_chips_won_lost_for_tournament import plot_chips_won_lost_for_tournament
plot_chips_won_lost_for_tournament(23191111)
