from get_all_tourney_ids_in_db import *
from get_all_folder_hh_filenames import *
from get_tracked_hh_filenames import *
from remove_duplicates_db_and_hh_folder import *

from get_tourney_content_and_summary_from_filename import *


def get_new_raw_hh_from_file() -> list:
    '''
    this function performs tasks to return
    the new hand histories
    :return:
    [{
        'title': str,
        'content': str,
        'summary': str
    },  { ... }
    ]
    '''

    all_tournaments_ids_in_db = get_all_tourney_ids_in_db()

    all_tournaments_filenames_in_folder = get_all_hh_filenames_in_folder()

    tournaments_in_folder_that_are_tracked = get_tracked_hh_filenames(all_tournaments_filenames_in_folder)

    remove_duplicates_folder_and_db = remove_duplicates_db_and_hh_folder(
        filenames=tournaments_in_folder_that_are_tracked,
        ids_already_in_db=all_tournaments_ids_in_db)

    hhs = []
    for filename in remove_duplicates_folder_and_db:
        hhs.append({
            'title': filename,
            'content': get_tournament_content(filename),
            'summary': get_tournament_summary(filename)
        })

    return hhs


print(get_new_raw_hh_from_file())