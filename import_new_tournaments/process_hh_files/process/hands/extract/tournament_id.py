
def tournament_id(hand_txt: str) -> int:
    """
    Extracts the tournament ID from a hand

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    t_id (str): tournament ID
    """
    for line in hand_txt.split('\n'):
        if 'Tournament #' in line:
            t_id = int(line.split('Tournament #')[1].split(' - ')[0])
            return t_id
