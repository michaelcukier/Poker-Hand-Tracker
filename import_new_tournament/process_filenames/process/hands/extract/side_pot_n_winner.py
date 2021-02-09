
def side_pot_n_winner(hand, n):
    for line in hand.split('\n'):
        if ('side pot-' + str(n)) in line:
            return line.split(' collected')[0]
    return None
