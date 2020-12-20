from os import listdir
import copy
from GLOBAL_VARIABLES import TOURNEY_SUMMARY_FOLDER


def task_7(tourneys: dict) -> dict:
    '''
    extracts the tourney summary from filesystem into a string
    '''
    for tourney_id, hands in tourneys.items():
        summary_file_name = [f for f in listdir(TOURNEY_SUMMARY_FOLDER) if str(tourney_id) in f]
        if len(summary_file_name) == 0:
            tourneys[tourney_id]['summary'] = None
        else:
            sum = open(TOURNEY_SUMMARY_FOLDER + summary_file_name[0], "r")
            hhsum = eval(copy.deepcopy(sum.read()))
            tourneys[tourney_id]['summary'] = hhsum
    return tourneys
