from GLOBAL_VARIABLES import PLAYER_NAME
import copy


def position(parent_folder_ts: str, ts_filename: str):
    # check if no tourney summary
    if ts_filename is None:
        return 0

    # open ts
    with open(parent_folder_ts + ts_filename, 'r') as f:
        data = f.read()
        ts = eval(copy.deepcopy(data))

    for player in ts['tournament_finishes_and_winnings']:
        if player['player_name'] == PLAYER_NAME:
            return player['finish_position']
