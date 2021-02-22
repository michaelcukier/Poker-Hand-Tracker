from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand
import copy
from GLOBAL_VARIABLES import PLAYER_NAME

def get_hands_in_list(parent_folder, hand_history_filenames):
    def order_hands_by_time(hands):
        a = sorted(hands, key=lambda x: '20' + str(x.split('\n')[0].split('- 20')[1]))
        return a
    hands = []
    for filename in hand_history_filenames:
        # open current filename
        with open(parent_folder + '/' + filename, 'r') as f:
            data = f.read()
            hhtext = copy.deepcopy(data)
        # split the hands into a list
        str_to_hands = hhtext.split('\n\n')
        for hand_ in str_to_hands:
            hands.append(hand_)
        del hands[-1]
    # order hands by time
    hands_t = order_hands_by_time(hands)
    return hands_t


def remove_hands_player_not_playing(hands: list) -> list:
    for h in hands:
        if PLAYER_NAME + ' will be allowed to play after the button' in h:
            hands.remove(h)
    return hands


def process_hands(hands: list) -> list:
    """
    Creates the Hand classes for each hand history

            Parameters:
                    hands (list): list of raw hand history text

            Returns:
                    processed_hands (list): list of Hand classes
    """
    processed_hands = []
    for h in hands:
        new_hand = Hand(hand_txt=h)
        new_hand.build_hand()
        processed_hands.append(new_hand)
    return processed_hands

