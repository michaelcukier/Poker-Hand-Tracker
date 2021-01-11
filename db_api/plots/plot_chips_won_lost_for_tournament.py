

from helpers.run_sql_command import run_sql_command
from helpers.make_line_plot import make_line_plot


def plot_chips_won_lost_for_tournament(tourney_id, width):
    chips = run_sql_command('SELECT stack_size_start_of_hand FROM hands WHERE tourney_id="'+ str(tourney_id) + '" ORDER BY time', unique_items=True)

    make_line_plot(
        list_of_data_points=chips,
        xlabel='Hand #',
        ylabel='Chips (in bb)',
        title='Chips won playing Tournament # (in bb)' + str(tourney_id),
        all_xticks=True,
        custom_width=True,
        width=width
    )
