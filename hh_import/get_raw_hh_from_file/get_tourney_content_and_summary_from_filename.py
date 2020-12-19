from os import listdir
import copy
from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER, TOURNEY_SUMMARY_FOLDER


def extract_id_from_content(content: str) -> int:
    return int(content.split('\n')[0].split('Tournament ')[1][1:9])


def get_tournament_content(tournament_filename):
    f = open(HAND_HISTORY_FOLDER + '/' + tournament_filename, "r")
    hhtext = copy.deepcopy(f.read())
    return hhtext


def get_tournament_summary(content):
    id = extract_id_from_content(content)
    summary_file_name = [f for f in listdir(TOURNEY_SUMMARY_FOLDER) if str(id) in f][0]
    sum = open(TOURNEY_SUMMARY_FOLDER + '/' + summary_file_name, "r")
    hhsum = eval(copy.deepcopy(sum.read()))
    return hhsum
