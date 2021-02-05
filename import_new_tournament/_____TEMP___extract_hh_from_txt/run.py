from task_1 import *
from task_2 import *
from task_3 import *
from task_4 import *
from task_5 import *
from task_6 import *
from task_7 import *

from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER


def run():
    task1 = task_1(HAND_HISTORY_FOLDER)         # none -> list | Query the local filesystem to get all the .txt filenames in the hand history folder
    task2 = task_2(task1)                       # list -> list | Remove the tournament that aren't tracked
    task3 = task_3(task2)                       # list -> list | Remove the tournament IDs already in the db
    task4 = task_4(task3)                       # list -> dict | Group the remaining ones like this: {tourney_ID: {'filenames': filename1, filename2, ...}}
    task5 = task_5(task4)                       # dict -> dict | Concatenate the multiple .txt files into one big list of hands
    task6 = task_6(task5)                       # dict -> dict | Clean that list of hands to remove the hands where i'm not playing
    task7 = task_7(task6)                       # dict -> dict | Extracts tourney summary

    return task7
