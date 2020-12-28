

from helpers.run_sql_command import run_sql_command
from helpers.plot_something import plot_something


def plot_chips_won_lost_for_tournament(tourney_id):
    chips = run_sql_command('SELECT stack_size_start_of_hand FROM hands WHERE tourney_id="'+ str(tourney_id) + '" ORDER BY time', unique_items=True)

    plot_something(
        list_of_data_points=chips,
        xlabel='Hand #',
        ylabel='Chips',
        title='Chips won playing Tournament #' + str(tourney_id),
        all_xticks=True,
        custom_width=True,
        width=30
    )