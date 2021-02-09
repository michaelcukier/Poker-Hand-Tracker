import sqlite3
import contextlib


def run_sql_command(query, database_file_path, unique_items=False):
    with contextlib.closing(sqlite3.connect(database_file_path)) as conn:
        with conn:
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                cursor.execute(query)
                records = cursor.fetchall()
    if unique_items:
        return [x[0] for x in records]
    return records
