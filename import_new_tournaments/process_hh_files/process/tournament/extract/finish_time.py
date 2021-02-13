from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand


def finish_time(last_hand: Hand) -> str:
    """
    Extracts the time when the tournament finished

            Parameters:
                    last_hand (Hand): the last hand of the tournament (by time)

            Returns:
                    time (int): the last hand's time
    """
    return last_hand.time
