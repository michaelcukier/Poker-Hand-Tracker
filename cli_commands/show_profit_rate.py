import click
from GLOBAL_VARIABLES import DATABASE_LOCATION, FOLDER_PLOT_DUMP
from db_api.plots.profit_rate import profit_rate
import subprocess


@click.command()
@click.argument('buyin', required=False, default=None)
def show_profit_rate(buyin):
    plot_name = profit_rate(
        buyin=buyin,
        save_to=FOLDER_PLOT_DUMP,
        database_file_path=DATABASE_LOCATION
    )
    filepath__ = FOLDER_PLOT_DUMP + plot_name
    subprocess.call(['open', filepath__])
