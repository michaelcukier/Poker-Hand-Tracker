
from GLOBAL_VARIABLES import PLAYER_NAME


def my_cards(hand_txt: str):
    """
    Extracts the 2 hole cards received

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    cards (str): the hole 2 cards
    """

    for line in hand_txt.split('\n'):
        if 'Dealt to ' + PLAYER_NAME + ' [' in line:
            cards = line.replace('Dealt to ' + PLAYER_NAME + ' [', '').replace(']', '')
            return cards
