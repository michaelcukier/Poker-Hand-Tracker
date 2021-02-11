def main_pot_winner(hand_txt: str) -> str:

    # side pots
    if 'side pot-1' in str(hand_txt):
        for line in hand_txt.split('\n'):
            if 'main pot' in line:
                return line.split(' collected')[0]

    # chop pot
    if str(hand_txt).count('from main pot') >= 2:
        return '**[CHOP-CHOP]**'

    # normal main pot
    for line in hand_txt.split('\n'):
        if 'and won' in line:
            if 'did not' in line:
                return line.split(' did not ')[0].split(': ')[1]
            elif 'showed' in line:
                return line.split(' showed ')[0].split(': ')[1].split(' (')[0]
