import requests

from GLOBAL_VARIABLES import PLAYER_NAME


def generate_hh_links_replayer(hands):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://pokeit.co',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://pokeit.co/convert/',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,la;q=0.7',
    }

    to_send = '\n\n'.join(hands)

    data = {
        '$filename': '',
        'text': to_send,
        'format': 'replayer',
        'make_public': 'true',
        'hide_results': 'false',
        'hide_names': 'false',
        'embedded': 'false',
        'skin': 'pokeit'
    }

    response = requests.post('http://pokeit.co/convert/hand.php', headers=headers, data=data)

    return response.json()['links']


# DELETE THIS ONE, NEVER USED (REPLACED BY TASK 4 IN raw_hh_to_dict
# def extract_hands_from_content_to_list(content: str) -> list:
#     hands = []
#     for hand in content.split('\n\n'):
#         if 'PotNoodle99912 will be allowed to play after the button' not in hand:  # avoid hands where im not there
#             hands.append(hand)
#     # del hands[-1]
#     return hands


def get_hand_time(hand: str):
    time = '202' + hand.split('\n')[0].split(')- 202')[1]
    return time


def get_hand_pot_size_chips(hand):
    for line in hand.split('\n'):
        if 'Total pot ' in line:
            return int(line.replace('Total pot ', '').split('.')[0])


def get_hand_level(hand):
    level = hand.split('\n')[0].split(' - Level')[1].split('- 20')[0][1:]
    return level


def get_hand_pot_size_bb(hand):
    current_level_big_blind = float(str(get_hand_level(hand)).split('/')[1].replace(')', ''))
    return round(get_hand_pot_size_chips(hand)/current_level_big_blind, 1)


def get_hand_my_cards(hand):
    for line in hand.split('\n'):
        if 'Dealt to ' + PLAYER_NAME + ' [' in line:
            return line.replace('Dealt to ' + PLAYER_NAME + ' [', '').replace(']', '')


def get_hand_board_cards(hand):
    for line in hand.split('\n'):
        if 'Board [' in line:
            return line.replace('Board [', '').replace(']', '')
    return 'no-board'


def get_tourney_id(hand: str) -> int:
    for line in hand.split('\n'):
        if 'Tournament #' in line:
            return int(line.split('Tournament #')[1].split(' - ')[0])


def get_hand_id(hand: str) -> int:
    for line in hand.split('\n'):
        if 'Game Hand #' in line:
            return int(line.split('Game Hand #')[1].split(' - ')[0])


def is_hand_relevant(hand: str) -> bool:
    if PLAYER_NAME + ' folded on the Pre-Flop and did not bet' in hand:
        return False
    if PLAYER_NAME + ' (big blind) folded on the Pre-Flop' in hand:
        return False
    if PLAYER_NAME + ' (small blind) folded on the Pre-Flop' in hand:
        return False
    if PLAYER_NAME + ' (button) folded on the Pre-Flop' in hand:
        return False
    return True


def get_stack_size_start_of_hand(hand):
    for line in hand.split('\n'):
        if PLAYER_NAME + ' (' in line:
            return int(line.split(PLAYER_NAME + ' (')[1].split('.')[0])

#
# def get_hand_type(hand):
#     def get_hand_preflop_action(hand):
#         preflop = hand.split('*** FLOP ***')[0].split('*** HOLE CARDS ***')[1].split('*** SUMMARY ***')[0]
#         return preflop
#
#     def get_hand_flop_action(hand):
#         if '*** FLOP ***' not in hand:
#             return None
#         if 'all-in' in get_hand_preflop_action(hand):
#             return None
#         else:
#             flop = hand.split('*** FLOP ***')[1].split('***')[0].split(']')[1].split('\n')
#             flop_cleaned = ''
#             for line in flop:
#                 if line != '':
#                     flop_cleaned += line + '\n'
#             return flop_cleaned
#
#     def get_hand_turn_action(hand):
#         if '*** TURN ***' not in hand:
#             return None
#         if 'all-in' in get_hand_preflop_action(hand):
#             return None
#         else:
#             flop = hand.split('*** TURN ***')[1].split('***')[0].split('\n')
#             flop_cleaned = ''
#             for line in flop:
#                 if (line != '') and ('] [' not in line):
#                     flop_cleaned += line + '\n'
#             return flop_cleaned
#
#     def get_hand_river_action(hand):
#         if '*** RIVER ***' not in hand:
#             return None
#         if 'all-in' in get_hand_preflop_action(hand):
#             return None
#         else:
#             flop = hand.split('*** RIVER ***')[1].split('***')[0].split('\n')
#             flop_cleaned = ''
#             for line in flop:
#                 if (line != '') and ('] [' not in line):
#                     flop_cleaned += line + '\n'
#             return flop_cleaned
#
#     # if 'all-in' in str(get_hand_preflop_action(hand)):
#     #     return 'ALL-IN - PRE - CALLED' if 'folded' not in hand else 'ALL-IN - PRE - UNCALLED'
#     #
#     # elif 'all-in' in str(get_hand_flop_action(hand)):
#     #     return 'ALL-IN - FLOP - CALLED' if 'folded' not in hand else 'ALL-IN - FLOP - UNCALLED'
#     #
#     # elif 'all-in' in str(get_hand_turn_action(hand)):
#     #     return 'ALL-IN - TURN - CALLED' if 'folded' not in hand else 'ALL-IN - TURN - UNCALLED'
#     #
#     # elif 'all-in' in str(get_hand_river_action(hand)):
#     #     return 'ALL-IN - RIVER - CALLED' if 'folded' not in hand else 'ALL-IN - RIVER - UNCALLED'
#     #
#     # elif '*** SHOW DOWN ***' in hand:
#     #     return 'SHOWDOWN'
#     #
#     # else:
#     #     return None
#
#     return 'hand-type'



# ----------



def get_hands_info(hands: list) -> list:

    hands_replayer_links = generate_hh_links_replayer(hands)

    # # BUG WITH THE REPLAYER.... IT GENERATES 18 HANDS WHEN THERES 17 IN THE FILE?!!
    if len(hands) != len(hands_replayer_links):
        print('@@@@@@@@@@@@@ BUG  - hands:', len(hands), '- replayer:', len(hands_replayer_links))

    hands_ = []
    for i, hand in enumerate(hands):
        try:
            replayer_link = hands_replayer_links[i]
        except IndexError:
            replayer_link = None

        if is_hand_relevant(hand):
            hands_.append({
                'time': get_hand_time(hand),
                'stack_size_start_of_hand': get_stack_size_start_of_hand(hand),
                'pot_size_chips': get_hand_pot_size_chips(hand),
                'pot_size_bb': get_hand_pot_size_bb(hand),
                'level': get_hand_level(hand),
                'my_cards': get_hand_my_cards(hand),
                'board_cards': get_hand_board_cards(hand),
                'replayer_link': replayer_link,
                'tourney_id': get_tourney_id(hand),
                'hand_id': get_hand_id(hand)
            })

    return hands_
