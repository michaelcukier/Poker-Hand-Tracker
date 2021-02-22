



from holdem_calc import calculate

print(calculate(
    board=["9h", "8s", "5h", "2d", "3c"],
    exact=False,
    num=5000,
    input_file=None,
    hole_cards=["9d", "6d", "?", "?"],
    verbose=True
))


print('---------')

print(calculate(
    board=["9h", "8s", "5h", "2d", "3c"],
    exact=True,
    num=5000,
    input_file=None,
    hole_cards=["Td", "9d", "?", "?"],
    verbose=True
))

print('---------')

print(calculate(
    board=["9h", "8s", "5h", "2d", "3c"],
    exact=False,
    num=5000,
    input_file=None,
    hole_cards=["Jd", "8d", "?", "?"],
    verbose=True
))