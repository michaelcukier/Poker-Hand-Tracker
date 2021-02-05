import requests

from GLOBAL_VARIABLES import PLAYER_NAME
#
# #
# # def generate_hh_links_replayer(hands):
# #     headers = {
# #         'Connection': 'keep-alive',
# #         'Pragma': 'no-cache',
# #         'Cache-Control': 'no-cache',
# #         'Accept': 'application/json, text/javascript, */*; q=0.01',
# #         'X-Requested-With': 'XMLHttpRequest',
# #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
# #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# #         'Origin': 'https://pokeit.co',
# #         'Sec-Fetch-Site': 'same-origin',
# #         'Sec-Fetch-Mode': 'cors',
# #         'Sec-Fetch-Dest': 'empty',
# #         'Referer': 'https://pokeit.co/convert/',
# #         'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,la;q=0.7',
# #     }
# #
# #     to_send = '\n\n'.join(hands)
# #
# #     data = {
# #         '$filename': '',
# #         'text': to_send,
# #         'format': 'replayer',
# #         'make_public': 'true',
# #         'hide_results': 'false',
# #         'hide_names': 'false',
# #         'embedded': 'false',
# #         'skin': 'pokeit'
# #     }
# #
# #     response = requests.post('http://pokeit.co/convert/hand.php', headers=headers, data=data)
# #
# #     return response.json()['links']
# #
#
# # DELETE THIS ONE, NEVER USED (REPLACED BY TASK 4 IN _____TEMP___extract_hh_from_txt
# # def extract_hands_from_content_to_list(content: str) -> list:
# #     hands = []
# #     for hand in content.split('\n\n'):
# #         if 'PotNoodle99912 will be allowed to play after the button' not in hand:  # avoid hands where im not there
# #             hands.append(hand)
# #     # del hands[-1]
# #     return hands
#
#
#
# import copy
#
#
#
#
# def get_hand_time(hand: str):
#     time = '202' + hand.split('\n')[0].split(')- 202')[1]
#     return time
#
#
# def get_hand_pot_size_chips(hand):
#     for line in hand.split('\n'):
#         if 'Total pot ' in line:
#             return int(line.replace('Total pot ', '').split('.')[0])
#
#
# def get_hand_level(hand):
#     level = hand.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]
#     return level
#
#
# def get_hand_pot_size_bb(hand):
#     current_level_big_blind = float(str(get_hand_level(hand)).split('/')[1].replace(')', ''))
#     return round(get_hand_pot_size_chips(hand)/current_level_big_blind, 1)
#
#
# def get_hand_my_cards(hand):
#     for line in hand.split('\n'):
#         if 'Dealt to ' + PLAYER_NAME + ' [' in line:
#             return line.replace('Dealt to ' + PLAYER_NAME + ' [', '').replace(']', '')
#
#
# def get_hand_board_cards(hand):
#     for line in hand.split('\n'):
#         if 'Board [' in line:
#             return line.replace('Board [', '').replace(']', '')
#     return 'no-board'
#
#
# # def get_tourney_id(hand: str) -> int:
# #     for line in hand.split('\n'):
# #         if 'Tournament #' in line:
# #             return int(line.split('Tournament #')[1].split(' - ')[0])
#
#
#
# # def is_hand_relevant(hand: str) -> bool:
# #     if PLAYER_NAME + ' folded on the Pre-Flop and did not bet' in hand:
# #         return False
# #     if PLAYER_NAME + ' (big blind) folded on the Pre-Flop' in hand:
# #         return False
# #     if PLAYER_NAME + ' (small blind) folded on the Pre-Flop' in hand:
# #         return False
# #     if PLAYER_NAME + ' (button) folded on the Pre-Flop' in hand:
# #         return False
# #     return True
#
#
# # def get_winners_of_hand(hand: str) -> str:
# #     def remove_position_from_name(name: str) -> str:
# #         return name.replace(' (big blind)', '').replace(' (button)', '').replace(' (small blind)', '')
# #
# #     winners = ''
# #     for line in hand.split('\n'):
# #         if 'and won' in line:
# #
# #             # no showdown
# #             if 'did not' in line:
# #                 winners += remove_position_from_name(line.split(' and won ')[0].split(': ')[1].split(' did not')[0]) + ','
# #
# #             # showdown
# #             elif 'showed' in line:
# #                 winners += remove_position_from_name(line.split(' and won ')[0].split(' showed ')[0].split(': ')[1]) + ','
# #
# #     return winners[:-1]
#
# def get_stack_size_start_of_hand(hand):
#     current_level_big_blind = float(str(get_hand_level(hand)).split('/')[1].replace(')', ''))
#     for line in hand.split('\n'):
#         if PLAYER_NAME + ' (' in line:
#             return round(int(line.split(PLAYER_NAME + ' (')[1].split('.')[0])/current_level_big_blind, 1)
#
#
# def get_winner_of_main_pot(hand):
#     # side pots
#     if 'side pot-1' in str(hand):
#         for line in hand.split('\n'):
#             if 'main pot' in line:
#                 return line.split(' collected')[0]
#
#     # chop pot
#     if str(hand).count('from main pot') >= 2:
#         return '**[CHOP-CHOP]**'
#
#     # normal main pot
#     for line in hand.split('\n'):
#         if 'and won' in line:
#             if 'did not' in line:
#                 return line.split(' did not ')[0].split(': ')[1]
#             elif 'showed' in line:
#                 return line.split(' showed ')[0].split(': ')[1].split(' (')[0]
#
#
# #
# #
# # def get_main_pot_size(hand):
# #     current_level_big_blind = float(str(get_hand_level(hand)).split('/')[1].replace(')', ''))
# #
# #     # if just one main pot:
# #     if get_winner_of_side_pot(hand, pot_nb=1) == 'no-side-pot':
# #         for line in hand.split('\n'):
# #             if ' did not show and won ' in line:
# #                 pot_size_chips = int(line.split(' did not show and won ')[1].split('.')[0])
# #                 return round(pot_size_chips/current_level_big_blind, 2)
# #             elif '] and won ' in line:
# #                 pot_size_chips = int(line.split('] and won ')[1].split(' with ')[0].split('.')[0])
# #                 return round(pot_size_chips/current_level_big_blind, 2)
# #     else:
# #         # if winner wins side + main
# #         if get_winner_of_main_pot(hand) == get_winner_of_side_pot(hand, pot_nb=1):
# #             for line in hand.split('\n'):
# #                 if 'Total pot ' in line:
# #                     pot_size_chips = int(line.split('Total pot ')[1].split('.')[0])
# #                     return round(pot_size_chips / current_level_big_blind, 2)
# #
# #         # if winner wins only main
# #         for line in hand.split('\n'):
# #             if '.00 from main pot' in line:
# #                 pot_size_chips = int(line.split('.00 from main pot')[0].split('collected ')[1])
# #                 return round(pot_size_chips / current_level_big_blind, 2)
# #
# #
# # def get_side_pot_size(hand, pot_nb):
# #     current_level_big_blind = float(str(get_hand_level(hand)).split('/')[1].replace(')', ''))
# #     for line in hand.split('\n'):
# #         if ('from side pot-' + str(pot_nb)) in line:
# #             pot_size_chips = int(line.split(' collected ')[1].split('.00 from side pot-' + str(pot_nb))[0])
# #             return round(pot_size_chips / current_level_big_blind, 2)
# #     return 0
# #
#
#
# # def get_hand_type(hand):
# #     def get_hand_preflop_action(hand):
# #         preflop = hand.split('*** FLOP ***')[0].split('*** HOLE CARDS ***')[1].split('*** SUMMARY ***')[0]
# #         return preflop
# #
# #     def get_hand_flop_action(hand):
# #         if '*** FLOP ***' not in hand:
# #             return None
# #         if 'all-in' in get_hand_preflop_action(hand):
# #             return None
# #         else:
# #             flop = hand.split('*** FLOP ***')[1].split('***')[0].split(']')[1].split('\n')
# #             flop_cleaned = ''
# #             for line in flop:
# #                 if line != '':
# #                     flop_cleaned += line + '\n'
# #             return flop_cleaned
# #
# #     def get_hand_turn_action(hand):
# #         if '*** TURN ***' not in hand:
# #             return None
# #         if 'all-in' in get_hand_preflop_action(hand):
# #             return None
# #         else:
# #             flop = hand.split('*** TURN ***')[1].split('***')[0].split('\n')
# #             flop_cleaned = ''
# #             for line in flop:
# #                 if (line != '') and ('] [' not in line):
# #                     flop_cleaned += line + '\n'
# #             return flop_cleaned
# #
# #     def get_hand_river_action(hand):
# #         if '*** RIVER ***' not in hand:
# #             return None
# #         if 'all-in' in get_hand_preflop_action(hand):
# #             return None
# #         else:
# #             flop = hand.split('*** RIVER ***')[1].split('***')[0].split('\n')
# #             flop_cleaned = ''
# #             for line in flop:
# #                 if (line != '') and ('] [' not in line):
# #                     flop_cleaned += line + '\n'
# #             return flop_cleaned
# #
# #     # if 'all-in' in str(get_hand_preflop_action(hand)):
# #     #     return 'ALL-IN - PRE - CALLED' if 'folded' not in hand else 'ALL-IN - PRE - UNCALLED'
# #     #
# #     # elif 'all-in' in str(get_hand_flop_action(hand)):
# #     #     return 'ALL-IN - FLOP - CALLED' if 'folded' not in hand else 'ALL-IN - FLOP - UNCALLED'
# #     #
# #     # elif 'all-in' in str(get_hand_turn_action(hand)):
# #     #     return 'ALL-IN - TURN - CALLED' if 'folded' not in hand else 'ALL-IN - TURN - UNCALLED'
# #     #
# #     # elif 'all-in' in str(get_hand_river_action(hand)):
# #     #     return 'ALL-IN - RIVER - CALLED' if 'folded' not in hand else 'ALL-IN - RIVER - UNCALLED'
# #     #
# #     # elif '*** SHOW DOWN ***' in hand:
# #     #     return 'SHOWDOWN'
# #     #
# #     # else:
# #     #     return None
# #
# #     return 'hand-type'



# ----------



import copy


def get_hands_in_list(parent_folder, hand_history_filenames):
    def order_hands_by_time(hands):
        a = sorted(hands, key=lambda x: '20' + str(x.split('\n')[0].split('- 20')[1]))
        return a
    hands = []
    for filename in hand_history_filenames:
        # open current filename
        with open(parent_folder + '/' + filename, 'r') as f:
            data = f.read()
            hhtext = copy.deepcopy(data)
        # split the hands into a list
        str_to_hands = hhtext.split('\n\n')
        for hand_ in str_to_hands:
            hands.append(hand_)
        del hands[-1]
    # order hands by time
    hands_t = order_hands_by_time(hands)
    return hands_t



def get_time(hand_txt):
    return '202' + hand_txt.split('\n')[0].split(')- 202')[1]

def get_level(hand_txt):
    return hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]

def get_my_cards(hand_txt):
    for line in hand_txt.split('\n'):
        if 'Dealt to ' + PLAYER_NAME + ' [' in line:
            return line.replace('Dealt to ' + PLAYER_NAME + ' [', '').replace(']', '')

def get_board_cards(hand_txt):
    for line in hand_txt.split('\n'):
        if 'Board [' in line:
            return line.replace('Board [', '').replace(']', '')
    return 'no-board'

def get_tourney_id(hand_txt):
    for line in hand_txt.split('\n'):
        if 'Tournament #' in line:
            return int(line.split('Tournament #')[1].split(' - ')[0])

def get_hand_id(hand: str) -> int:
    for line in hand.split('\n'):
        if 'Game Hand #' in line:
            return int(line.split('Game Hand #')[1].split(' - ')[0])

def get_position(hand_txt: str) -> str:
    return 'todo and testing'

def get_starting_stack_size_bb(hand_txt: str) -> float:
    current_level_big_blind = float(str(hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]).split('/')[1].replace(')', ''))
    for line in hand_txt.split('\n'):
        if PLAYER_NAME + ' (' in line:
            return round(int(line.split(PLAYER_NAME + ' (')[1].split('.')[0])/current_level_big_blind, 1)


def get_main_pot_winner(hand_txt: str) -> str:

    # side pots
    if 'side pot-1' in str(hand_txt):
        for line in hand_txt.split('\n'):
            if 'main pot' in line:
                return line.split(' collected')[0]

    # chop pot
    if str(hand_txt).count('from main pot') >= 2:
        return '**[CHOP-CHOP]**'

    # normal main pot
    for line in hand_txt.split('\n'):
        if 'and won' in line:
            if 'did not' in line:
                return line.split(' did not ')[0].split(': ')[1]
            elif 'showed' in line:
                return line.split(' showed ')[0].split(': ')[1].split(' (')[0]


def get_winner_of_side_pot(hand, pot_nb):
    # if side pot winner = main pot winner
    for line in hand.split('\n'):
        if ('side pot-' + str(pot_nb)) in line:
            return line.split(' collected')[0]
    return 'no-side-pot'

def get_side_pot_1_winner(hand_txt: str) -> str:
    return get_winner_of_side_pot(hand_txt, 1)

def get_side_pot_2_winner(hand_txt: str) -> str:
    return get_winner_of_side_pot(hand_txt, 2)

def get_side_pot_3_winner(hand_txt: str) -> str:
    return get_winner_of_side_pot(hand_txt, 3)









def get_main_pot_size_bb(hand_txt: str) -> float:
    current_level_big_blind = float(str(hand_txt.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]).split('/')[1].replace(')', ''))

    # if just one main pot:
    if get_winner_of_side_pot(hand_txt, pot_nb=1) == 'no-side-pot':
        for line in hand_txt.split('\n'):
            if ' did not show and won ' in line:
                pot_size_chips = int(line.split(' did not show and won ')[1].split('.')[0])
                return round(pot_size_chips / current_level_big_blind, 2)
            elif '] and won ' in line:
                pot_size_chips = int(line.split('] and won ')[1].split(' with ')[0].split('.')[0])
                return round(pot_size_chips / current_level_big_blind, 2)
    else:
        # if winner wins side + main
        if get_main_pot_winner(hand_txt) == get_winner_of_side_pot(hand_txt, pot_nb=1):
            for line in hand_txt.split('\n'):
                if 'Total pot ' in line:
                    pot_size_chips = int(line.split('Total pot ')[1].split('.')[0])
                    return round(pot_size_chips / current_level_big_blind, 2)

        # if winner wins only main
        for line in hand_txt.split('\n'):
            if '.00 from main pot' in line:
                pot_size_chips = int(line.split('.00 from main pot')[0].split('collected ')[1])
                return round(pot_size_chips / current_level_big_blind, 2)



def get_side_pot_size(hand, pot_nb):
    current_level_big_blind = float(str(get_level(hand)).split('/')[1].replace(')', ''))
    for line in hand.split('\n'):
        if ('from side pot-' + str(pot_nb)) in line:
            pot_size_chips = int(line.split(' collected ')[1].split('.00 from side pot-' + str(pot_nb))[0])
            return round(pot_size_chips / current_level_big_blind, 2)
    return 0

def get_side_pot_1_size_bb(hand_txt: str) -> int:
    return get_side_pot_size(hand_txt, 1)

def get_side_pot_2_size_bb(hand_txt: str) -> int:
    return get_side_pot_size(hand_txt, 2)

def get_side_pot_3_size_bb(hand_txt: str) -> int:
    return get_side_pot_size(hand_txt, 3)




class Hand:
    def __init__(self, hand_txt):
        self.hand_txt = hand_txt
        self.time = None
        self.level = None
        self.my_cards = None
        self.board_cards = None
        self.tourney_id = None
        self.hand_id = None
        self.position = None
        self.starting_stack_size_bb = None
        self.main_pot_winner = None
        self.side_pot_1_winner = None
        self.side_pot_2_winner = None
        self.side_pot_3_winner = None
        self.main_pot_size_bb = None
        self.side_pot_1_size_bb = None
        self.side_pot_2_size_bb = None
        self.side_pot_3_size_bb = None

    def _get_time(self):
        self.time = get_time(self.hand_txt)

    def _get_level(self):
        self.level = get_level(self.hand_txt)

    def _get_my_cards(self):
        self.my_cards = get_my_cards(self.hand_txt)

    def _get_board_cards(self):
        self.board_cards = get_board_cards(self.hand_txt)

    def _get_tourney_id(self):
        self.tourney_id = get_tourney_id(self.hand_txt)

    def _get_hand_id(self):
        self.hand_id = get_hand_id(self.hand_txt)

    def _get_position(self):
        self.position = get_position(self.hand_txt)

    def _get_starting_stack_size_bb(self):
        self.starting_stack_size_bb = get_starting_stack_size_bb(self.hand_txt)

    def _get_main_pot_winner(self):
        self.main_pot_winner = get_main_pot_winner(self.hand_txt)

    def _get_side_pot_1_winner(self):
        self.side_pot_1_winner = get_side_pot_1_winner(self.hand_txt)

    def _get_side_pot_2_winner(self):
        self.side_pot_2_winner = get_side_pot_2_winner(self.hand_txt)

    def _get_side_pot_3_winner(self):
        self.side_pot_3_winner = get_side_pot_3_winner(self.hand_txt)

    def _get_main_pot_size_bb(self):
        self.main_pot_size_bb = get_main_pot_size_bb(self.hand_txt)

    def _get_side_pot_1_size_bb(self):
        self.side_pot_1_size_bb = get_side_pot_1_size_bb(self.hand_txt)

    def _get_side_pot_2_size_bb(self):
        self.side_pot_2_size_bb = get_side_pot_2_size_bb(self.hand_txt)

    def _get_side_pot_3_size_bb(self):
        self.side_pot_3_size_bb = get_side_pot_3_size_bb(self.hand_txt)

    def build_hand(self):
        self._get_time()
        self._get_level()
        self._get_my_cards()
        self._get_board_cards()
        self._get_tourney_id()
        self._get_hand_id()
        self._get_position()
        self._get_starting_stack_size_bb()
        self._get_main_pot_winner()
        self._get_side_pot_1_winner()
        self._get_side_pot_2_winner()
        self._get_side_pot_3_winner()
        self._get_main_pot_size_bb()
        self._get_side_pot_1_size_bb()
        self._get_side_pot_2_size_bb()
        self._get_side_pot_3_size_bb()


def process_hands(hands: list) -> list:
    processed_hands = []
    for h in hands:
        new_hand = Hand(hand_txt=h)
        new_hand.build_hand()
        processed_hands.append(new_hand)
    return processed_hands

#
# def get_hands_info(hands: list) -> list:
#
#     # hands_replayer_links = generate_hh_links_replayer(hands)
#     #
#     # # # BUG WITH THE REPLAYER.... IT GENERATES 18 HANDS WHEN THERES 17 IN THE FILE?!!
#     # if len(hands) != len(hands_replayer_links):
#     #     print('@@@@@@@@@@@@@ BUG  - hands:', len(hands), '- replayer:', len(hands_replayer_links))
#
#     hands_ = []
#     for i, hand in enumerate(hands):
#         # try:
#         #     replayer_link = hands_replayer_links[i]
#         # except IndexError:
#         #     replayer_link = None
#
#         hands_.append({
#             'time': get_hand_time(hand),
#             'level': get_hand_level(hand),
#             'my_cards': get_hand_my_cards(hand),
#             'board_cards': get_hand_board_cards(hand),
#             'replayer_link': None,
#             'tourney_id': get_tourney_id(hand),
#             'hand_id': get_hand_id(hand),
#
#             'Position': get_hand_position(hand),
#
#             'Stack size at start of hand': get_stack_size_start_of_hand(hand),
#
#             'Winner (Main Pot)': get_winner_of_main_pot(hand),
#             'Winner (Side Pot #1)': get_winner_of_side_pot(hand, pot_nb=1),
#             'Winner (Side Pot #2)': get_winner_of_side_pot(hand, pot_nb=2),
#             'Winner (Side Pot #3)': get_winner_of_side_pot(hand, pot_nb=3),
#
#             'Pot Size (Main Pot)': get_main_pot_size(hand),
#             'Pot Size (Side Pot #1)': get_side_pot_size(hand, pot_nb=1),
#             'Pot Size (Side Pot #2)': get_side_pot_size(hand, pot_nb=2),
#             'Pot Size (Side Pot #3)': get_side_pot_size(hand, pot_nb=3),
#
#         })
#
#     return hands_
