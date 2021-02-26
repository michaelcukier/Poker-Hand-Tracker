def reorder_seats_with_btn_first(lst, btn):
    while any("Seat "+str(btn)+":" in word for word in lst) is False:
        btn = btn + 1
        if btn == 10:
            btn = 1

    for idx, elem in enumerate(lst):
        if 'Seat ' + str(btn) + ':' in elem:
            slicing_index = idx
            return lst[slicing_index:] + lst[:slicing_index]
