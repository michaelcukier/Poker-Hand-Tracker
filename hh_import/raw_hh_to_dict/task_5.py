from GLOBAL_VARIABLES import HAND_HISTORY_FOLDER
import copy


def task_5(filenames: dict) -> dict:
    for tourney_id, value in filenames.items():
        hands = []
        for filename in value['filenames']:
            # open current filename
            f = open(HAND_HISTORY_FOLDER + '/' + filename, "r")
            hhtext = copy.deepcopy(f.read())
            # split the hands into a list
            str_to_hands = hhtext.split('\n\n')
            for hand_ in str_to_hands:
                hands.append(hand_)
            del hands[-1]
        filenames[tourney_id] = {'title': value['filenames'][0], 'hands': hands}
    return filenames
