from .new_hands import extract_hands_from_content
from .new_opponents import extract_opponents_names
from .new_tournaments import * # CHANGE THISSSSS !!!!!!!!!!! INCONSISTENT

# ------


def extract_from_raw_hh(raw_hh: list) -> list:
    extraction = []
    for hh in raw_hh:
        extraction.append({
            'new_tournament': {   #2@@@@@@@ CHANGE THISSSSS !!!!!!!!!!! INCONSISTENT
                'id': extract_id_from_content(hh['content']),
                'price': extract_price_from_title(hh['title']),
                'finished_time': extract_finished_time_from_content(hh['content']),
                'elapsed_time': extract_elapsed_time_from_content(hh['content']),
                'prize': extract_prize(hh['tourney_summary']),
                'position': extract_position(hh['tourney_summary'])
            },
            'new_hands': extract_hands_from_content(hh['content']),
            'new_opponents': extract_opponents_names(hh['tourney_summary'])
        })
    return extraction
