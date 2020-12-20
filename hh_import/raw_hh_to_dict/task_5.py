from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER
import copy


def task_5(filenames: dict, custom_folder=False) -> dict:
    for tourney_id, value in filenames.items():
        hands = []
        for filename in value['filenames']:
            # open current filename
            with open((custom_folder if custom_folder else HAND_HISTORY_FOLDER) + '/' + filename, 'r') as f:
                data = f.read()
                hhtext = copy.deepcopy(data)
            # split the hands into a list
            str_to_hands = hhtext.split('\n\n')
            for hand_ in str_to_hands:
                hands.append(hand_)
            del hands[-1]
        filenames[tourney_id] = {'title': value['filenames'][0], 'hands': hands}
    return filenames
