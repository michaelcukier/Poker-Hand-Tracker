import click
from GLOBAL_VARIABLES import DATABASE_LOCATION
import sqlite3


@click.command()
def setup_database():
    con = sqlite3.connect(DATABASE_LOCATION)
    cur = con.cursor()
    hands_table = """ 
    CREATE TABLE "hands" (
        "tourney_id"	TEXT,
        "time"	TEXT,
        "level"	TEXT,
        "my_cards"	TEXT,
        "board_cards"	TEXT,
        "hand_id"	TEXT,
        "stack_size"	INTEGER,
        "Winner (Main Pot)"	TEXT,
        "Winner (Side Pot #1)"	TEXT,
        "Winner (Side Pot #2)"	TEXT,
        "Winner (Side Pot #3)"	TEXT,
        "Pot Size (Main Pot)"	INT,
        "Pot Size (Side Pot #1)"	INT,
        "Pot Size (Side Pot #2)"	INT,
        "Pot Size (Side Pot #3)"	INT,
        "hand_txt"	TEXT,
        "BTN_player_name"	TEXT,
        "SB_player_name"	TEXT,
        "BB_player_name"	TEXT,
        "UTG_player_name"	TEXT,
        "UTGp1_player_name"	TEXT,
        "MP_player_name"	TEXT,
        "MPp1_player_name"	TEXT,
        "MPp2_player_name"	TEXT,
        "CO_player_name"	TEXT,
        "BTN_stack"	INT,
        "SB_stack"	INT,
        "BB_stack"	INT,
        "UTG_stack"	INT,
        "UTGp1_stack"	INT,
        "MP_stack"	INT,
        "MPp1_stack"	INT,
        "MPp2_stack"	INT,
        "CO_stack"	INT,
        "BTN_cards"	TEXT,
        "SB_cards"	TEXT,
        "BB_cards"	TEXT,
        "UTG_cards"	TEXT,
        "UTGp1_cards"	TEXT,
        "MP_cards"	TEXT,
        "MPp1_cards"	TEXT,
        "MPp2_cards"	TEXT,
        "CO_cards"	TEXT,
        "table_type"	TEXT,
        "nb_occupied_seats"	INT,
        PRIMARY KEY("hand_id")
    )
    """
    cur.execute(hands_table)
    tournaments_table = """
    CREATE TABLE "tournaments" (
        "ID"	TEXT,
        "finished_time"	TEXT,
        "price"	INT,
        "prize"	INT,
        "position"	INT,
        "elapsed_time"	INT,
        "Entries"	INT,
        PRIMARY KEY("ID")
    )
    """
    cur.execute(tournaments_table)

