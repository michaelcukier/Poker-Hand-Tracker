
def board_cards(hand_txt):
    for line in hand_txt.split('\n'):
        if 'Board [' in line:
            return line.replace('Board [', '').replace(']', '')
    return 'no-board'
