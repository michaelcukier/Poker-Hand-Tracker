from GLOBAL_VARIABLES import PLAYER_NAME
import copy


def prize(parent_folder_ts: str, ts_filename: str) -> float:
    """
    Extracts the money prize amount of the tournament

            Parameters:
                    parent_folder_ts (str): the parent folder where the tournament summary file is located
                    ts_filename (str): the name of the tournament summary file

            Returns:
                    prize_ (float): the money amount received
    """
    if ts_filename is None:
        return 0

    # open ts
    with open(parent_folder_ts + ts_filename, 'r') as f:
        data = f.read()
        ts = eval(copy.deepcopy(data))

    # get the info
    for player in ts['tournament_finishes_and_winnings']:
        if player['player_name'] == PLAYER_NAME:
            prize_ = player['prize']
            return prize_
