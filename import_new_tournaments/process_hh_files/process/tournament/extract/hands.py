
from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand


def hands(hands: list) -> list:
    processed_hands = []
    for h in hands:
        new_hand = Hand(hand_txt=h)
        new_hand.build_hand()
        processed_hands.append(new_hand)
    return processed_hands
