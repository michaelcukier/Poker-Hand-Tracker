def table_type(hand_txt: str) -> str:
    """
    Extracts the table type (for ex: 6-max)

            Parameters:
                    hand_txt (int): a hand history

            Returns:
                    table_type (str): the table type
    """

    line = hand_txt.split('\n')[1]  # = Table "1" 9-max Seat #6 is the button
    line = line.split('Table "')[1]   # = 1" 9-max Seat #6 is the button
    line = line.split('" ')[1]  # = 9-max Seat #6 is the button
    table_type = line.split(" Seat")[0]  # = 9-max
    return table_type
