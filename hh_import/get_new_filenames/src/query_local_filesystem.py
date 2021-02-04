from os.path import isfile, join
from os import listdir


def query_local_filesystem(HAND_HISTORY_FOLDER) -> list:
    '''
    :return: list of all the file names in a particular folder
    '''
    files = [f for f in listdir(HAND_HISTORY_FOLDER) if isfile(join(HAND_HISTORY_FOLDER, f))]
    return files
