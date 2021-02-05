from GLOBAL_VARIABLES import PLAYER_NAME


def extract_prize(tourney_summary: dict):
    if tourney_summary is None:
        return 0
    for player in tourney_summary['tournament_finishes_and_winnings']:
        if player['player_name'] == PLAYER_NAME:
            return player['prize']
