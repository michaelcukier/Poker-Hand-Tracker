from GLOBAL_VARIABLES import PLAYER_NAME


def extract_position(tourney_summary: dict):
    # check if no tourney summary
    if tourney_summary is None:
        return 0

    for player in tourney_summary['tournament_finishes_and_winnings']:
        if player['player_name'] == PLAYER_NAME:
            return player['finish_position']
