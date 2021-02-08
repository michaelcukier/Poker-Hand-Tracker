
def tournament_id(hand_txt):
    for line in hand_txt.split('\n'):
        if 'Tournament #' in line:
            return int(line.split('Tournament #')[1].split(' - ')[0])
