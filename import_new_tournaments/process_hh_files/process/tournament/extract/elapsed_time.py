from datetime import datetime
from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand


def elapsed_time(first_hand: Hand, last_hand: Hand) -> int:

    last_hand_time = datetime.strptime(last_hand.time.replace('/', '-'), '%Y-%m-%d %H:%M:%S UTC')
    first_hand_time = datetime.strptime(first_hand.time.replace('/', '-'), '%Y-%m-%d %H:%M:%S UTC')

    duration = last_hand_time - first_hand_time
    duration_in_mn = duration.total_seconds()/60

    return round(duration_in_mn)
