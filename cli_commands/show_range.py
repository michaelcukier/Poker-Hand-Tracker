from db_api.plots.player_range import create_config_for_sql_query, \
    get_sql_data, transform_cards, transform_to_frequencies, \
    create_freq_matrix, create_heatmaps
import subprocess
import click
from GLOBAL_VARIABLES import DATABASE_LOCATION


@click.command()
@click.argument('player', required=True)
@click.argument('position', required=True)
def show_range(player, position):
    config = create_config_for_sql_query(position_at_table=position, player_name=player)
    step1 = get_sql_data(config=config, database_file_path=DATABASE_LOCATION)
    step2 = transform_cards(step1)
    step3 = transform_to_frequencies(step2)
    step4 = create_freq_matrix(step3)
    plot_path = create_heatmaps(step4, pos=position, player_name=player, nb_of_samples=len(step1))
    subprocess.call(['open', plot_path])
