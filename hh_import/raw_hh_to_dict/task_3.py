from helpers.extract_id_from_title import extract_id_from_title
from helpers.run_sql_command import run_sql_command


def task_3(filenames: list) -> list:
    '''
    remove filenames already in the db
    '''
    hh_in_db = run_sql_command('SELECT ID FROM tournaments', unique_items=True)
    filtered = []
    for file_name in filenames:
        tournament_id = extract_id_from_title(file_name)
        if tournament_id not in hh_in_db:
            filtered.append(file_name)
    return filtered
