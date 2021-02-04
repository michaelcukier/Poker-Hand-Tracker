from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT


def remove_untracked_tournaments(filenames: list) -> list:
    '''
    remove filenames that aren't tracked
    '''

    filtered = []
    for file_name in filenames:
        for tourney in TOURNAMENTS_TO_EXTRACT.keys():
            if tourney in file_name:
                filtered.append(file_name)
    return filtered
