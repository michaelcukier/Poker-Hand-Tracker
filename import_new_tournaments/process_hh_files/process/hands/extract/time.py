
def time(hand_txt: str) -> str:
    """
    Extracts the time when a hand starts

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    hand_time (str): time in H:M:S UTC format
    """
    hand_time = '202' + hand_txt.split('\n')[0].split(')- 202')[1]
    return hand_time
