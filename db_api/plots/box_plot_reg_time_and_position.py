from utils.run_sql_command import run_sql_command
from utils.make_box_plot import make_box_plot

import numpy as np


def box_plot_reg_time_and_position(database_file_path: str, save_to: str) -> str:

    query = '''
        SELECT 
            position, level
        FROM
            (SELECT t.ID, t.position, h.time, h.level, row_number() 
                OVER (partition by t.id order by h.time) rank
                    FROM 
                        Tournaments t
                    INNER JOIN 
                        hands h
                    ON 
                        t.id = h.tourney_id
            ) r
        WHERE rank = 1
        '''

    get_some = run_sql_command(
        query=query,
        unique_items=False,
        database_file_path=database_file_path
    )

    positions_and_level_dict = {}
    for pos, lvl, in get_some:
        level = int(str(lvl).split(' (')[0])
        if level not in positions_and_level_dict:
            positions_and_level_dict[level] = []
        if pos == 0:  # position not recorded by the site, so pass it
            pass
        else:
            positions_and_level_dict[level].append(pos)

    data = [positions_and_level_dict[i] for i in range(1, 6)]

    x_axis_labels = []
    for i in range(1, 6):
        txt = 'Level {0} \nSamples={1} \nMean={2}'
        lvl = i
        samples = str(len(positions_and_level_dict[i]))
        mean_ = np.around(np.mean(positions_and_level_dict[i]), 1)
        x_axis_labels.append(
            txt.format(lvl, samples, mean_)
        )

    plot_path = make_box_plot(
        save_to_folder=save_to,
        x_axis_labels=x_axis_labels,
        data=data,
        x_label='Level at the time of registration',
        y_label='Final position',
        title='Relationship between regging level and final position',
    )

    return plot_path


# from GLOBAL_VARIABLES import DATABASE_LOCATION
#
#
# print(box_plot_reg_time_and_position(
#     save_to="/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/plots_dump/",
#     database_file_path=DATABASE_LOCATION
# ))


