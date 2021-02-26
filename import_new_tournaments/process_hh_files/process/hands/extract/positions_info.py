from .position_info.get_btn_position_nb import get_btn_position_nb
from .position_info.get_seats_and_nb_of_players import get_seats_and_nb_of_players
from .position_info.reorder_seats_with_btn_first import reorder_seats_with_btn_first
from .position_info.assign_position_to_name_and_stack import assign_position_to_name_and_stack
from .position_info.assign_position_to_cards import assign_position_to_cards


def position_info(hand_txt: str) -> dict:
    """
    Extracts player information (his name, stack & position)
    and assigns it to his position at the table

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    position_info (dict): key is position and value are the info retrieved
    """

    # step 1 - get seats in list & nb of players
    all_seats = get_seats_and_nb_of_players(
        hand=hand_txt)

    # step 2 - get btn position
    btn_position = get_btn_position_nb(
        hand=hand_txt)

    # step 3 - order list seats list with btn first
    seats_list_with_btn_first = reorder_seats_with_btn_first(
        lst=all_seats['lst'],
        btn=btn_position)

    # step 4 - assign position to name & stack
    positions_and_stacks = assign_position_to_name_and_stack(
        seats=seats_list_with_btn_first,
        nb_of_players=all_seats['nb_of_players'])

    # step 5 - assign cards if showdown
    positions_info = assign_position_to_cards(
        hand_txt=hand_txt,
        positions_and_stack=positions_and_stacks)

    return positions_info
