
import click

from cli_commands.update_db import update_db
from cli_commands.show_money_graph import show_money_graph
from cli_commands.show_reg_time_and_pos import show_reg_time_and_pos
from cli_commands.show_profit_rate import show_profit_rate
from cli_commands.show_chip_graph import show_chip_graph
from cli_commands.show_last_n_tournaments import show_last_n_tournaments


@click.group()
def main():
    pass


main.add_command(update_db)
main.add_command(show_money_graph)
main.add_command(show_reg_time_and_pos)
main.add_command(show_profit_rate)
main.add_command(show_chip_graph)
main.add_command(show_last_n_tournaments)


if __name__ == '__main__':
    main()
