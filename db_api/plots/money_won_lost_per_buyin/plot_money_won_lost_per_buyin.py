
from helpers.run_sql_command import run_sql_command
from helpers.make_line_plot import make_line_plot


def plot_money_won_lost(sigma, all_buyins=False, buyin=None):

    if all_buyins:
        price_and_prize = run_sql_command('SELECT prize, price, Entries FROM process ORDER BY finished_time')
    else:
        price_and_prize = run_sql_command('SELECT prize, price, Entries FROM process WHERE price="'+ str(buyin) + '" ORDER BY finished_time')

    datapoints = [0]  # we always start at 0

    for price, prize, entries in price_and_prize:
        if entries is None:
            entries = 1
        datapoints.append(
            float(float(datapoints[-1]) + ((price*entries) - prize))
        )

    title = 'All Profit in $ won (all process)' if all_buyins else 'All Profit in $ won (buyin:' + str(buyin) + ')'

    make_line_plot(
        list_of_data_points=datapoints,
        xlabel='Game #',
        ylabel='Money ($)',
        title=title,
        add_avg_line=True,
        sigma=sigma
    )