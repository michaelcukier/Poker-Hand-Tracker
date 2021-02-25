from .position_utils.get_btn_position_nb import get_btn_position_nb
from .position_utils.get_seats_and_nb_of_players import get_seats_and_nb_of_players
from .position_utils.recreate_ordered_list import recreate_ordered_list
from GLOBAL_VARIABLES import PLAYER_NAME
from .my_cards import my_cards


def position_player_name(hand_txt: str) -> dict:
    """
    Extracts the player name and his position

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    position_and_player (dict): each position and the corresponding player name
    """

    def extract_name_from_seat_line(seat_line: str) -> str:
        return seat_line.split(': ')[1].split(' (')[0]

    def extract_stack_from_seat_line(seat_line: str) -> float or None:
        if 'will be allowed to play after the button' in seat_line:
            return None
        return float(seat_line.split(' (')[1].split(')')[0])

    def extract_cards(hand_txt: str, positions_and_stack: dict) -> dict:
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

    def assign_idx_to_pos(lst, nb_of_players):
        empty_position_and_player = {
            'BTN': {'Name': None, 'Stack': None, 'Cards': None},
            'SB': {'Name': None, 'Stack': None, 'Cards': None},
            'BB': {'Name': None, 'Stack': None, 'Cards': None},
            'UTG': {'Name': None, 'Stack': None, 'Cards': None},
            'UTG+1': {'Name': None, 'Stack': None, 'Cards': None},
            'MP': {'Name': None, 'Stack': None, 'Cards': None},
            'MP+1': {'Name': None, 'Stack': None, 'Cards': None},
            'MP+2': {'Name': None, 'Stack': None, 'Cards': None},
            'CO': {'Name': None, 'Stack': None, 'Cards': None}}

        PositionIndexes = {
            'max2': {0: 'SB', 1: 'BB'},
            'max3': {0: 'BTN', 1: 'SB', 2: 'BB'},
            'max4': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'CO'},
            'max5': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'CO'},
            'max6': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'MP', 5: 'CO'},
            'max7': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'UTG+1', 5: 'MP', 6: 'CO'},
            'max8': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'UTG+1', 5: 'MP', 6: 'MP+1', 7: 'CO'},
            'max9': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'UTG+1', 5: 'MP', 6: 'MP+1', 7: 'MP+2', 8: 'CO'}
        }
        for idx, elem in enumerate(lst):
            posName = PositionIndexes['max' + str(nb_of_players)][idx]
            empty_position_and_player[posName]['Name'] = extract_name_from_seat_line(elem)
            empty_position_and_player[posName]['Stack'] = extract_stack_from_seat_line(elem)
        return empty_position_and_player

    # step 1 - get seats in list & nb of players
    all_seats = get_seats_and_nb_of_players(
        hand=hand_txt)

    # step 2 - get btn position
    btn_position = get_btn_position_nb(
        hand=hand_txt)

    # step 3 - order list seats list with btn first
    btn_first = recreate_ordered_list(
        lst=all_seats['lst'],
        btn=btn_position)

    # step 4 - assign indexes to position
    positions_and_stacks = assign_idx_to_pos(
        lst=btn_first,
        nb_of_players=all_seats['nb_of_players'])

    # step 5 - assign cards if showdown
    positions_info = extract_cards(
        hand_txt=hand_txt,
        positions_and_stack=positions_and_stacks)

    return positions_info
