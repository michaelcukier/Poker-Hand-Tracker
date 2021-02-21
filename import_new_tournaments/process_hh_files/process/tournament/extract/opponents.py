from GLOBAL_VARIABLES import PLAYER_NAME
import copy


def opponents(parent_folder_ts: str, ts_filename: str) -> list:
    """
    Extracts the names of the players in a tournament

            Parameters:
                    parent_folder_ts (str): the parent folder where the tournament summary file is located
                    ts_filename (str): the name of the tournament summary file

            Returns:
                    opp_no_duplicates (list): a list of players names
    """
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

