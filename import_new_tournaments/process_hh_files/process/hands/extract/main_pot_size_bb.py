from .side_pot_n_winner import side_pot_n_winner
from .main_pot_winner import main_pot_winner


def main_pot_size_bb(hand_txt: str) -> float:

    """
    Extracts the main pot size of a hand.

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    pot_size (float): the pot size in big blinds
    """

    current_level_big_blind = float(str(hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]).split('/')[1].replace(')', ''))

    # if just one main pot:
    if side_pot_n_winner(hand_txt, n=1) == None:
        for line in hand_txt.split('\n'):
            if ' did not show and won ' in line:
                pot_size_chips = int(line.split(' did not show and won ')[1].split('.')[0])
                return round(pot_size_chips / current_level_big_blind, 2)
            elif '] and won ' in line:
                pot_size_chips = int(line.split('] and won ')[1].split(' with ')[0].split('.')[0])
                return round(pot_size_chips / current_level_big_blind, 2)
    else:
        # if winner wins side + main
        if main_pot_winner(hand_txt) == side_pot_n_winner(hand_txt, n=1):
            for line in hand_txt.split('\n'):
                if 'Total pot ' in line:
                    pot_size_chips = int(line.split('Total pot ')[1].split('.')[0])
                    return round(pot_size_chips / current_level_big_blind, 2)

        # if winner wins only main
        for line in hand_txt.split('\n'):
            if '.00 from main pot' in line:
                pot_size_chips = int(line.split('.00 from main pot')[0].split('collected ')[1])
                return round(pot_size_chips / current_level_big_blind, 2)

