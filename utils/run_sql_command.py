import sqlite3
import contextlib
from GLOBAL_VARIABLES import DATABASE_LOCATION


def run_sql_command(query, unique_items=False):
    with contextlib.closing(sqlite3.connect(DATABASE_LOCATION)) as conn:
        with conn:
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                cursor.execute(query)
                records = cursor.fetchall()
    if unique_items:
        return [x[0] for x in records]
    return records
