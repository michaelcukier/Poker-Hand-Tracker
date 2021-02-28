from utils.run_sql_command import run_sql_command
from utils.make_line_plot import make_line_plot



# from tests.utils.create_fake_database.create_fake_database import CreateFakeDatabase
#
# # '25o', '7To', 'K3o', 'AKo', '7Ao', 'TAo', 'TQs', '33', '7Qo', 'J6o', '37s', 'T5o', '2Qo', 'J7o'
# myFakeDB = CreateFakeDatabase(
#     db_name='testDB',
#     table_name='hands',
#     columns_labels=['SB_player_name', 'BB_player_name', 'SB_cards', 'BB_cards'],
#     data=[
#         ['zop', None, 'Ts 7d', None],
#         ['PotNoodle99912', 'zop', 'Ad Qc', None],
#         ['zop', None, '5c 5h'],
#         ['PotNoodle99912', 'carrot', 'Qd 8s', '4c Kd'],
#         ['PotNoodle99912', 'plop', '7d 7c', None],
#         ['PotNoodle99912', 'swdwdfw', None, '2d 3s'],
#         ['efewferf', 'PotNoodle99912', '9c Tc', None],
#         ['PotNoodle99912', 'swdwdfw', 'Td 9d', None],
#         ['PotNoodle99912', 'swdwdfw', None, '5s Jh'],
#         ['efewfwef', 'PotNoodle99912', 'Jc Tc', None],
#         ['PotNoodle99912', 'swdwdfw', 'As 8s', None],
#         ['PotNoodle99912', 'swdwdfw', None, '6c Kd'],
#         ['wefwegrthg', 'PotNoodle99912', None, '6c Kd'],
#         ['tyjhreg', 'PotNoodle99912', None, 'Kc 6c'],
#         ['tyjhreg', 'PotNoodle99912', None, '6s Ks'],
#         ['tyjhreg', 'PotNoodle99912', None, 'Ac As']
#     ])
#
#
# quit()


def player_range_heatmap(database_file_path: str, player_name, nb_seated):

    config = {
        'rows': None,
        'cols': None,
        'sqlColumsToRetrieve': None,
        'AxisToRemove': [],
        'plotsToCreate': None,
    }

    if nb_seated == 2:
        config['rows'] = 1
        config['cols'] = 2
        config['sqlColumsToRetrieve'] = ['SB', 'BB']

    if nb_seated == 9:
        config['rows'] = 1
        config['cols'] = 2
        config['sqlColumsToRetrieve'] = ['SB']

    select_query = []
    for col in config['sqlColumsToRetrieve']:
        select_query.append(col + '_cards')

    where_query = []
    for col in config['sqlColumsToRetrieve']:
        where_query.append(col + "_player_name='{0}'".format(player_name))




    # get the data
    data__ = {}
    for col, whereQuery, selectQuery in zip(config['sqlColumsToRetrieve'], where_query, select_query):

        query = '''
            SELECT 
                {0} 
            FROM 
                hands 
            WHERE
                {1}
            AND
                {0} != 'None'
            AND 
                hand_txt NOT LIKE '%PotNoodle99912 folded on the Pre-Flop and did not bet%'
        '''.format(selectQuery, whereQuery)

        data = run_sql_command(
            query=query,
            unique_items=True,
            database_file_path=database_file_path)

        data__[col] = data


    # transform - step 1 - eg As Ad --> AA, Tc 9s --> T9o
    werrrr = {}
    for pos, hands in data__.items():
        werrrr[pos] = []
        for h in hands:
            if h[0] == h[3]:  # eg As Ad
                cleaned_h = h[0] + h[3]
            elif h[1] == h[4]:  # eg: Ts 9s
                cleaned_h = h[0] + h[3] + 's'
            else:  # eg: 8c 9s
                cleaned_h = h[0] + h[3] + 'o'
            werrrr[pos].append(cleaned_h)

    return werrrr



from GLOBAL_VARIABLES import DATABASE_LOCATION, PLAYER_NAME
mySuperDat = player_range_heatmap(
    database_file_path=DATABASE_LOCATION,
    player_name=PLAYER_NAME,
    nb_seated=9
)


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
#
#
# matrix___ = [[0 for i in range(13)] for j in range(13)]
#
#
# idx = 0
# for idx_c1, c1 in enumerate(cards):
#     for idx_c2, c2 in enumerate(cards):
#
#         findMax = max(idx_c1, idx_c2)
#         findMin = min(idx_c1, idx_c2)
#         egg_max = [findMax, findMax]
#         egg_min = [findMin, findMin]
#         loc = [idx_c1, idx_c2]
#
#         # print(c1, c2)
#         # print('egg', egg_min)
#         # print('egg', egg_max)
#         # print(loc)
#         # print()
#
#         if loc == egg_max:
#             cardsss = c1 + c2
#
#         if (loc[0] < egg_max[0]) and (loc[1] > egg_min[1]):
#             cardsss = c1 + c2 + 's'
#
#         if (loc[0] > egg_min[0]) and (loc[1] < egg_max[1]):
#             cardsss = c1 + c2 + 'o'
#
#         matrix___[idx_c1][idx_c2] = cardsss
#
#
#




matrix___ = [
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



# TRANSFORM TO FREQUENCIES , eg: '6Ko', 'K6s', '6Ks', 'AA' = 1/4, 2/4, 2/4, 1/4
# print('superdat', mySuperDat['BB'])

def transform_list_of_hands_to_frequencies(list_of_observed_hands_for_position_n):
    all_possible_hands = {'AA': 0, 'AKs': 0, 'AQs': 0, 'AJs': 0, 'ATs': 0, 'A9s': 0, 'A8s': 0, 'A7s': 0, 'A6s': 0, 'A5s': 0, 'A4s': 0, 'A3s': 0, 'A2s': 0, 'KAo': 0, 'KK': 0, 'KQs': 0, 'KJs': 0, 'KTs': 0, 'K9s': 0, 'K8s': 0, 'K7s': 0, 'K6s': 0, 'K5s': 0, 'K4s': 0, 'K3s': 0, 'K2s': 0, 'QAo': 0, 'QKo': 0, 'QQ': 0, 'QJs': 0, 'QTs': 0, 'Q9s': 0, 'Q8s': 0, 'Q7s': 0, 'Q6s': 0, 'Q5s': 0, 'Q4s': 0, 'Q3s': 0, 'Q2s': 0, 'JAo': 0, 'JKo': 0, 'JQo': 0, 'JJ': 0, 'JTs': 0, 'J9s': 0, 'J8s': 0, 'J7s': 0,
                          'J6s': 0, 'J5s': 0, 'J4s': 0, 'J3s': 0, 'J2s': 0, 'TAo': 0, 'TKo': 0, 'TQo': 0, 'TJo': 0, 'TT': 0, 'T9s': 0, 'T8s': 0, 'T7s': 0, 'T6s': 0, 'T5s': 0, 'T4s': 0, 'T3s': 0, 'T2s': 0, '9Ao': 0, '9Ko': 0, '9Qo': 0, '9Jo': 0, '9To': 0, '99': 0, '98s': 0, '97s': 0, '96s': 0, '95s': 0, '94s': 0, '93s': 0, '92s': 0, '8Ao': 0, '8Ko': 0, '8Qo': 0, '8Jo': 0, '8To': 0, '89o': 0, '88': 0, '87s': 0, '86s': 0, '85s': 0, '84s': 0, '83s': 0, '82s': 0, '7Ao': 0, '7Ko': 0, '7Qo': 0,
                          '7Jo': 0, '7To': 0, '79o': 0, '78o': 0, '77': 0, '76s': 0, '75s': 0, '74s': 0, '73s': 0, '72s': 0, '6Ao': 0, '6Ko': 0, '6Qo': 0, '6Jo': 0, '6To': 0, '69o': 0, '68o': 0, '67o': 0, '66': 0, '65s': 0, '64s': 0, '63s': 0, '62s': 0, '5Ao': 0, '5Ko': 0, '5Qo': 0, '5Jo': 0, '5To': 0, '59o': 0, '58o': 0, '57o': 0, '56o': 0, '55': 0, '54s': 0, '53s': 0, '52s': 0, '4Ao': 0, '4Ko': 0, '4Qo': 0, '4Jo': 0, '4To': 0, '49o': 0, '48o': 0, '47o': 0, '46o': 0, '45o': 0, '44': 0,
                          '43s': 0, '42s': 0, '3Ao': 0, '3Ko': 0, '3Qo': 0, '3Jo': 0, '3To': 0, '39o': 0, '38o': 0, '37o': 0, '36o': 0, '35o': 0, '34o': 0, '33': 0, '32s': 0, '2Ao': 0, '2Ko': 0, '2Qo': 0, '2Jo': 0, '2To': 0, '29o': 0, '28o': 0, '27o': 0, '26o': 0, '25o': 0, '24o': 0, '23o': 0, '22': 0}

    # step 1 --> ['6Ko', 'K6s', '6Ks', 'AA'] = ['6Ko', 'K6s', 'K6s', 'AA']
    hands_1 = []
    for h in list_of_observed_hands_for_position_n:
        permutHand = h[1] + h[0] + h[2:]  # K6s --> 6Ks
        if permutHand in hands_1:
            hands_1.append(permutHand)
        else:
            hands_1.append(h)

    # step 2 --> ['6Ko', '6Ks', '6Ks', 'AA'] = {'6Ko': 0.25, '6Ks': 0.5, 'AA': 0.25}
    hands_2 = {}
    for c in hands_1:
        hands_2[c] = hands_1.count(c)/len(hands_1)

    # step 3 -- set the values to all_possible_hands
    for hand, freq in hands_2.items():
        permutHand = hand[1] + hand[0] + hand[2:]
        if permutHand in all_possible_hands:
            all_possible_hands[permutHand] = freq
        elif hand in all_possible_hands:
            all_possible_hands[hand] = freq

    frequencies_for_each_hand = all_possible_hands
    return frequencies_for_each_hand


# for k, v in transform_list_of_hands_to_frequencies(['6Ko', 'K6s', '6Ks', 'AA']).items():
#     print(k, v)
#
# quit()



# [(index, row.index(val)) for index, row in enumerate(mymatrix) if val in row]



# matrix1 = {}


#
# for h in mySuperDat['SB']:
#     for idx_row, row in enumerate(matrix___):
#         for idx_col, col in enumerate(row):
#             permutHand = h[1] + h[0] + h[2:]
#             if (h in col) or (permutHand in col):
#                 matrix___[idx_row][idx_col] += '@@@'
#
#
# print()
#
# ergwef = ''
# for r in matrix___:
#     for col in r:
#         ergwef += ''''{0}': 0, '''.format(col)


# print(ergwef)
# quit()

# freq_each_played = {'AA': 0, 'AKs': 0, 'AQs': 0, 'AJs': 0, 'ATs': 0, 'A9s': 0, 'A8s': 0, 'A7s': 0, 'A6s': 0, 'A5s': 0, 'A4s': 0, 'A3s': 0, 'A2s': 0, 'KAo': 0, 'KK': 0, 'KQs': 0, 'KJs': 0, 'KTs': 0, 'K9s': 0, 'K8s': 0, 'K7s': 0, 'K6s': 0, 'K5s': 0, 'K4s': 0, 'K3s': 0, 'K2s': 0, 'QAo': 0, 'QKo': 0, 'QQ': 0, 'QJs': 0, 'QTs': 0, 'Q9s': 0, 'Q8s': 0, 'Q7s': 0, 'Q6s': 0, 'Q5s': 0, 'Q4s': 0, 'Q3s': 0, 'Q2s': 0, 'JAo': 0, 'JKo': 0, 'JQo': 0, 'JJ': 0, 'JTs': 0, 'J9s': 0, 'J8s': 0, 'J7s': 0, 'J6s': 0, 'J5s': 0, 'J4s': 0, 'J3s': 0, 'J2s': 0, 'TAo': 0, 'TKo': 0, 'TQo': 0, 'TJo': 0, 'TT': 0, 'T9s': 0, 'T8s': 0, 'T7s': 0, 'T6s': 0, 'T5s': 0, 'T4s': 0, 'T3s': 0, 'T2s': 0, '9Ao': 0, '9Ko': 0, '9Qo': 0, '9Jo': 0, '9To': 0, '99': 0, '98s': 0, '97s': 0, '96s': 0, '95s': 0, '94s': 0, '93s': 0, '92s': 0, '8Ao': 0, '8Ko': 0, '8Qo': 0, '8Jo': 0, '8To': 0, '89o': 0, '88': 0, '87s': 0, '86s': 0, '85s': 0, '84s': 0, '83s': 0, '82s': 0, '7Ao': 0, '7Ko': 0, '7Qo': 0, '7Jo': 0, '7To': 0, '79o': 0, '78o': 0, '77': 0, '76s': 0, '75s': 0, '74s': 0, '73s': 0, '72s': 0, '6Ao': 0, '6Ko': 0, '6Qo': 0, '6Jo': 0, '6To': 0, '69o': 0, '68o': 0, '67o': 0, '66': 0, '65s': 0, '64s': 0, '63s': 0, '62s': 0, '5Ao': 0, '5Ko': 0, '5Qo': 0, '5Jo': 0, '5To': 0, '59o': 0, '58o': 0, '57o': 0, '56o': 0, '55': 0, '54s': 0, '53s': 0, '52s': 0, '4Ao': 0, '4Ko': 0, '4Qo': 0, '4Jo': 0, '4To': 0, '49o': 0, '48o': 0, '47o': 0, '46o': 0, '45o': 0, '44': 0, '43s': 0, '42s': 0, '3Ao': 0, '3Ko': 0, '3Qo': 0, '3Jo': 0, '3To': 0, '39o': 0, '38o': 0, '37o': 0, '36o': 0, '35o': 0, '34o': 0, '33': 0, '32s': 0, '2Ao': 0, '2Ko': 0, '2Qo': 0, '2Jo': 0, '2To': 0, '29o': 0, '28o': 0, '27o': 0, '26o': 0, '25o': 0, '24o': 0, '23o': 0, '22': 0}


# quit()
#
#
# quit()
#
# freq_percentage = dict()
# for i in freq_each:
#     if(i in freq_each_raised):
#         freq_percentage[i] = freq_each_raised[i]/freq_each[i]

wdwdlllll = mySuperDat['SB']


freq_percentage = transform_list_of_hands_to_frequencies(wdwdlllll)

# print(freq_percentage)
#
#
# quit()
#
# for x, y in freq_percentage.items():
#     print(x, '-', y)





# create freq matrix

matrix = [[0 for i in range(13)] for j in range(13)]

print(freq_percentage)

quit()

for i in freq_percentage:
    for m in range(13):
        b = 0
        for n in range(13):
            if(matrix___[m][n] == i):
                matrix[m][n] = freq_percentage[i]
                b = 1
                break
        if(b):
            break




#
#
#
#
# for r in matrix:
#     print(r)

from matplotlib import rcParams

# figure size in inches
rcParams['figure.figsize'] = 15, 15


hands_percentage1 = pd.DataFrame(matrix)

hands_percentage2 = pd.DataFrame(matrix)

hands_percentage3 = pd.DataFrame(matrix)


fig, axes = plt.subplots(nrows=1, ncols=2)

sns.heatmap(hands_percentage1, cbar=False, cmap="YlGnBu", square=True, annot = matrix___, annot_kws={"size": 7}, fmt = '', xticklabels=False, yticklabels=False, ax=axes[0])
# sns.heatmap(hands_percentage2, cbar=False, cmap="YlGnBu", square=True, annot = matrix___, annot_kws={"size": 7}, fmt = '', xticklabels=False, yticklabels=False, ax=axes[1][1])
# plt.show()

# axes[0, 0].axis('off')
# axes[1, 0].axis('off')

# columns = 3
# rows = 2
# plots = [
#     sns.heatmap(hands_percentage1, cbar=False, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False),
#     sns.heatmap(hands_percentage2, cbar=False, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False),
#     sns.heatmap(hands_percentage2, cbar=False, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False),
#     sns.heatmap(hands_percentage2, cbar=False, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False),
#     sns.heatmap(hands_percentage2, cbar=False, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False),
#     sns.heatmap(hands_percentage2, cbar=False, cmap="YlGnBu", square=True, annot=matrix___, fmt='', xticklabels=False, yticklabels=False),
# ]
# for i in range(1, 6):
#     fig.add_subplot(rows, columns, i)
#     plots[i] ### what you want you can plot

# plt.title('Observed range for "PotNoodle9973"\n\nUTG (23/108 samples) | Seated players: 9\n')

# ax.text(4, 0.001, r'an equation: $E=mc^2$', fontsize=15, bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 2})

# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax2 = fig.add_subplot(212)

# We use ax parameter to tell seaborn which subplot to use for this plot
# sns.heatmap( hands_percentage1,cbar=False, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False, ax=ax)
# plt.gcf().text(0.05, 0.9, 'textstr', fontsize=24)

# plt.figtext(100, 100, 'lol', fontdict=None)

# sns.heatmap(hands_percentage2, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False, ax=ax2)
#



# fig, axs = plt.subplots(2)
# fig.suptitle('Vertically stacked subplots')
#
#
# fig.add_subplot(
#     sns.heatmap(hands_percentage1, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False, ax=ax1))
# fig.add_subplot(
# sns.heatmap(hands_percentage2, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False, ax=ax2))

plt.savefig('./nowhitespace.png', bbox_inches='tight', pad_inches=0.5)
# plt.show()
