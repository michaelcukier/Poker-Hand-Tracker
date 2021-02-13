
def level(hand_txt: str) -> str:
    """
    Extracts the blind level of a hand

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    level (int): the blind level
    """
    return hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]
