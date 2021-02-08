
def side_pot_n_winner(hand, n):
    # if side pot winner = main pot winner
    for line in hand.split('\n'):
        if ('side pot-' + str(n)) in line:
            return line.split(' collected')[0]
    return 'no-side-pot'

#
# def get_side_pot_1_winner(hand_txt: str) -> str:
#     return side_pot_n_winner(hand_txt, n=1)
#
# def get_side_pot_2_winner(hand_txt: str) -> str:
#     return side_pot_n_winner(hand_txt, n=2)
#
# def get_side_pot_3_winner(hand_txt: str) -> str:
#     return side_pot_n_winner(hand_txt, n=3)