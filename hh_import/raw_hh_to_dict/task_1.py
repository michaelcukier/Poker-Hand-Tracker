from os.path import isfile, join
from os import listdir
from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER


def task_1(custom_folder=False) -> list:
    '''
    :return: list of all the file names in a particular folder
    '''
    files = [f for f in listdir(custom_folder if custom_folder else HAND_HISTORY_FOLDER) if isfile(join(custom_folder if custom_folder else HAND_HISTORY_FOLDER, f))]
    return files
