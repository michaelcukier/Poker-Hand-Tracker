import click
from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER, TOURNEY_SUMMARY_FOLDER, DATABASE_LOCATION
from import_new_tournaments.get_new_hh_files.get_new_filenames import get_new_filenames
from import_new_tournaments.process_hh_files.process_filenames import process_filenames
from import_new_tournaments.store_processed_files_in_db.store_processed_files_in_db import store_processed_files_in_db


@click.command(short_help='Updates the database with new tournaments')
def update_db():
    # 1- get the new filenames
    new_tourneys_filenames = get_new_filenames(
        HAND_HISTORY_FOLDER,
        TOURNEY_SUMMARY_FOLDER,
        DATABASE_LOCATION)

    # 2- process the filenames
    processed_tournaments = process_filenames(
        new_tourneys_filenames,
        parent_folder_hand_history=HAND_HISTORY_FOLDER,
        parent_folder_tournament_summary=TOURNEY_SUMMARY_FOLDER)

    # 3- store the tournaments
    for t in processed_tournaments:
        store_processed_files_in_db(t, database_file_path=DATABASE_LOCATION)

    click.secho('Added ' + str(len(processed_tournaments)) + ' new tournaments', fg="blue", bold=True)
