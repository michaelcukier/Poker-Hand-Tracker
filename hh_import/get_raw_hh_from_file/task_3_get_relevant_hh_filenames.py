from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT


def get_relevant_hh_filenames(filenames: list) -> list:
    '''
    :param filenames: list of all filenames in folder
    :return: list of filenames containing only the ones I want to add to the database
    '''
    filtered = []
    for file_name in filenames:
        if file_name in TOURNAMENTS_TO_EXTRACT:
            filtered.append(file_name)
    return filtered
