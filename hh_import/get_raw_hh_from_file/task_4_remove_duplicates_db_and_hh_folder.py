def remove_duplicates_db_and_hh_folder(filenames: list, ids_already_in_db: list) -> list:
    '''
    remove duplicates between filenames already in db and new ones
    '''
    filtered = []
    for file_name in filenames:
        if file_name not in ids_already_in_db:
            filtered.append(file_name)
    return filtered
