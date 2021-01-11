
from helpers.run_sql_command import run_sql_command
from helpers.make_line_plot import make_line_plot


def plot_rate_of_profit_per_game(buyin=None, all_buyins=False):

    if all_buyins:
        profits_per_game = run_sql_command('SELECT (prize-price) as profit_per_game FROM tournaments ORDER BY finished_time', unique_items=True)
    else:
        profits_per_game = run_sql_command('SELECT (prize-price) as profit_per_game FROM tournaments WHERE price="'+ str(buyin) + '" ORDER BY finished_time', unique_items=True)

    avg_profits = []
    for i, prize in enumerate(profits_per_game):
        if i == 0:
            avg_profits.append(prize)
        else:
            avg_profits.append(round(sum(profits_per_game[:i+1])/(i+1), 2))

    title = 'Profit rate per tournament (across all tournaments buyins)' if all_buyins else 'Profit rate per game over time for $' + str(buyin)

    make_line_plot(
        list_of_data_points=avg_profits,
        xlabel='Game',
        ylabel='Profit/game',
        title=title,
        all_xticks=False,
        add_avg_line=True,
        sigma=4
    )
