
from helpers.run_sql_command import run_sql_command
from helpers.make_line_plot import make_line_plot


def plot_money_won_lost(sigma, all_buyins=False, buyin=None):

    if all_buyins:
        price_and_prize = run_sql_command('SELECT prize, price FROM tournaments ORDER BY finished_time')
    else:
        price_and_prize = run_sql_command('SELECT prize, price FROM tournaments WHERE price="'+ str(buyin) + '" ORDER BY finished_time')

    datapoints = [0]  # we always start at 0

    for price, prize in price_and_prize:
        datapoints.append(
            float(float(datapoints[-1]) + (price - prize))
        )

    title = 'All Profit in $ won (all tournaments)' if all_buyins else 'All Profit in $ won (buyin:' + str(buyin) + ')'

    make_line_plot(
        list_of_data_points=datapoints,
        xlabel='Game #',
        ylabel='Money ($)',
        title=title,
        add_avg_line=True,
        sigma=sigma
    )