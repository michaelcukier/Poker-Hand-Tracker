def get_btn_position_nb(hand):
    btn_seat_nb = hand.split('\n')[1]  # Table "1" 9-max Seat #6 is the button
    btn_seat_nb = btn_seat_nb.split('Seat #')[1]  # 6 is the button
    btn_seat_nb = int(btn_seat_nb.split(' is the button')[0])  # 6
    return btn_seat_nb
