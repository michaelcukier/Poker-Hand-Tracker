from datetime import datetime
from import_new_tournaments.process_hh_files.process.hands.Hand.Hand import Hand


def elapsed_time(first_hand: Hand, last_hand: Hand) -> int:
    """
    Extracts the entire time spent on a tournament

            Parameters:
                    first_hand (Hand): the first hand of the tournament (by time)
                    last_hand (Hand): the last hand of the tournament (by time)

            Returns:
                    entire_time (int): the time spent
    """

    last_hand_time = datetime.strptime(last_hand.time.replace('/', '-'), '%Y-%m-%d %H:%M:%S UTC')
    first_hand_time = datetime.strptime(first_hand.time.replace('/', '-'), '%Y-%m-%d %H:%M:%S UTC')

    duration = last_hand_time - first_hand_time
    duration_in_mn = duration.total_seconds()/60

    entire_time = round(duration_in_mn)

    return entire_time
