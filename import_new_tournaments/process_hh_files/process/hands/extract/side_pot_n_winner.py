
def side_pot_n_winner(hand_txt: str, n: int) -> str or None:
    """
    Extracts the 2 hole cards received

            Parameters:
                    hand_txt (int): a hand history
                    n (int): the side pot number

            Returns:
                    winner (float) or None: the name of the winner of the pot
    """

    for line in hand_txt.split('\n'):
        if ('side pot-' + str(n)) in line:
            winner = line.split(' collected')[0]
            return winner
    return None
