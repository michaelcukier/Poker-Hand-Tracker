from .new_hands import extract_hands_from_content
from .new_opponents import extract_opponents_names
from .new_tournaments import extract_new_tournament

# ------


def extract_from_raw_hh(raw_hh: list) -> list:
    extraction = []
    for hh in raw_hh:
        extraction.append({
            'new_tournament': extract_new_tournament(hh['title'], hh['content'], hh['tourney_summary']),
            'new_hands': extract_hands_from_content(hh['content']),
            'new_opponents': extract_opponents_names(hh['tourney_summary'])
        })
    return extraction
