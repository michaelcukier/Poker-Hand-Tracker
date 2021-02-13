
def board_cards(hand_txt: str) -> str:
    """
    Extracts the board cards from a single hand history

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    board_cards (str): the board cards
    """

    for line in hand_txt.split('\n'):
        if 'Board [' in line:
            return line.replace('Board [', '').replace(']', '')
    return 'no-board'
