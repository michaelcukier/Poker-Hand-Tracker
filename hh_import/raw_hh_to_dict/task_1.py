from os.path import isfile, join
from os import listdir
from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER


def task_1(FOR_TESTING_CUSTOM_FOLDER=False) -> list:
    '''
    :return: list of all the file names in a particular folder
    '''
    files = [f for f in listdir(FOR_TESTING_CUSTOM_FOLDER if FOR_TESTING_CUSTOM_FOLDER else HAND_HISTORY_FOLDER) if isfile(join(FOR_TESTING_CUSTOM_FOLDER if FOR_TESTING_CUSTOM_FOLDER else HAND_HISTORY_FOLDER, f))]
    return files
