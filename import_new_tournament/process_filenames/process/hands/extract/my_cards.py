
from GLOBAL_VARIABLES import PLAYER_NAME


def my_cards(hand_txt):
    for line in hand_txt.split('\n'):
        if 'Dealt to ' + PLAYER_NAME + ' [' in line:
            return line.replace('Dealt to ' + PLAYER_NAME + ' [', '').replace(']', '')
