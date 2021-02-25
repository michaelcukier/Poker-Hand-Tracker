def recreate_ordered_list(lst, btn):
    for idx, elem in enumerate(lst):
        if 'Seat ' + str(btn) + ':' in elem:
            slicing_index = idx
            return lst[slicing_index:] + lst[:slicing_index]
