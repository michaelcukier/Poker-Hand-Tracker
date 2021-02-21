import copy


def nb_of_participants(parent_folder_ts: str, ts_filename: str) -> int:
    """
    Extracts the number of participants in a tournament

            Parameters:
                    parent_folder_ts (str): the parent folder where the tournament summary file is located
                    ts_filename (str): the name of the tournament summary file

            Returns:
                    nb_of_p (int): the number of participants
    """
    if ts_filename is None:
        return 0

    with open(parent_folder_ts + ts_filename, 'r') as f:
        data = f.read()
        ts = eval(copy.deepcopy(data))

    nb_of_p = int(ts['player_count'])
    return nb_of_p
