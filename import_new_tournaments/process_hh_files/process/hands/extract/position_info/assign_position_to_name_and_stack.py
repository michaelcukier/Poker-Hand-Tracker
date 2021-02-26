from .extract_name_from_seat_line import extract_name_from_seat_line
from .extract_stack_from_seat_line import extract_stack_from_seat_line


def assign_position_to_name_and_stack(seats: list, nb_of_players: int) -> dict:
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
        '2-max': {0: 'SB', 1: 'BB'},
        '3-max': {0: 'BTN', 1: 'SB', 2: 'BB'},
        '4-max': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'CO'},
        '5-max': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'CO'},
        '6-max': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'MP', 5: 'CO'},
        '7-max': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'UTG+1', 5: 'MP', 6: 'CO'},
        '8-max': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'UTG+1', 5: 'MP', 6: 'MP+1', 7: 'CO'},
        '9-max': {0: 'BTN', 1: 'SB', 2: 'BB', 3: 'UTG', 4: 'UTG+1', 5: 'MP', 6: 'MP+1', 7: 'MP+2', 8: 'CO'}
    }
    for idx, elem in enumerate(seats):
        posName = PositionIndexes[str(nb_of_players) + '-max'][idx]
        empty_position_and_player[posName]['Name'] = extract_name_from_seat_line(elem)
        empty_position_and_player[posName]['Stack'] = extract_stack_from_seat_line(elem)
    return empty_position_and_player
