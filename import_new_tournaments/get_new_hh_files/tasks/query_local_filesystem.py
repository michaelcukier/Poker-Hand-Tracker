from os.path import isfile, join
from os import listdir


def query_local_filesystem(HAND_HISTORY_FOLDER: str) -> list:
    """
    Returns a list of all filenames in a folder

            Parameters:
                    HAND_HISTORY_FOLDER (str): parent folder of the files

            Returns:
                    files (list): a list of the filenames inside HAND_HISTORY_FOLDER
    """

    files = [f for f in listdir(HAND_HISTORY_FOLDER) if isfile(join(HAND_HISTORY_FOLDER, f))]
    return files
