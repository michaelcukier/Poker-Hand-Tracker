from os import listdir
import copy
from GLOBAL_VARIABLES import TOURNEY_SUMMARY_FOLDER
import sys


def task_7(tourneys: dict, FOR_TESTING_CUSTOM_FOLDER=False) -> dict:
    '''
    extracts the tourney summary from filesystem into a dict
    '''

    def find_best_summary_when_multiple_filenames(summary_file_name: list):
        all = {}
        for file in summary_file_name:
            with open((FOR_TESTING_CUSTOM_FOLDER if FOR_TESTING_CUSTOM_FOLDER else TOURNEY_SUMMARY_FOLDER) + file, 'r') as f:
                data = f.read()
                hhsum = eval(copy.deepcopy(data))
                all[file] = hhsum['player_count']
        return max(all, key=all.get)

    for tourney_id, hands in tourneys.items():
        summary_file_name = [f for f in listdir(FOR_TESTING_CUSTOM_FOLDER if FOR_TESTING_CUSTOM_FOLDER else TOURNEY_SUMMARY_FOLDER) if str(tourney_id) in f]
        re_entries = 1
        if len(summary_file_name) == 0:
            tourneys[tourney_id]['summary'] = None
        else:
            if len(summary_file_name) == 1:
                real_summary_file_name = summary_file_name[0]
            if len(summary_file_name) > 1:
                re_entries = len(summary_file_name)
                real_summary_file_name = find_best_summary_when_multiple_filenames(summary_file_name)
            with open((FOR_TESTING_CUSTOM_FOLDER if FOR_TESTING_CUSTOM_FOLDER else TOURNEY_SUMMARY_FOLDER) + real_summary_file_name, 'r') as f:
                data = f.read()
                hhsum = eval(copy.deepcopy(data))
            tourneys[tourney_id]['summary'] = hhsum
        tourneys[tourney_id]['re_entries'] = re_entries
    return tourneys
