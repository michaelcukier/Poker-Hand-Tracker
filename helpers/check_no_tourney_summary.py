def check_no_tourney_summary(sum: dict):
    try:
        if sum['no-tourney-summary']:
            return True
    except KeyError:
        return False