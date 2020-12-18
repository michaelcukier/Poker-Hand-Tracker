from datetime import datetime


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
