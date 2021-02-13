
from utils.run_sql_command import run_sql_command
from utils.make_line_plot import make_line_plot


def plot_money_won_lost(sigma, database, all_buyins=False, buyin=None):

    if all_buyins:
        price_and_prize = run_sql_command('SELECT prize, price, Entries FROM tournaments ORDER BY finished_time', database)
    else:
        price_and_prize = run_sql_command('SELECT prize, price, Entries FROM tournaments WHERE price="'+ str(buyin) + '" ORDER BY finished_time', database)

    datapoints = [0]  # we always start at 0

    for price, prize, entries in price_and_prize:
        if entries is None:
            entries = 1
        datapoints.append(
            float(float(datapoints[-1]) + ((price*entries) - prize))
        )

    title = 'All Profit in $ won (all buyins)' if all_buyins else 'All Profit in $ won (buyin:' + str(buyin) + ')'

    make_line_plot(
        list_of_data_points=datapoints,
        xlabel='Game #',
        ylabel='Money ($)',
        title=title,
        add_avg_line=True,
        sigma=sigma
    )