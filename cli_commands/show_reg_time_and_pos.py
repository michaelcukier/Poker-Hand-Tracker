import click
from GLOBAL_VARIABLES import DATABASE_LOCATION, FOLDER_PLOT_DUMP
from db_api.plots.box_plot_reg_time_and_position import box_plot_reg_time_and_position
import subprocess


@click.command(short_help='Shows a box plot representing the relationship between registration time and final position')
def show_reg_time_and_pos():
    plot_name = box_plot_reg_time_and_position(
        save_to=FOLDER_PLOT_DUMP,
        database_file_path=DATABASE_LOCATION
        )
    filepath__ = FOLDER_PLOT_DUMP + plot_name
    subprocess.call(['open', filepath__])
