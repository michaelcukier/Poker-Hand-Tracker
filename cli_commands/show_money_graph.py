import click
from GLOBAL_VARIABLES import DATABASE_LOCATION, FOLDER_PLOT_DUMP
from db_api.plots.money_graph import money_graph
import subprocess


@click.command()
@click.argument('buyin', required=False, default=None)
def show_money_graph(buyin):
    plot_name = money_graph(
        sigma=10,
        database_file_path=DATABASE_LOCATION,
        buyin=buyin)
    filepath__ = FOLDER_PLOT_DUMP + plot_name
    subprocess.call(['open', filepath__])
