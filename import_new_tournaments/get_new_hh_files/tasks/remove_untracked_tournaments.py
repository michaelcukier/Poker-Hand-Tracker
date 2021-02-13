from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT


def remove_untracked_tournaments(filenames: list) -> list:
    """
    Removes filenames that aren't tracked

            Parameters:
                    filenames (list): tournament files names

            Returns:
                    filtered (list): tournament files names
    """

    filtered = []
    for file_name in filenames:
        for tourney in TOURNAMENTS_TO_EXTRACT.keys():
            if tourney in file_name:
                filtered.append(file_name)
    return filtered
