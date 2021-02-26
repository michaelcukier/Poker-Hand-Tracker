def extract_name_from_seat_line(seat_line: str) -> str:
    # Seat 3: PokerPete24 (40518.00)

    return seat_line.split(': ')[1].split(' (')[0]