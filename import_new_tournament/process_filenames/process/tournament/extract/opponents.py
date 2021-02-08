from GLOBAL_VARIABLES import PLAYER_NAME
import copy


def opponents(parent_folder_ts: str, ts_filename: str) -> list:
    if ts_filename is None:
        return []

    # open ts
    with open(parent_folder_ts + ts_filename, 'r') as f:
        data = f.read()
        ts = eval(copy.deepcopy(data))

    opponents = []
    for opp in ts['tournament_finishes_and_winnings']:
        opponents.append(opp['player_name'])

    opp_no_duplicates = list(dict.fromkeys(opponents))

    opp_no_duplicates.remove(PLAYER_NAME)

    return opp_no_duplicates

