import click

from cli_commands.update_db import update_db
from cli_commands.show_money_graph import show_money_graph
from cli_commands.show_reg_time_and_pos import show_reg_time_and_pos
from cli_commands.show_profit_rate import show_profit_rate
from cli_commands.show_chip_graph import show_chip_graph
from cli_commands.show_last_n_tournaments import show_last_n_tournaments
from cli_commands.show_buyin_report import show_report_by_buyin

from prettytable import PrettyTable, ALL


class RichGroup(click.Group):
    def format_help(self, ctx, formatter):
        t = PrettyTable(['Command', 'Type', 'Parameters', 'Description'])
        t.hrules = ALL
        t.add_row(['update-db', 'action', 'None', 'Updates the database with new tournaments'])
        t.add_row(['', '', '', ''])
        t.add_row(['show-money-graph', 'plot', 'optional: buyin (float)', 'Shows a line plot of the money graph'])
        t.add_row(['show-reg-time-and-pos', 'plot', 'None', 'Shows a box plot representing the relationship \n between registration time and final position'])
        t.add_row(['show-profit-rate', 'plot', 'optional: buyin (float)', 'Shows the the avg profit/tournament over time'])
        t.add_row(['show-chip-graph', 'plot', 'required: tournament ID (int)', 'Shows the chip graph for a tournament'])
        t.add_row(['', '', '', ''])
        t.add_row(['show-last-n-tournaments', 'table', 'required: n (int)', 'Shows the last n tournaments'])
        t.add_row(['show-report-by-buyin', 'table', 'None', 'Shows statistics about each buy-in'])
        print(t)


@click.group(cls=RichGroup)
def main():
    click.clear()
    pass


main.add_command(update_db)
main.add_command(show_money_graph)
main.add_command(show_reg_time_and_pos)
main.add_command(show_profit_rate)
main.add_command(show_chip_graph)
main.add_command(show_last_n_tournaments)
main.add_command(show_report_by_buyin)


if __name__ == '__main__':
    main()

