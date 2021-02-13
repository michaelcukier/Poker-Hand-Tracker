from GLOBAL_VARIABLES import PLAYER_NAME


def starting_stack_size_bb(hand_txt: str) -> float:
    """
    Extracts the 2 hole cards received

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    size (float): the size of the starting stack size in bb
    """

    current_level_big_blind = float(str(hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]).split('/')[1].replace(')', ''))
    for line in hand_txt.split('\n'):
        if PLAYER_NAME + ' (' in line:
            size = round(int(line.split(PLAYER_NAME + ' (')[1].split('.')[0])/current_level_big_blind, 1)
            return size
