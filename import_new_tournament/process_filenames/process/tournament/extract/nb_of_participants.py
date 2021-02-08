import copy


def nb_of_participants(parent_folder_ts: str, ts_filename: str) -> int:
    if ts_filename is None:
        return 0

    # open ts
    with open(parent_folder_ts + ts_filename, 'r') as f:
        data = f.read()
        ts = eval(copy.deepcopy(data))

    return int(ts['player_count'])
