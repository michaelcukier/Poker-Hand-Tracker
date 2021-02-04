from utils.run_sql_command import run_sql_command


def query_local_database(filenames: list) -> list:
    '''
    remove filenames already in the db
    '''

    def extract_id_from_title(title: str):
        return title.split('SITGOID-G')[1].split(' TN')[0].split('T')[0]

    hh_in_db = run_sql_command('''
        SELECT 
        ID 
        FROM 
        tournaments
    ''', unique_items=True)

    filtered = []
    for file_name in filenames:
        tournament_id = extract_id_from_title(file_name)
        if tournament_id not in hh_in_db:
            filtered.append(file_name)
    return filtered
