# import copy
#
#
# def get_hands_in_list(parent_folder, hand_history_filenames):
#     def order_hands_by_time(hands):
#         a = sorted(hands, key=lambda x: '20' + str(x.split('\n')[0].split('- 20')[1]))
#         return a
#     hands = []
#     for filename in hand_history_filenames:
#         # open current filename
#         with open(parent_folder + '/' + filename, 'r') as f:
#             data = f.read()
#             hhtext = copy.deepcopy(data)
#         # split the hands into a list
#         str_to_hands = hhtext.split('\n\n')
#         for hand_ in str_to_hands:
#             hands.append(hand_)
#         del hands[-1]
#     # order hands by time
#     hands_t = order_hands_by_time(hands)
#     return hands_t
