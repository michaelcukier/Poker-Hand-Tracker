from GLOBAL_VARIABLES import PLAYER_NAME
import copy


def position(parent_folder_ts: str, ts_filename: str) -> int:
    """
    Extracts the finish position

            Parameters:
                    parent_folder_ts (str): the parent folder where the tournament summary file is located
                    ts_filename (str): the name of the tournament summary file

            Returns:
                    finish_pos (int): the finish position
    """

    # check if no tourney summary
    if ts_filename is None:
        return 0

    # open ts
    with open(parent_folder_ts + ts_filename, 'r') as f:
        data = f.read()
        ts = eval(copy.deepcopy(data))

    for player in ts['tournament_finishes_and_winnings']:
        if player['player_name'] == PLAYER_NAME:
            finish_pos = player['finish_position']
            return finish_pos
