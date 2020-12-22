from helpers.run_sql_command import run_sql_command


def run(clean_data):
    for new_tourney in clean_data:
        run_sql_command(
            "INSERT INTO "
            "tournaments (ID, finished_time, price, prize, position, elapsed_time) "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            new_tourney['new_tournament']['id'],
            new_tourney['new_tournament']['finished_time'],
            new_tourney['new_tournament']['price'],
            new_tourney['new_tournament']['prize'],
            new_tourney['new_tournament']['position'],
            new_tourney['new_tournament']['elapsed_time'])
        )
