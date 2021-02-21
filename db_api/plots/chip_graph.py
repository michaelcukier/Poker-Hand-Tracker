from utils.run_sql_command import run_sql_command
from utils.make_line_plot import make_line_plot


def chip_graph(tourney_id: int, database_file_path: str, width: int) -> str:
    """
    Returns the chip stack amount (in chips) at the start of every hand played within a tournament

            Parameters:
                    tourney_id (int): the tournament ID
                    database_file_path (str): the path of the database file

            Returns:
                    plot_path (str): path of the plot
    """

    query = '''
        SELECT 
            stack_size, level
        FROM 
            hands 
        WHERE 
            tourney_id={0}
        ORDER BY 
            time
    '''.format(tourney_id)

    data = run_sql_command(
        query=query,
        unique_items=False,
        database_file_path=database_file_path)

    # convert stack size to chips

    data_ = []
    for stack_size_bb, lvl in data:
        # print('xx', lvl, '-', stack_size_bb)
        bb_level = float(lvl.split('/')[1].replace(')', ''))
        data_.append(stack_size_bb * bb_level)

    plot_path = make_line_plot(
        save_to_folder="/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/plots_dump/",
        list_of_data_points=data_,
        xlabel='Hand #',
        ylabel='Chips (in bb)',
        title='Chip graph for Tournament #' + str(tourney_id),
        all_xticks=True,
        custom_width=True,
        width=width
    )

    return plot_path

#
# from GLOBAL_VARIABLES import DATABASE_LOCATION
#
# print(chip_graph(
#     tourney_id=24096797,
#     database_file_path=DATABASE_LOCATION
# ))