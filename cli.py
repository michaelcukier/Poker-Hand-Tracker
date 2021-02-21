
import click

from cli_commands.update_db import update_db
from cli_commands.show_money_graph import show_money_graph


@click.group()
def main():
    pass


main.add_command(update_db)
main.add_command(show_money_graph)

if __name__ == '__main__':
    main()
