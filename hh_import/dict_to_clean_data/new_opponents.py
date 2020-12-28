from helpers.check_no_tourney_summary import check_no_tourney_summary
from GLOBAL_VARIABLES import PLAYER_NAME


def extract_opponents_names(tourney_summary: dict) -> list:
    if check_no_tourney_summary(tourney_summary):
        return []

    opponents = []
    for opp in tourney_summary['tournament_finishes_and_winnings']:
        opponents.append(opp['player_name'])

    opp_no_duplicates = list(dict.fromkeys(opponents))

    opp_no_duplicates.remove(PLAYER_NAME)

    return opp_no_duplicates

