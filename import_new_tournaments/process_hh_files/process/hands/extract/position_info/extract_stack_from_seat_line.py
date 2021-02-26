def extract_stack_from_seat_line(seat_line: str) -> float or None:
    # Seat 3: PokerPete24 (40518.00)

    if 'will be allowed to play after the button' in seat_line:
        return None
    return float(seat_line.split(' (')[1].split(')')[0])
