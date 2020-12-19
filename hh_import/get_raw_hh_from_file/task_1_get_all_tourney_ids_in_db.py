from helpers.run_sql_command import run_sql_command


def get_all_tourney_ids_in_db() -> list:
    '''
    :return: a list of unique IDs of tournaments currently saved in the database
    '''
    return run_sql_command('SELECT ID FROM tournaments', unique_items=True)
