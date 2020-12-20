from .new_hands import get_hands_info
from .new_opponents import extract_opponents_names
from .new_tournaments import extract_new_tournament

# ------


def run(raw_hh: dict) -> list:
    extraction = []
    for tourney_id, hh in raw_hh.items():
        extraction.append({
            'new_tournament': extract_new_tournament(hh['title'], hh['hands'], hh['summary']),
            'new_hands': get_hands_info(hh['hands']),
            'new_opponents': extract_opponents_names(hh['summary'])
        })
    return extraction