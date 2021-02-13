import sqlite3
import contextlib


def run_sql_command(query: str, database_file_path:str, unique_items=False) -> list:
    """
    Returns the output of an SQL query performed on a specified SQLite database

        Parameters:
            query (str): An SQL query
            database_file_path (str): absolute path of the SQLite database file
            unique_items (bool): whether the function should return a list
            of items instead of a list of tuples with one value

        Returns:
            records (list): The output of the SQLite database
    """
    with contextlib.closing(sqlite3.connect(database_file_path)) as conn:
        with conn:
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                cursor.execute(query)
                records = cursor.fetchall()
    if unique_items:
        return [x[0] for x in records]
    return records
