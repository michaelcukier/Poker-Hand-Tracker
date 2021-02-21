import click
from GLOBAL_VARIABLES import DATABASE_LOCATION, FOLDER_PLOT_DUMP
from db_api.plots.plot_money_won_lost_per_buyin import plot_money_won_lost
import subprocess


@click.command()
@click.argument('buyin', required=False, default=None)
def show_money_graph(buyin):
    plot_name = plot_money_won_lost(
        sigma=10,
        save_to=FOLDER_PLOT_DUMP,
        database_file_path=DATABASE_LOCATION,
        buyin=buyin)
    filepath__ = FOLDER_PLOT_DUMP + plot_name
    subprocess.call(['open', filepath__])
