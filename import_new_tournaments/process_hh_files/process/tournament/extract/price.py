from GLOBAL_VARIABLES import TOURNAMENTS_TO_EXTRACT


def price(title: str) -> float:
    """
    Extracts the buyin amount from the title

            Parameters:
                    title (str): the name of the tournament hand history file

            Returns:
                    price (float): the entry price of the tournament
    """

    for tourney_to_extract, price in TOURNAMENTS_TO_EXTRACT.items():
        if tourney_to_extract in title:
            return price
