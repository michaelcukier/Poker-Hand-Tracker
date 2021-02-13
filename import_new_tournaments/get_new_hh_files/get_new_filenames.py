from .tasks.query_local_filesystem import query_local_filesystem
from .tasks.remove_untracked_tournaments import remove_untracked_tournaments
from .tasks.query_local_database import query_local_database
from .tasks.group_filenames_by_id import group_filenames_by_id
from .tasks.get_tournament_summaries_and_re_entries import get_tournament_summaries_and_re_entries


def get_new_filenames(HH_PATH:str, TOURNAMENT_SUMMARY_FOLDER:str, DATABASE_PATH:str) -> list:
    """
    Returns a list of TournamentFiles

            Parameters:
                    HH_PATH (str): absolute path of the hand history files
                    TOURNAMENT_SUMMARY_FOLDER (str): absolute path of the tournament summary files
                    DATABASE_PATH (str): absolute path of the database

            Returns:
                    tournament (list): a list of TournamentFiles
    """

    # returns a list of Filename to be processed
    tournaments = query_local_filesystem(HH_PATH)
    tournaments = remove_untracked_tournaments(tournaments)
    tournaments = query_local_database(tournaments, DATABASE_PATH)

    # here we create the TournamentFiles class
    tournaments = group_filenames_by_id(tournaments)
    tournaments = get_tournament_summaries_and_re_entries(tournaments, TOURNAMENT_SUMMARY_FOLDER)

    return tournaments
