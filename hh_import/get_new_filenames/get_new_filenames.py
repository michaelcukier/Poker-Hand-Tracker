
from src.query_local_filesystem import query_local_filesystem
from src.remove_untracked_tournaments import remove_untracked_tournaments
from src.query_local_database import query_local_database
from src.group_filenames_by_id import group_filenames_by_id
from src.get_tournament_summaries_and_re_entries import get_tournament_summaries_and_re_entries


def get_new_filenames(HH_PATH):
    # returns a list of Filename to be processed

    tournaments = query_local_filesystem(HH_PATH)
    # print(len(tournaments))

    tournaments = remove_untracked_tournaments(tournaments)
    # print(len(tournaments))

    tournaments = query_local_database(tournaments)
    # print(len(tournaments))

    # here we create the TournamentFiles class
    tournaments = group_filenames_by_id(tournaments)
    # print(len(tournaments))

    tournaments = get_tournament_summaries_and_re_entries(tournaments)
    # print(len(tournaments))
    return tournaments


#
#
# from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER
# for x in get_new_tourneys_filenames(HAND_HISTORY_FOLDER):
#     for k in x.__dict__:
#         print(k)
#
#     print()
#     print()

