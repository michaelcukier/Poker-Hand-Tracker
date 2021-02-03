

def extract_nb_of_participants(tourney_summary: dict):
    def check_no_tourney_summary(sum):
        if sum is None:
            return True
        return False

    if check_no_tourney_summary(tourney_summary):
        return None
    return tourney_summary['player_count']