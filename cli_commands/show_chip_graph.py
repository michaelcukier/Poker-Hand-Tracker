import click
from GLOBAL_VARIABLES import DATABASE_LOCATION, FOLDER_PLOT_DUMP
from db_api.plots.chip_graph import chip_graph
import subprocess


@click.command()
@click.argument('tournament_id', required=True)
@click.argument('width', required=True)
def show_chip_graph(tournament_id, width):
    plot_name = chip_graph(
        width=int(width),
        tourney_id=tournament_id,
        database_file_path=DATABASE_LOCATION
    )
    filepath__ = FOLDER_PLOT_DUMP + plot_name
    subprocess.call(['open', filepath__])
