

from helpers.run_sql_command import run_sql_command
from helpers.make_scatter_plot import make_scatter_plot


def plot_relationship_between_regging_time_and_position():

    get_all_ids_and_positions = run_sql_command(
        '''
        SELECT ID, position
        FROM tournaments
        ''')

    first_hand_levels = []
    positions = []
    for id, position in get_all_ids_and_positions:
        query = '''
            SELECT level
            FROM hands
            WHERE tourney_id={}
            ORDER BY time
            LIMIT 1
            '''.format(id)
        if position != 0:  # position level not recorded by poker site, so ignored
            first_hand_level = run_sql_command(query, unique_items=True)[0].split(' (')[0]
            first_hand_levels.append(first_hand_level)
            positions.append(position)

    sorted_first_hand_levels, sorted_final_position = (list(t) for t in zip(*sorted(zip(first_hand_levels, positions))))
    #
    # for lvl, pos in zip(sorted_first_hand_levels, sorted_final_position):
    #     print('lvl:'+str(lvl), '- pos:'+str(pos))
    #
    # quit()
    title = 'relationship regging'

    make_scatter_plot(
        x_coordinates=sorted_final_position,
        y_coordinates=sorted_first_hand_levels,
        x_label='Finished Position',
        y_label='Level when joined tournament',
        title=title
    )


plot_relationship_between_regging_time_and_position()