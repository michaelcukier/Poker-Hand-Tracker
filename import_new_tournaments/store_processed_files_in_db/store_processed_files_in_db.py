from utils.run_sql_command import run_sql_command

from ..process_hh_files.process.tournament.Tournament.Tournament import Tournament

def store_processed_files_in_db(tournament: Tournament, database_file_path: str):

    # add new process to `process` table
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
        tournament.re_entries),
    database_file_path)

    # add new hands to `hands` table
    for hand in tournament.hands:
        run_sql_command(
            "INSERT INTO "
            "hands (`tourney_id`, `time`, `my_cards`, `board_cards`, `hand_id`, `Stack size at start of hand`, `Winner (Main Pot)`,`Winner (Side Pot #1)`, `Winner (Side Pot #2)`, `Winner (Side Pot #3)`, `Pot Size (Main Pot)`, `Pot Size (Side Pot #1)`, `Pot Size (Side Pot #2)`, `Pot Size (Side Pot #3)`, `level`) "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
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
            ),
    database_file_path)

    # add new opponents:
    # if opp is already in db, increment seen by 1
    # otherwise, create the opp with seen=1
    opponents_in_db = run_sql_command('SELECT ALL name FROM opponents', unique_items=True, database_file_path=database_file_path)
    for new_opp in tournament.opponents:
        if new_opp in opponents_in_db:
            run_sql_command('UPDATE opponents SET seen = seen + 1 WHERE name="' + new_opp + '"', database_file_path)
        else:
            run_sql_command(
                "INSERT INTO "
                "opponents (name, seen) "
                "VALUES ('{}', '{}')".format(
                new_opp,
                1),
            database_file_path)
