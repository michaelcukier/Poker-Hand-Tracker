def main_pot_winner(hand_txt: str) -> str:
    """
    Extracts the name of the main pot winner

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    winner (str): name of main pot winner
                    or '**[CHOP-CHOP]**' when it's a chop
    """

    # side pots
    if 'side pot-1' in str(hand_txt):
        for line in hand_txt.split('\n'):
            if 'main pot' in line:
                winner = line.split(' collected')[0]
                return winner

    # chop pot
    if str(hand_txt).count('from main pot') >= 2:
        winner = '**[CHOP-CHOP]**'
        return winner

    # normal main pot
    for line in hand_txt.split('\n'):
        if 'and won' in line:
            if 'did not' in line:
                winner = line.split(' did not ')[0].split(': ')[1]
                return winner
            elif 'showed' in line:
                winner = line.split(' showed ')[0].split(': ')[1].split(' (')[0]
                return winner
