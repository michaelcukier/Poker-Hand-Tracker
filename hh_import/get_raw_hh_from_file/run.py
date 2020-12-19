from .task_1_get_all_tourney_ids_in_db import *
from .task_2_get_all_hh_filenames import *
from .task_3_get_relevant_hh_filenames import *
from .task_4_remove_duplicates_db_and_hh_folder import *

from .get_tourney_content_and_summary_from_filename import *


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

    task_1 = get_all_tourney_ids_in_db()
    task_2 = get_all_hh_filenames_in_folder()
    task_3 = get_relevant_hh_filenames(task_2)
    task_4 = remove_duplicates_db_and_hh_folder(task_3, task_1)

    hhs = []
    for filename in task_4:
        hhs.append({
            'title': filename,
            'content': get_tournament_content(filename),
            'summary': get_tournament_summary(get_tournament_content(filename))
        })

    return hhs


get_new_raw_hh_from_file()