from datetime import datetime
import requests


def extract_price_from_title(title: str) -> float:
    if "$0{FULLSTOP}50 Hold'Em Turbo" in title:
        return 0.55


def extract_id_from_content(content: str) -> int:
    return int(content.split('\n')[0].split('Tournament ')[1][1:9])


def extract_finished_time_from_content(content: str) -> str:
    finished_time = '202' + content.split('\n\n')[:-1][-1].split('\n')[0].split(')- 202')[1]
    return finished_time


def extract_elapsed_time_from_content(content: str) -> int:
    last_hand_time_ = '202' + content.split('\n\n')[:-1][0].split('\n')[0].split(')- 202')[1][:-4]
    first_hand_time_ = '202' + content.split('\n\n')[:-1][-1].split('\n')[0].split(')- 202')[1][:-4]
    last_hand_time = datetime.strptime(last_hand_time_.replace('/', '-'), '%Y-%m-%d %H:%M:%S')
    first_hand_time = datetime.strptime(first_hand_time_.replace('/', '-'), '%Y-%m-%d %H:%M:%S')
    duration = first_hand_time - last_hand_time  # For build-in functions
    duration_in_mn = duration.total_seconds()/60
    return round(duration_in_mn)

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

    data = {
        '$filename': '',
        'text': hands,
        'format': 'replayer',
        'make_public': 'true',
        'hide_results': 'false',
        'hide_names': 'false',
        'embedded': 'false',
        'skin': 'pokeit'
    }

    response = requests.post('http://pokeit.co/convert/hand.php', headers=headers, data=data)

    return response.json()['links']

def extract_hands_from_content(content: str):
    def extract_hands_from_content_to_list(content: str) -> list:
        hands = []
        for hand in content.split('\n\n'):
            hands.append(hand)
        del hands[-1]
        return hands

    def get_hand_time(hand):
        time = '202' + hand.split('\n')[0].split(')- 202')[1]
        return time

    def get_hand_pot_size(hand):
        for line in hand.split('\n'):
            if 'Total pot ' in line:
                return int(line.replace('Total pot ', '').split('.')[0])

    def get_hand_level(hand):
        level = hand.split('\n')[0].split(' - Level')[1].split('- 20')[0]
        return level

    def get_hand_my_cards(hand):
        for line in hand.split('\n'):
            if 'Dealt to PotNoodle99912 [' in line:
                return line.replace('Dealt to PotNoodle99912 [', '').replace(']', '')

    def get_hand_board_cards(hand):
        for line in hand.split('\n'):
            if 'Board [' in line:
                return line.replace('Board [', '').replace(']', '')
        return None

    def get_hand_type(hand):

        def get_hand_preflop_action(hand):
            preflop = hand.split('*** FLOP ***')[0].split('*** HOLE CARDS ***')[1].split('*** SUMMARY ***')[0]
            return preflop

        def get_hand_flop_action(hand):
            if '*** FLOP ***' not in hand:
                return None
            if 'all-in' in get_hand_preflop_action(hand):
                return None
            else:
                flop = hand.split('*** FLOP ***')[1].split('***')[0].split(']')[1].split('\n')
                flop_cleaned = ''
                for line in flop:
                    if line != '':
                        flop_cleaned += line + '\n'
                return flop_cleaned

        def get_hand_turn_action(hand):
            if '*** TURN ***' not in hand:
                return None
            if 'all-in' in get_hand_preflop_action(hand):
                return None
            else:
                flop = hand.split('*** TURN ***')[1].split('***')[0].split('\n')
                flop_cleaned = ''
                for line in flop:
                    if (line != '') and ('] [' not in line):
                        flop_cleaned += line + '\n'
                return flop_cleaned

        def get_hand_river_action(hand):
            if '*** RIVER ***' not in hand:
                return None
            if 'all-in' in get_hand_preflop_action(hand):
                return None
            else:
                flop = hand.split('*** RIVER ***')[1].split('***')[0].split('\n')
                flop_cleaned = ''
                for line in flop:
                    if (line != '') and ('] [' not in line):
                        flop_cleaned += line + '\n'
                return flop_cleaned

        if 'all-in' in str(get_hand_preflop_action(hand)):
            return 'ALL-IN - PRE - CALLED' if 'folded' not in hand else 'ALL-IN - PRE - UNCALLED'

        elif 'all-in' in str(get_hand_flop_action(hand)):
            return 'ALL-IN - FLOP - CALLED' if 'folded' not in hand else 'ALL-IN - FLOP - UNCALLED'

        elif 'all-in' in str(get_hand_turn_action(hand)):
            return 'ALL-IN - TURN - CALLED' if 'folded' not in hand else 'ALL-IN - TURN - UNCALLED'

        elif 'all-in' in str(get_hand_river_action(hand)):
            return 'ALL-IN - RIVER - CALLED' if 'folded' not in hand else 'ALL-IN - RIVER - UNCALLED'

        elif '*** SHOW DOWN ***' in hand:
            return 'SHOWDOWN'

        else:
            return None

    hands = []
    hands_replayer_link = generate_hh_links_replayer(content)
    for i, hand in enumerate(extract_hands_from_content_to_list(content)):
        hands.append({
            'time': get_hand_time(hand),
            'pot_size': get_hand_pot_size(hand),
            'level': get_hand_level(hand),
            'my_cards': get_hand_my_cards(hand),
            'board_cards': get_hand_board_cards(hand),
            'hand_type': get_hand_type(hand),
            'replayer_link': hands_replayer_link[i]
        })

    return hands

def extract_opponents_names(tourney_summary: dict) -> list:
    opponents = []
    for opp in tourney_summary['tournament_finishes_and_winnings']:
        opponents.append(opp['player_name'])
    return opponents


def extract_nb_of_participants(tourney_summary: dict) -> list:
    return tourney_summary['player_count']


def extract_prize(tourney_summary: dict) -> float:
    for player in tourney_summary['tournament_finishes_and_winnings']:
        if player['player_name'] == 'PotNoodle99912':
            return player['prize']


def extract_position(tourney_summary: dict) -> int:
    for player in tourney_summary['tournament_finishes_and_winnings']:
        if player['player_name'] == 'PotNoodle99912':
            return player['finish_position']


# ------


def extract_from_raw_hh(raw_hh: list) -> list:
    extraction = []
    for hh in raw_hh:
        extraction.append({
            'new_hands': extract_hands_from_content(hh['content']),
            'new_tournament': {
                'id': extract_id_from_content(hh['content']),
                'price': extract_price_from_title(hh['title']),
                'finished_time': extract_finished_time_from_content(hh['content']),
                'elapsed_time': extract_elapsed_time_from_content(hh['content']),
                'prize': extract_prize(hh['tourney_summary']),
                'position': extract_position(hh['tourney_summary'])
            },
            'new_opponents': extract_opponents_names(hh['tourney_summary'])
        })
    return extraction