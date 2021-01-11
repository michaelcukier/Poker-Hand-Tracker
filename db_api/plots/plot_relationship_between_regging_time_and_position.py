

from helpers.run_sql_command import run_sql_command
from helpers.make_scatter_plot import make_scatter_plot
import random
import matplotlib.pyplot as plt
import numpy as np


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


    print('xsxsx', np.average(positions_and_level_dict[1]))
    print('xsxsx', np.average(positions_and_level_dict[2]))
    print('xsxsx', np.average(positions_and_level_dict[3]))
    print('xsxsx', np.average(positions_and_level_dict[4]))
    print('xsxsx', np.average(positions_and_level_dict[5]))

    data = [positions_and_level_dict[1],
            positions_and_level_dict[2],
            positions_and_level_dict[3],
            positions_and_level_dict[4],
            positions_and_level_dict[5],
            positions_and_level_dict[6]]

    plt.figure(figsize=(10, 7))


    # plt.scatter('1', positions_and_level_dict[1], alpha=0.4)

    # Creating axes instance
    # ax = plt.add_axes([0, 0, 1, 1])

    # Creating plot
    plt.boxplot(data, labels=[
        'Level 1, s=' + str(len(positions_and_level_dict[1])),
        'Level 2, s=' + str(len(positions_and_level_dict[2])),
        'Level 3, s=' + str(len(positions_and_level_dict[3])),
        'Level 4, s=' + str(len(positions_and_level_dict[4])),
        'Level 5, s=' + str(len(positions_and_level_dict[5])),
        'Level 6, s=' + str(len(positions_and_level_dict[6]))])

    # show plot
    plt.show()

    # avgDict = {}
    # for lvl, pos in positions_and_level_dict.items():
    #     avgDict[lvl] = sum(pos) / float(len(pos))
    #
    # print(avgDict)

    # plt.bar(range(len(avgDict)), list(avgDict.values()), align='center')
    # plt.xticks(range(len(avgDict)), list(avgDict.keys()))
    # plt.show()
    quit()
    #
    # get_all_ids_and_positions = run_sql_command(
    #     '''
    #     SELECT ID, position
    #     FROM tournaments
    #     ''')
    #
    #
    # first_hand_levels = []
    # positions = []
    # for id, position in get_all_ids_and_positions:
    #     query = '''
    #         SELECT level
    #         FROM hands
    #         WHERE tourney_id={}
    #         ORDER BY time
    #         LIMIT 1
    #         '''.format(id)
    #     if position != 0:  # position level not recorded by poker site, so ignored
    #         first_hand_level = run_sql_command(query, unique_items=True)[0].split(' (')[0]
    #         first_hand_levels.append(first_hand_level)
    #         positions.append(position)

    # sorted_first_hand_levels, sorted_final_position = (list(t) for t in zip(*sorted(zip(first_hand_levels, positions))))

    # for lvl, pos in zip(sorted_first_hand_levels, sorted_final_position):
    #     print('lvl:'+str(lvl), '- pos:'+str(pos))
    #
    # quit()
    # title = 'relationship regging'
    #
    # make_scatter_plot(
    #     x_coordinates=sorted_final_position,
    #     y_coordinates=sorted_first_hand_levels,
    #     x_label='Finished Position',
    #     y_label='Level when joined tournament',
    #     title=title
    # )


plot_relationship_between_regging_time_and_position()