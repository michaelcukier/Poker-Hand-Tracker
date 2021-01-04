

# ---- 1. Update the db with new data, if there's any
# from hh_import.run import wrapper_import_new as run
# run()


# ---- 2. Play with the API
from db_api.plots.plot_money_won_lost_per_buyin import plot_money_won_lost
from db_api.plots.plot_rate_of_profit_per_game import plot_rate_of_profit_per_game

def update_graphs():
    from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT
    for name, buyin in TOURNAMENTS_TO_EXTRACT.items():
        plot_money_won_lost(buyin=buyin, sigma=7)
        plot_rate_of_profit_per_game(buyin=buyin)
    plot_money_won_lost(sigma=7, all_buyins=True)
    plot_rate_of_profit_per_game(all_buyins=True)

update_graphs()

from db_api.plots.plot_chips_won_lost_for_tournament import plot_chips_won_lost_for_tournament
# plot_chips_won_lost_for_tournament(23115737, width=50)

