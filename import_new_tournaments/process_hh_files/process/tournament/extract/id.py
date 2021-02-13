from utils.extract_id_from_title import extract_id_from_title


def get_id(title: str) -> int:
    """
    Extracts the time when the tournament finished

            Parameters:
                    hands (title): the title of the tournament's hand history filename

            Returns:
                    id (list): the tournament ID
    """
    return extract_id_from_title(title)
