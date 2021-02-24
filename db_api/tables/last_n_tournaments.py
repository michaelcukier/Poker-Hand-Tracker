from prettytable import PrettyTable

from utils.run_sql_command import run_sql_command
import timeago, datetime

from datetime import datetime

def last_n_tournaments(n: int, database_file_path: str) -> PrettyTable:
    """
    Returns the last n tournaments played in a table format

            Parameters:
                    n (int): the number of tournaments to return
                    database_file_path (str): the path of the database file

            Returns:
                    table (str): the table
    """

    query = '''
        SELECT 
            ID, finished_time, price, prize, position, elapsed_time, Entries 
        FROM 
            tournaments 
        ORDER BY 
            finished_time DESC
        LIMIT 
            {0}
    '''.format(str(n))

    data = run_sql_command(
        query=query,
        unique_items=False,
        database_file_path=database_file_path)

    t = PrettyTable(['ID', 'When', 'Buyin', 'Prize', 'Position', 'Duration (mn)'])

    for ID, finished_time, price, prize, position, elapsed_time, Entries in data:

        now = datetime.now()
        dt_object1 = datetime.strptime(finished_time.replace(' UTC', ''), "%Y/%m/%d %H:%M:%S")

        money = round(prize-price, 2)
        if money > 0:
            mn = '\033[92m' + str(prize)
        else:
            mn = '\033[91m' + '-' + str(price)

        t.add_row([
            ID,
            timeago.format(dt_object1, now),
            price,
            mn + '\033[0m',
            position,
            str(elapsed_time)
        ])

    return t


# from GLOBAL_VARIABLES import DATABASE_LOCATION
# print(last_n_tournaments(4, DATABASE_LOCATION))
