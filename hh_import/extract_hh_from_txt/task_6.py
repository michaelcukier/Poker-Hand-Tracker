from GLOBAL_VARIABLES import PLAYER_NAME


def task_6(tourneys: dict) -> dict:
    # remove hands where I'm not playing
    for tourney_id, value in tourneys.items():
        for i, hand in enumerate(value['hands']):
            if PLAYER_NAME + ' will be allowed to play after the button' in hand:
                tourneys[tourney_id]['hands'].remove(hand)
    return tourneys
