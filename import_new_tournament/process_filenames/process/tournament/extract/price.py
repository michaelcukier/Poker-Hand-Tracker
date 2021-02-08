from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT


def price(title: str) -> float:
    # extracts the buyin amount
    # from the title
    for tourney_to_extract, price in TOURNAMENTS_TO_EXTRACT.items():
        if tourney_to_extract in title:
            return price
