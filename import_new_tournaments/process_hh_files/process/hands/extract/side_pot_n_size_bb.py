from .level import level


def side_pot_n_size_bb(hand_txt: str, n: int) -> float:
    """
    Extracts the 2 hole cards received

            Parameters:
                    hand_txt (int): a hand history
                    n (int): the side pot number

            Returns:
                    size (float): the pot size amount in big blinds
    """

    current_level_big_blind = float(str(level(hand_txt)).split('/')[1].replace(')', ''))
    for line in hand_txt.split('\n'):
        if ('from side pot-' + str(n)) in line:
            pot_size_chips = int(line.split(' collected ')[1].split('.00 from side pot-' + str(n))[0])
            size = round(pot_size_chips / current_level_big_blind, 2)
            return size
    return 0
