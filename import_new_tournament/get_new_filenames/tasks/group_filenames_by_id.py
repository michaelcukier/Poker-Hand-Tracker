from TournamentFiles.TournamentFiles import TournamentFiles
from utils.extract_id_from_title import extract_id_from_title

def group_filenames_by_id(filenames: list) -> list:
    '''
    group remaining filenames and create a dict: {tourney_ID: [filename1, filename2, ...]}
    '''

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