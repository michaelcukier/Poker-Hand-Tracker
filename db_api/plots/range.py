

hand_matrix = [
    ['AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s'],
    ['KAo', 'KK', 'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s'],
    ['QAo', 'QKo', 'QQ', 'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s'],
    ['JAo', 'JKo', 'JQo', 'JJ', 'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s'],
    ['TAo', 'TKo', 'TQo', 'TJo', 'TT', 'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s'],
    ['9Ao', '9Ko', '9Qo', '9Jo', '9To', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s'],
    ['8Ao', '8Ko', '8Qo', '8Jo', '8To', '89o', '88', '87s', '86s', '85s', '84s', '83s', '82s'],
    ['7Ao', '7Ko', '7Qo', '7Jo', '7To', '79o', '78o', '77', '76s', '75s', '74s', '73s', '72s'],
    ['6Ao', '6Ko', '6Qo', '6Jo', '6To', '69o', '68o', '67o', '66', '65s', '64s', '63s', '62s'],
    ['5Ao', '5Ko', '5Qo', '5Jo', '5To', '59o', '58o', '57o', '56o', '55', '54s', '53s', '52s'],
    ['4Ao', '4Ko', '4Qo', '4Jo', '4To', '49o', '48o', '47o', '46o', '45o', '44', '43s', '42s'],
    ['3Ao', '3Ko', '3Qo', '3Jo', '3To', '39o', '38o', '37o', '36o', '35o', '34o', '33', '32s'],
    ['2Ao', '2Ko', '2Qo', '2Jo', '2To', '29o', '28o', '27o', '26o', '25o', '24o', '23o', '22']]


def create_config_for_sql_query(position_at_table: str, player_name: str) -> dict:

    config = {}

    # position_at_table = blinds | early | middle | late

    if position_at_table == 'early':
        config['sqlColumsToRetrieve'] = ['UTG', 'UTGp1']

    if position_at_table == 'blinds':
        config['sqlColumsToRetrieve'] = ['SB', 'BB']

    if position_at_table == 'middle':
        config['sqlColumsToRetrieve'] = ['MP', 'MPp1', 'MPp2']

    if position_at_table == 'late':
        config['sqlColumsToRetrieve'] = ['CO', 'BTN']

    select_query = []
    for col in config['sqlColumsToRetrieve']:
        select_query.append(col + '_cards')
    config['select_query'] = select_query

    where_query = []
    for col in config['sqlColumsToRetrieve']:
        where_query.append(col + "_player_name='{0}'".format(player_name))
    config['where_query'] = where_query

    config['player_name'] = player_name

    return config



def check_if_folded_pre(hand_txt):
    for line in hand_txt.split('\n'):
        if ('PotNoodle99912' in line) and ('folded on the Pre-Flop' in line):
            return True
    return False

from utils.run_sql_command import run_sql_command

from GLOBAL_VARIABLES import PLAYER_NAME, DATABASE_LOCATION

def get_sql_data(config: dict, database_file_path: str) -> list:

    where_query = config['where_query']
    select_query = config['select_query']

    data = []
    for whereQ, selectQ in zip(where_query, select_query):
        query = '''
                SELECT
                    {0}, hand_txt
                FROM
                    hands
                WHERE
                    {1}
                AND
                    {0} != 'None'
            '''.format(selectQ, whereQ)

        retrieval = run_sql_command(
            query=query,
            unique_items=False,
            database_file_path=database_file_path)

        remove_folded_preflop = []
        for cards, hand_txt in retrieval:
            if not check_if_folded_pre(hand_txt):
                remove_folded_preflop.append(cards)

        data.extend(remove_folded_preflop)

    return data



def transform_cards(cards: list) -> list:
    # eg ['As Ad', 'Tc 9s', ...]   -->    ['AA', 'T9o', ...]
    cards_without_suit = []
    for c in cards:
        if c[0] == c[3]:  # eg As Ad --> AA
            cleaned_h = c[0] + c[3]
        elif c[1] == c[4]:  # eg: Td 9d --> T9s
            cleaned_h = c[0] + c[3] + 's'
        elif c[1] != c[4]:  # eg: 8c 9s  --> 89o
            cleaned_h = c[0] + c[3] + 'o'
        cards_without_suit.append(cleaned_h)

    return cards_without_suit


def transform_to_frequencies(observed_hands: list) -> dict:
    # eg ['6Ko', 'K6s', 'K6s', 'AA']    -->    {'AA': 0.25, ... , K6s': 0.5, ..., '6Ko': 0.25, '22': 0}

    all_possible_hands = {'AA': 0, 'AKs': 0, 'AQs': 0, 'AJs': 0, 'ATs': 0, 'A9s': 0, 'A8s': 0, 'A7s': 0, 'A6s': 0, 'A5s': 0, 'A4s': 0, 'A3s': 0, 'A2s': 0, 'KAo': 0, 'KK': 0, 'KQs': 0, 'KJs': 0, 'KTs': 0, 'K9s': 0, 'K8s': 0, 'K7s': 0, 'K6s': 0, 'K5s': 0, 'K4s': 0, 'K3s': 0, 'K2s': 0, 'QAo': 0, 'QKo': 0, 'QQ': 0, 'QJs': 0, 'QTs': 0, 'Q9s': 0, 'Q8s': 0, 'Q7s': 0, 'Q6s': 0, 'Q5s': 0, 'Q4s': 0, 'Q3s': 0, 'Q2s': 0, 'JAo': 0, 'JKo': 0, 'JQo': 0, 'JJ': 0, 'JTs': 0, 'J9s': 0, 'J8s': 0, 'J7s': 0,
                          'J6s': 0, 'J5s': 0, 'J4s': 0, 'J3s': 0, 'J2s': 0, 'TAo': 0, 'TKo': 0, 'TQo': 0, 'TJo': 0, 'TT': 0, 'T9s': 0, 'T8s': 0, 'T7s': 0, 'T6s': 0, 'T5s': 0, 'T4s': 0, 'T3s': 0, 'T2s': 0, '9Ao': 0, '9Ko': 0, '9Qo': 0, '9Jo': 0, '9To': 0, '99': 0, '98s': 0, '97s': 0, '96s': 0, '95s': 0, '94s': 0, '93s': 0, '92s': 0, '8Ao': 0, '8Ko': 0, '8Qo': 0, '8Jo': 0, '8To': 0, '89o': 0, '88': 0, '87s': 0, '86s': 0, '85s': 0, '84s': 0, '83s': 0, '82s': 0, '7Ao': 0, '7Ko': 0, '7Qo': 0,
                          '7Jo': 0, '7To': 0, '79o': 0, '78o': 0, '77': 0, '76s': 0, '75s': 0, '74s': 0, '73s': 0, '72s': 0, '6Ao': 0, '6Ko': 0, '6Qo': 0, '6Jo': 0, '6To': 0, '69o': 0, '68o': 0, '67o': 0, '66': 0, '65s': 0, '64s': 0, '63s': 0, '62s': 0, '5Ao': 0, '5Ko': 0, '5Qo': 0, '5Jo': 0, '5To': 0, '59o': 0, '58o': 0, '57o': 0, '56o': 0, '55': 0, '54s': 0, '53s': 0, '52s': 0, '4Ao': 0, '4Ko': 0, '4Qo': 0, '4Jo': 0, '4To': 0, '49o': 0, '48o': 0, '47o': 0, '46o': 0, '45o': 0, '44': 0,
                          '43s': 0, '42s': 0, '3Ao': 0, '3Ko': 0, '3Qo': 0, '3Jo': 0, '3To': 0, '39o': 0, '38o': 0, '37o': 0, '36o': 0, '35o': 0, '34o': 0, '33': 0, '32s': 0, '2Ao': 0, '2Ko': 0, '2Qo': 0, '2Jo': 0, '2To': 0, '29o': 0, '28o': 0, '27o': 0, '26o': 0, '25o': 0, '24o': 0, '23o': 0, '22': 0}

    # step 1 --> ['6Ko', 'K6s', '6Ks', 'AA'] = ['6Ko', 'K6s', 'K6s', 'AA']
    hands_1 = []
    for c in observed_hands:
        permutHand = c[1] + c[0] + c[2:]  # K6s --> 6Ks
        if permutHand in hands_1:
            hands_1.append(permutHand)
        else:
            hands_1.append(c)

    # step 2 --> ['6Ko', '6Ks', '6Ks', 'AA'] = {'6Ko': 0.25, '6Ks': 0.5, 'AA': 0.25}
    hands_2 = {}
    for c in hands_1:
        hands_2[c] = hands_1.count(c) / len(hands_1)

    # step 3 -- set the values to all_possible_hands
    for hand, freq in hands_2.items():
        permutHand = hand[1] + hand[0] + hand[2:]
        if permutHand in all_possible_hands:
            all_possible_hands[permutHand] = freq
        elif hand in all_possible_hands:
            all_possible_hands[hand] = freq

    return all_possible_hands




def create_freq_matrix(freq: dict) -> list:
    # creates a 13*13 matrix with each value set to the frequencies
    matrix = [[0 for i in range(13)] for j in range(13)]

    for i in freq:
        for m in range(13):
            b = 0
            for n in range(13):
                if hand_matrix[m][n] == i:
                    matrix[m][n] = freq[i]
                    b = 1
                    break
            if b:
                break

    return matrix












import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import seaborn as sns


def create_heatmaps(freq_matrix: list, pos: str, player_name: str, nb_of_samples: int):

    # creates and saves the heatmap plot(s)

    rcParams['figure.figsize'] = 15, 7
    df = pd.DataFrame(freq_matrix)
    fig = plt.figure()
    gs = fig.add_gridspec(ncols=1, nrows=1)
    ax1 = fig.add_subplot(gs[0, 0])

    sns.heatmap(
        df,
        cbar=False,
        cmap="YlGnBu",
        square=True,
        annot=hand_matrix,
        annot_kws={"size": 7},
        fmt='',
        xticklabels=False,
        yticklabels=False,
        ax=ax1)

    def generatePositionsNames(_pos: str) -> str:
        if _pos == 'early':
            return 'UTG  |  UTGp1'

        if _pos == 'blinds':
            return 'SB  |  BB'

        if _pos == 'middle':
            return 'MP  |  MPp1  |  MPp2'

        if _pos == 'late':
            return 'CO  |  BTN'

    ax1.set_title('{2} position range of "{0}"\n\n{1} samples\n\n{3}'.format(
        player_name,
        nb_of_samples,
        pos,
        generatePositionsNames(pos)
    ))

    plt.savefig('/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/plots_dump/'+player_name+'_'+pos+'.png', bbox_inches='tight', pad_inches=0.2, dpi=300)
