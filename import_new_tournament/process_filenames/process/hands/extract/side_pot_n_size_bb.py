
from .level import level


def side_pot_n_size_bb(hand, n):
    current_level_big_blind = float(str(level(hand)).split('/')[1].replace(')', ''))
    for line in hand.split('\n'):
        if ('from side pot-' + str(n)) in line:
            pot_size_chips = int(line.split(' collected ')[1].split('.00 from side pot-' + str(n))[0])
            return round(pot_size_chips / current_level_big_blind, 2)
    return 0
