def extract_name_from_seat_line(seat_line: str) -> str:
    return seat_line.split(': ')[1].split(' (')[0]


def recreate_ordered_list(lst, btn):
    for idx, elem in enumerate(lst):
        if 'Seat ' + str(btn) + ':' in elem:
            slicing_index = idx
            return lst[slicing_index:] + lst[:slicing_index]


def assign_idx_to_pos(lst, nb_of_players):
    empty_position_and_player = {
        'BTN': None, 'SB': None, 'BB': None, 'UTG': None, 'UTG+1': None,
        'MP': None, 'MP+1': None, 'MP+2': None, 'CO': None}
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
        empty_position_and_player[posName] = extract_name_from_seat_line(elem)
    return empty_position_and_player


def get_seats_and_nb_of_players(hand) -> dict:
    # extract seats and number of players
    seats_lines = []
    for l in hand.split('\n')[2:]:
        if 'Seat' in l:
            seats_lines.append(l)
        else:
            break
    return {'lst': seats_lines, 'nb_of_players': len(seats_lines)}


def get_btn_position_nb(hand):
    btn_seat_nb = hand.split('\n')[1]  # Table "1" 9-max Seat #6 is the button
    btn_seat_nb = btn_seat_nb.split('Seat #')[1]  # 6 is the button
    btn_seat_nb = int(btn_seat_nb.split(' is the button')[0])  # 6
    return btn_seat_nb


def position_player_name(hand_txt: str) -> dict:
    """
    Extracts the player name and his position

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    position_and_player (dict): each position and the corresponding player name
    """

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

    # step 4 - assign indexes to position depending on nb players
    position_and_player = assign_idx_to_pos(
        lst=btn_first,
        nb_of_players=all_seats['nb_of_players'])

    return position_and_player












