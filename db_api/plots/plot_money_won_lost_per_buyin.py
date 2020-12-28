
from helpers.run_sql_command import run_sql_command
from helpers.plot_something import plot_something


def plot_money_won_lost_per_buyin(buyin, sigma):
    prizes = run_sql_command('SELECT prize FROM tournaments WHERE price="'+ str(buyin) + '" ORDER BY finished_time', unique_items=True)

    datapoints = [0]  # we always start at 0

    for prize in prizes:
        datapoints.append(
            float(float(datapoints[-1]) + (prize - buyin))
        )

    plot_something(
        list_of_data_points=datapoints,
        xlabel='Game #',
        ylabel='Money ($)',
        title='Cumulative money won playing the $' + str(buyin),
        add_avg_line=True,
        sigma=sigma
    )