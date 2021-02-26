def reorder_seats_with_btn_first(lst, btn):


    # tests for case 1 where BTN seat is not at the table, eg:
    '''
    Table "3" 9-max Seat #2 is the button
    Seat 3: PokerPete24 (40518.00)
    Seat 4: taoDP (6595.00)
    Seat 5: joeyv (37808.00)
    Seat 6: pking69 (129924.00)
    Seat 7: first shirt (91195.00)
    Seat 9: PotNoodle99912 (47175.00)


    and for

    tests for case 2 where BTN seat is at the table, eg:
    # Table "3" 9-max Seat #4 is the button
    # Seat 3: PokerPete24 (40518.00)
    # Seat 4: taoDP (6595.00)
    # Seat 5: joeyv (37808.00)
    # Seat 6: pking69 (129924.00)
    # Seat 7: first shirt (91195.00)
    # Seat 9: PotNoodle99912 (47175.00)


    and for


    tests for case 2 where BTN seat is not at table and seat 9, eg:
    # Table "3" 9-max Seat #4 is the button
    # Seat 3: PokerPete24 (40518.00)
    # Seat 4: taoDP (6595.00)
    # Seat 5: joeyv (37808.00)
    # Seat 6: pking69 (129924.00)
    # Seat 7: first shirt (91195.00)
    '''

    while any("Seat "+str(btn)+":" in word for word in lst) is False:
        btn = btn + 1
        if btn == 10:
            btn = 1

    for idx, elem in enumerate(lst):
        if 'Seat ' + str(btn) + ':' in elem:
            slicing_index = idx
            return lst[slicing_index:] + lst[:slicing_index]


#
# wdwd = ['Seat 3: PokerPete24 (39018.00)',
#         'Seat 4: taoDP (6895.00)',
#         'Seat 5: joeyv (38108.00)',
#         'Seat 6: pking69 (130224.00)',
#         'Seat 7: first shirt (91495.00)',
#         'Seat 9: PotNoodle99912 (47475.00)']
#
# print(recreate_ordered_list(wdwd, 9))