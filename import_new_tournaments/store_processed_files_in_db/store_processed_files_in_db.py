from utils.run_sql_command import run_sql_command
from ..process_hh_files.process.tournament.Tournament.Tournament import Tournament


def store_processed_files_in_db(tournament: Tournament, database_file_path: str):

    """
    Stores a Tournament class in the SQL database

            Parameters:
                    tournament (Tournament): a fully-processed tournament
                    database_file_path (str): the path of the database

            Returns:
                    None
    """

    # tournaments
    run_sql_command(
            "INSERT INTO "
            "tournaments (ID, finished_time, price, prize, position, elapsed_time, Entries) "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                tournament.id,
                tournament.finish_time,
                tournament.price,
                tournament.prize,
                tournament.position,
                tournament.elapsed_time,
                tournament.re_entries
        ),
        database_file_path)

    # hands
    for hand in tournament.hands:
        run_sql_command(
            "INSERT INTO "
            "hands (`tourney_id`, `time`, `my_cards`, `board_cards`, `hand_id`, `Stack size at start of hand`, `Winner (Main Pot)`,`Winner (Side Pot #1)`, `Winner (Side Pot #2)`, `Winner (Side Pot #3)`, `Pot Size (Main Pot)`, `Pot Size (Side Pot #1)`, `Pot Size (Side Pot #2)`, `Pot Size (Side Pot #3)`, `level`, `hand_txt`) "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                hand.tournament_id,
                hand.time,
                hand.my_cards,
                hand.board_cards,
                hand.id,
                hand.starting_stack_size_bb,
                hand.main_pot_winner,
                hand.side_pot_1_winner,
                hand.side_pot_2_winner,
                hand.side_pot_3_winner,
                hand.main_pot_size_bb,
                hand.side_pot_1_size_bb,
                hand.side_pot_2_size_bb,
                hand.side_pot_3_size_bb,
                hand.level,
                hand.hand_txt
            ),
            database_file_path)
