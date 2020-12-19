def extract_opponents_names(tourney_summary: dict) -> list:
    # NEED TO CHECK IF IN SQL DB FIRST !!!
    # check for uniqueness too !!!

    opponents = []
    for opp in tourney_summary['tournament_finishes_and_winnings']:
        opponents.append(opp['player_name'])

    opp_no_duplicates = list(dict.fromkeys(opponents))

    return opp_no_duplicates

