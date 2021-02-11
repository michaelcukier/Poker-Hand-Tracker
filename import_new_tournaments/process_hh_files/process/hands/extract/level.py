
def level(hand_txt):
    return hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]
