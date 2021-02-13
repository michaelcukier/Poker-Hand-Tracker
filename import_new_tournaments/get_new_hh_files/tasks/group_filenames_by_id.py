from utils.extract_id_from_title import extract_id_from_title
from import_new_tournaments.get_new_hh_files.TournamentFiles.TournamentFiles import TournamentFiles


def group_filenames_by_id(filenames: list) -> list:
    """
    Takes a list of tournament files names and creates a TournamentFiles class from them

            Parameters:
                    filenames (List[str]): a list of tournament files names

            Returns:
                    tournament_files (list): a list of TournamentFiles classes
    """

    filenames_classes = {}
    for file_name in filenames:
        id = extract_id_from_title(file_name)
        if id in filenames_classes:
            filenames_classes.get(id).add_hand_history_filename(file_name)
        else:
            new_t = TournamentFiles(id)
            new_t.add_hand_history_filename(file_name)
            filenames_classes[id] = new_t
    return list(filenames_classes.values())
