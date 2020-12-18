from os import listdir
from os.path import isfile, join
import copy
from helpers.run_sql_command import run_sql_command

mypath_hh = '/Users/cukiermichael/Downloads/AmericasCardroom/handHistory/PotNoodle99912'
mypath_sum = '/Users/cukiermichael/Downloads/AmericasCardroom/handHistory/PotNoodle99912'


def task_1() -> list:
    # get all current ids from db
    return run_sql_command('SELECT ID FROM tournaments', unique_items=True)


def task_2() -> list:
    # get all filenames in folder
    files = [f for f in listdir(mypath_hh) if isfile(join(mypath_hh, f))]
    return files


def task_3(filenames: list) -> list:
    # filter the files to get only the ones needed
    filtered = []
    for file_name in filenames:
        if "$0{FULLSTOP}50 Hold'Em Turbo" in file_name:
            filtered.append(file_name)
    return filtered


def task_4(filenames: list, ids_already_in_db: list) -> list:
    # remove duplicates between filenames already in db and new ones
    filtered = []
    for file_name in filenames:
        if file_name not in ids_already_in_db:
            filtered.append(file_name)
    return filtered

def extract_id_from_content(content: str) -> int:
    return int(content.split('\n')[0].split('Tournament ')[1][1:9])


def task_5(filenames: list) -> list:
    # add tournaments summary from tournament
    # id and return clean dict: [{title: <>, raw_hh: <>, summary: <>}, {...}]
    filtered = []
    for file_name in filenames:
        f = open(mypath_hh + '/' + file_name, "r")
        hhtext = copy.deepcopy(f.read())

        id = extract_id_from_content(hhtext)
        summary_file_name = [f for f in listdir(mypath_hh) if str(id) in f][0]
        sum = open(mypath_sum + '/' + summary_file_name, "r")
        hhsum = eval(copy.deepcopy(sum.read()))

        filtered.append({
            'title': file_name,
            'content': hhtext,
            'summary': hhsum
        })
    return filtered


# ------


def get_new_raw_hh_from_file() -> list:
    '''
    this function performs tasks to return
    the new hand histories
    :return:
    [{
        'title': str,
        'content': str,
        'summary': str
    }, {
        ...
    ]}
    '''
    current_ids_in_db = task_1()
    current_filenames_in_folder = task_2()
    filter_filenames_in_folder = task_3(current_filenames_in_folder)
    remove_filenames_already_in_db = task_4(filter_filenames_in_folder, current_ids_in_db)
    new_hhs = task_5(remove_filenames_already_in_db)

    return new_hhs