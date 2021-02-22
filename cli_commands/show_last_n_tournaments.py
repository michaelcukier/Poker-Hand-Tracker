import click
from GLOBAL_VARIABLES import DATABASE_LOCATION
from db_api.tables.last_n_tournaments import last_n_tournaments


@click.command(short_help='[table] Displays the last played tournaments')
@click.argument('n', required=True)
def show_last_n_tournaments(n):
    print(last_n_tournaments(n, DATABASE_LOCATION))
