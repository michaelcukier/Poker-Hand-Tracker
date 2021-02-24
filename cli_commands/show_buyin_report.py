import click
from GLOBAL_VARIABLES import DATABASE_LOCATION
from db_api.tables.buyin_report import buyin_report


@click.command()
def show_report_by_buyin():
    print(buyin_report(DATABASE_LOCATION))
