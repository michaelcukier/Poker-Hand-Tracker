from helpers.run_sql_command import run_sql_command


def run(clean_data):
    for new_tourney in clean_data:

        # add new tournaments to `tournaments` table
        run_sql_command(
            "INSERT INTO "
            "tournaments (ID, finished_time, price, prize, position, elapsed_time) "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            new_tourney['new_tournament']['id'],
            new_tourney['new_tournament']['finished_time'],
            new_tourney['new_tournament']['price'],
            new_tourney['new_tournament']['prize'],
            new_tourney['new_tournament']['position'],
            new_tourney['new_tournament']['elapsed_time']))

        # add new hands to `hands` table
        for new_hand in new_tourney['new_hands']:
            run_sql_command(
                "INSERT INTO "
                "hands (tourney_id, time, pot_size_chips, pot_size_bb, level, my_cards, board_cards, replayer_link, hand_id) "
                "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                new_hand['tourney_id'],
                new_hand['time'],
                new_hand['pot_size_chips'],
                new_hand['pot_size_bb'],
                new_hand['level'],
                new_hand['my_cards'],
                new_hand['board_cards'],
                new_hand['replayer_link'],
                new_hand['hand_id']))

        # add new opponents:
        # if opp is already in db, increment seen by 1
        # otherwise, create the opp with seen=1
        opponents_in_db = run_sql_command('SELECT ALL name FROM opponents', unique_items=True)
        for new_opp in new_tourney['new_opponents']:
            if new_opp in opponents_in_db:
                run_sql_command('UPDATE opponents SET seen = seen + 1 WHERE name="' + new_opp + '"')
            else:
                run_sql_command(
                    "INSERT INTO "
                    "opponents (name, seen) "
                    "VALUES ('{}', '{}')".format(
                    new_opp,
                    1))

