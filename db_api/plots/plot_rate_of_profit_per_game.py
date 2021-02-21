from utils.run_sql_command import run_sql_command
from utils.make_line_plot import make_line_plot


def rate_of_profit_per_game(database_file_path, save_to,  buyin=None):

    query = '''
        SELECT 
            (prize - price)
        AS 
            profit_per_game 
        FROM 
            tournaments 
        WHERE
            {0}
        ORDER BY 
            finished_time
    '''.format(str('price=' + str(buyin) if buyin is not None else '1=1'))

    data = run_sql_command(
        query=query,
        unique_items=True,
        database_file_path=database_file_path
    )

    avg_profits = []
    for i, prize in enumerate(data):
        if i == 0:
            avg_profits.append(prize)
        else:
            avg_profits.append(round(sum(data[:i+1])/(i+1), 2))

    title = 'Profit rate per tournament (across all tournament buyins)' if buyin is None else 'Profit rate per game over time for $' + str(buyin)

    plot_path = make_line_plot(
        save_to_folder=save_to,
        list_of_data_points=avg_profits,
        xlabel='Game',
        ylabel='Profit/game',
        title=title,
        all_xticks=False,
        add_avg_line=True,
        sigma=4
    )

    return plot_path

#
# from GLOBAL_VARIABLES import DATABASE_LOCATION
#
#
# print(rate_of_profit_per_game(
#     save_to="/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/plots_dump/",
#     database_file_path=DATABASE_LOCATION
# ))