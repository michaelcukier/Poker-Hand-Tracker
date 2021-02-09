
def get_id(hand: str) -> int:
    for line in hand.split('\n'):
        if 'Game Hand #' in line:
            return int(line.split('Game Hand #')[1].split(' - ')[0])
