def extract_name_from_seat_line(seat_line: str) -> str or None:
    # Seat 3: PokerPete24 (40518.00)

    # also

    # Seat 3: joeyv will be allowed to play after the button

    if 'will be allowed to play after the button' in seat_line:
        return None
    return seat_line.split(': ')[1].split(' (')[0]