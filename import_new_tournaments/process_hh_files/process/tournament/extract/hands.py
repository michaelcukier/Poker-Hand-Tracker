from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand


def hands(hands: list) -> list:
    """
    Extracts the time when the tournament finished

            Parameters:
                    hands (list): list of raw hand history text

            Returns:
                    processed_hands (list): list of Hands classes
    """
    processed_hands = []
    for h in hands:
        new_hand = Hand(hand_txt=h)
        new_hand.build_hand()
        processed_hands.append(new_hand)
    return processed_hands
