from prettytable import PrettyTable

from utils.run_sql_command import run_sql_command
import timeago, datetime

from datetime import datetime


def daily_report(n: int, database_file_path: str):
    """
    Returns the last n tournaments played in a table format

            Parameters:
                    n (int): the number of tournaments to return
                    database_file_path (str): the path of the database file

            Returns:
                    table (str): the table


                            GROUP BY
            the_day
    """


    # query = '''
    #     SELECT
    #         ROW_NUMBER() OVER(ORDER BY ID) AS RN,
    #         ID,
    #         time(SUBSTR(finished_time, 12, 8), '-' || elapsed_time || ' minutes') as startTime,
    #         SUBSTR(finished_time, 12, 8) as endTime,
    #         elapsed_time
    #     FROM
    #         tournaments
    #     LIMIT
    #         {0}
    # '''.format(str(n))

    # query = '''
    #
    #     SELECT
    #         COUNT(ID),
    #         ROUND(SUM(price), 2),
    #         ROUND(SUM(prize), 2),
    #         SUBSTR(finished_time, 0, 11) AS the_day,
    #         finished_time AS raw_date
    #     FROM
    #         tournaments
    #     GROUP BY
    #         the_day
    #     ORDER BY
    #         raw_date DESC
    #     LIMIT
    #         {0}
    # '''.format(str(n))

    data = run_sql_command(
        query=query,
        unique_items=False,
        database_file_path=database_file_path)

    return data
    #
    # # Day | Nb of games played | Money spent | Money won | session length
    # t = PrettyTable(['Day', 'Nb. of games played', 'Money spent', 'Money won', 'Session duration (mn)'])
    #
    # return t





from GLOBAL_VARIABLES import DATABASE_LOCATION

for x in daily_report(5, DATABASE_LOCATION):
    print(x)






