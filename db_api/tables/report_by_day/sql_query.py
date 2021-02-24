from utils.run_sql_command import run_sql_command


def sql_query(database_file_path: str) -> list:


    query = '''
        WITH 
            startAndEndTimes 
        AS
            (
            SELECT 
                time(SUBSTR(finished_time, 12, 8), '-' || elapsed_time || ' minutes') as startTime,
                SUBSTR(finished_time, 12, 8) as endTime,
                SUBSTR(finished_time, 0, 11) AS the_day
            FROM 
                tournaments
            )
        SELECT 
            the_day,
            (
                WITH 
                    duration
                AS 
                (  
                    SELECT DISTINCT 
                        COALESCE(
                          (SELECT MIN(t2.startTime) 
                           FROM startAndEndTimes t2 
                           WHERE t1.startTime BETWEEN t2.startTime AND t2.endTime), t1.startTime) start,
                        COALESCE(
                          (SELECT MAX(t2.endTime) 
                           FROM startAndEndTimes t2 
                           WHERE t1.endTime BETWEEN t2.startTime AND t2.endTime), t1.startTime) end   
                    FROM startAndEndTimes t1
                )
                SELECT 
                    SUM(strftime('%s', end) - strftime('%s', start)) / 60 total
                FROM
                    duration
            )
        FROM 
            startAndEndTimes
        GROUP BY 
            the_day
    '''

    # query = '''
    #     SELECT
    #         SUBSTR(finished_time, 0, 11) AS the_day,
    #         COUNT(*),
    #         ROUND(sum(price), 2),
    #         ROUND(sum(prize), 2)
    #     FROM
    #         tournaments
    #     GROUP BY
    #         the_day
    # '''

    data = run_sql_command(
        query=query,
        unique_items=False,
        database_file_path=database_file_path)

    return data

# from GLOBAL_VARIABLES import DATABASE_LOCATION
# print(sql_query(DATABASE_LOCATION))