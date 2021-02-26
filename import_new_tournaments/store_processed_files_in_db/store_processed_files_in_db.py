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
            "hands (`tourney_id`, `time`, `my_cards`, `board_cards`, `hand_id`, `stack_size`, `Winner (Main Pot)`,`Winner (Side Pot #1)`, `Winner (Side Pot #2)`, `Winner (Side Pot #3)`, `Pot Size (Main Pot)`, `Pot Size (Side Pot #1)`, `Pot Size (Side Pot #2)`, `Pot Size (Side Pot #3)`, `level`, `hand_txt`, `BTN_player_name`, `SB_player_name`, `BB_player_name`, `UTG_player_name`, `UTGp1_player_name`, `MP_player_name`, `MPp1_player_name`, `MPp2_player_name`, `CO_player_name`, `BTN_stack`, `SB_stack`, `BB_stack`, `UTG_stack`, `UTGp1_stack`, `MP_stack`, `MPp1_stack`, `MPp2_stack`, `CO_stack`, `BTN_cards`, `SB_cards`, `BB_cards`, `UTG_cards`, `UTGp1_cards`, `MP_cards`, `MPp1_cards`, `MPp2_cards`, `CO_cards`, `table_type`, `nb_occupied_seats`) "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
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
                hand.hand_txt,
                hand.BTN_player_name,
                hand.SB_player_name,
                hand.BB_player_name,
                hand.UTG_player_name,
                hand.UTGp1_player_name,
                hand.MP_player_name,
                hand.MPp1_player_name,
                hand.MPp2_player_name,
                hand.CO_player_name,
                hand.BTN_stack,
                hand.SB_stack,
                hand.BB_stack,
                hand.UTG_stack,
                hand.UTGp1_stack,
                hand.MP_stack,
                hand.MPp1_stack,
                hand.MPp2_stack,
                hand.CO_stack,
                hand.BTN_cards,
                hand.SB_cards,
                hand.BB_cards,
                hand.UTG_cards,
                hand.UTGp1_cards,
                hand.MP_cards,
                hand.MPp1_cards,
                hand.MPp2_cards,
                hand.CO_cards,
                hand.table_type,
                hand.nb_occupied_seats
            ),
            database_file_path)
