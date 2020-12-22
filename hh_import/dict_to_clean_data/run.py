from .new_hands import get_hands_info
from .new_opponents import extract_opponents_names
from .new_tournaments import extract_new_tournament

# ------


def run(raw_hh: dict, log_progress=False) -> list:
    extraction = []
    idx = 0
    for tourney_id, hh in raw_hh.items():
        idx += 1
        if log_progress:
            print("Getting [", tourney_id, "]'s data...", str(idx) + '/' + str(len(raw_hh.items())))
        extraction.append({
            'new_tournament': extract_new_tournament(hh['title'], hh['hands'], hh['summary']),
            'new_hands': get_hands_info(hh['hands']),
            'new_opponents': extract_opponents_names(hh['summary'])
        })






        # # early stop for test
        # if idx == 10:
        #     return extraction
        # # early stop for test




    return extraction