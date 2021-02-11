from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand


def finish_time(last_hand: Hand) -> str:
    return last_hand.time
