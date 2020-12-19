

def extract_id_from_title(title: str):
    return title.split('SITGOID-G')[1].split('T2 TN')[0]


def remove_duplicates_db_and_hh_folder(filenames: list, ids_already_in_db: list) -> list:
    '''
    remove duplicates between filenames already in db and new ones
    '''
    filtered = []
    for file_name in filenames:
        tournament_id = extract_id_from_title(file_name)
        if tournament_id not in ids_already_in_db:
            filtered.append(file_name)
    return filtered
