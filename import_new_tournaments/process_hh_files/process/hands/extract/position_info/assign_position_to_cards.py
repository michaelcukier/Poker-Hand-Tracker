from GLOBAL_VARIABLES import PLAYER_NAME
from ..my_cards import my_cards


def assign_position_to_cards(hand_txt: str, positions_and_stack: dict) -> dict:
    for pos, val in positions_and_stack.items():
        player_name = val['Name']
        if player_name is None:
            pass
        elif player_name == PLAYER_NAME:
            positions_and_stack[pos]['Cards'] = my_cards(hand_txt)
        else:
            for line in hand_txt.split('\n'):
                if (player_name in line) and ('showed' in line):
                    cards = line.split('showed [')[1].split('] and')[0]
                    positions_and_stack[pos]['Cards'] = cards
    return positions_and_stack
