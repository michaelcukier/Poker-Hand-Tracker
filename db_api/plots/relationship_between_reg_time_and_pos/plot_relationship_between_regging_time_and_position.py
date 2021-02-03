
from helpers.run_sql_command import run_sql_command
from helpers.make_box_plot import make_box_plot
import matplotlib.pyplot as plt


def plot_relationship_between_regging_time_and_position():

    get_some = run_sql_command('''
        select position, level
        from
            (Select t.ID, t.position, h.time, h.level, row_number() over (partition by t.id order by h.time) rank
            FROM Tournaments t
            inner join hands h
            on t.id = h.tourney_id
            ) r
        where rank = 1
        ''')

    positions_and_level_dict = {}
    for pos, lvl, in get_some:
        level = int(str(lvl).split(' (')[0])
        if level not in positions_and_level_dict:
            positions_and_level_dict[level] = []
        if pos == 0:  # position not recorded by the site, so pass it

            pass
        else:
            positions_and_level_dict[level].append(pos)

    data = [positions_and_level_dict[1],
            positions_and_level_dict[2],
            positions_and_level_dict[3],
            positions_and_level_dict[4],
            positions_and_level_dict[5]]

    x_axis_labels = [
        'Level 1 \n# sample=' + str(len(positions_and_level_dict[1])),
        'Level 2 \n# sample=' + str(len(positions_and_level_dict[2])),
        'Level 3 \n# sample=' + str(len(positions_and_level_dict[3])),
        'Level 4 \n# sample=' + str(len(positions_and_level_dict[4])),
        'Level 5 \n# sample=' + str(len(positions_and_level_dict[5]))]

    make_box_plot(
        x_axis_labels=x_axis_labels,
        data=data,
        x_label='Level at the time of registration',
        y_label='Final position',
        title='Relationship between regging level and final position',
    )