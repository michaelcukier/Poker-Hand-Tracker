def get_seats_and_nb_of_players(hand) -> dict:
    # extract seats and number of players
    seats_lines = []
    for l in hand.split('\n')[2:]:
        if 'Seat' in l:
            seats_lines.append(l)
        else:
            break
    return {'lst': seats_lines, 'nb_of_players': len(seats_lines)}
