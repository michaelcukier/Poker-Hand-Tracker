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
                "hands (`tourney_id`, `time`, `my_cards`, `board_cards`, `replayer_link`, `hand_id`, `Stack size at start of hand`, `Winner (Main Pot)`,`Winner (Side Pot #1)`, `Winner (Side Pot #2)`, `Winner (Side Pot #3)`, `Pot Size (Main Pot)`, `Pot Size (Side Pot #1)`, `Pot Size (Side Pot #2)`, `Pot Size (Side Pot #3)`, `level`) "
                "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    new_hand['tourney_id'],
                    new_hand['time'],
                    new_hand['my_cards'],
                    new_hand['board_cards'],
                    new_hand['replayer_link'],
                    new_hand['hand_id'],
                    new_hand['Stack size at start of hand'],
                    new_hand['Winner (Main Pot)'],
                    new_hand['Winner (Side Pot #1)'],
                    new_hand['Winner (Side Pot #2)'],
                    new_hand['Winner (Side Pot #3)'],
                    new_hand['Pot Size (Main Pot)'],
                    new_hand['Pot Size (Side Pot #1)'],
                    new_hand['Pot Size (Side Pot #2)'],
                    new_hand['Pot Size (Side Pot #3)'],
                    new_hand['level']
                ))

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

