def get_id(hand_txt: str) -> int:
    """
    Extracts the unique ID of a hand

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    id (int): the board cards
    """

    for line in hand_txt.split('\n'):
        if 'Game Hand #' in line:
            return int(line.split('Game Hand #')[1].split(' - ')[0])
