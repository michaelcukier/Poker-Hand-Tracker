from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT


def get_tracked_hh_filenames(filenames: list) -> list:
    '''
    :param filenames: list of all filenames in folder
    :return: list of filenames containing only the ones I want to add to the database
    '''
    filtered = []
    for file_name in filenames:
        for tourney in TOURNAMENTS_TO_EXTRACT:
            if tourney in file_name:
                filtered.append(file_name)
    return filtered
