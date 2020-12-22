from os import listdir
import copy
from GLOBAL_VARIABLES import TOURNEY_SUMMARY_FOLDER


def task_7(tourneys: dict, FOR_TESTING_CUSTOM_FOLDER=False) -> dict:
    '''
    extracts the tourney summary from filesystem into a dict
    '''
    for tourney_id, hands in tourneys.items():
        summary_file_name = [f for f in listdir(FOR_TESTING_CUSTOM_FOLDER if FOR_TESTING_CUSTOM_FOLDER else TOURNEY_SUMMARY_FOLDER) if str(tourney_id) in f]
        if len(summary_file_name) == 0:
            tourneys[tourney_id]['summary'] = None
        else:
            with open((FOR_TESTING_CUSTOM_FOLDER if FOR_TESTING_CUSTOM_FOLDER else TOURNEY_SUMMARY_FOLDER) + summary_file_name[0], 'r') as f:
                data = f.read()
                hhsum = eval(copy.deepcopy(data))
            tourneys[tourney_id]['summary'] = hhsum
    return tourneys
