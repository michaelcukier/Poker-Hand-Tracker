def nb_occupied_seats(hand_txt: str) -> int:
    """
    Extracts the number of occupied seats at the table

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    out (int): the nb of occupied seats
    """
    out = 0
    lines = hand_txt.split('\n')[2:]
    for l in lines:
        if 'Seat' in l:
            out += 1
        else:
            break
    return out