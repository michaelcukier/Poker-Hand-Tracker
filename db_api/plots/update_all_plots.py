from db_api.plots.plot_money_won_lost_per_buyin import plot_money_won_lost
from db_api.plots.plot_rate_of_profit_per_game import plot_rate_of_profit_per_game
from db_api.plots.plot_relationship_between_regging_time_and_position import plot_relationship_between_regging_time_and_position


def update_all_plots():
    from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT
    for name, buyin in TOURNAMENTS_TO_EXTRACT.items():
        plot_money_won_lost(buyin=buyin, sigma=7)
        plot_rate_of_profit_per_game(buyin=buyin)
    plot_money_won_lost(sigma=7, all_buyins=True)
    plot_rate_of_profit_per_game(all_buyins=True)
    plot_relationship_between_regging_time_and_position()
