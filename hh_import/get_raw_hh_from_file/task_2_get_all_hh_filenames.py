from os.path import isfile, join
from os import listdir
from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER

def get_all_hh_filenames_in_folder() -> list:
    '''
    :return: list of all the file names in a particular folder
    '''
    files = [f for f in listdir(HAND_HISTORY_FOLDER) if isfile(join(HAND_HISTORY_FOLDER, f))]
    return files
