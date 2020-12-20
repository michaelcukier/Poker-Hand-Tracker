from helpers.extract_id_from_title import extract_id_from_title


def order_filenames(filenames):
    a = sorted(filenames, key=lambda x: str(x[29]))
    return a


def task_4(filenames: list) -> dict:
    '''
    group remaining filenames and create a dict: {tourney_ID: [filename1, filename2, ...]}
    '''

    filenames_ = order_filenames(filenames)
    hhs = {}
    for file_name in filenames_:
        id = extract_id_from_title(file_name)
        if id not in hhs:
            hhs[id] = {'filenames': []}
        hhs[id]['filenames'].append(file_name)

    return hhs
