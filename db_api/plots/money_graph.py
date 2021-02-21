from utils.run_sql_command import run_sql_command
from utils.make_line_plot import make_line_plot


def money_graph(sigma, database_file_path, save_to, buyin=None):

    query = '''
        SELECT 
            prize, price, Entries 
        FROM 
            tournaments 
        WHERE
            {0}
        ORDER BY 
            finished_time
    '''.format(str('price=' + str(buyin) if buyin is not None else '1=1'))

    data = run_sql_command(
        query=query,
        unique_items=False,
        database_file_path=database_file_path
    )

    datapoints = [0]  # we always start at 0

    for price, prize, entries in data:
        if entries is None:
            entries = 1
        datapoints.append(
            float(float(datapoints[-1]) + ((price*entries) - prize))
        )

    title = 'All Profit in $ won (all buyins)' if buyin is None else 'All Profit in $ won (buyin:' + str(buyin) + ')'

    plot_path = make_line_plot(
        save_to_folder=save_to,
        list_of_data_points=datapoints,
        xlabel='Game #',
        ylabel='Money ($)',
        title=title,
        add_avg_line=True,
        sigma=sigma
    )

    return plot_path


#
# from GLOBAL_VARIABLES import DATABASE_LOCATION
#
#
# print(plot_money_won_lost(
#     sigma=10,
#     save_to="/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/plots_dump/",
#     database_file_path=DATABASE_LOCATION,
#     buyin=3.3
# ))
