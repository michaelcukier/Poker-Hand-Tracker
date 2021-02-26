from utils.run_sql_command import run_sql_command
from utils.make_line_plot import make_line_plot


def player_range_heatmap(database_file_path: str, player_name, position, nb_seated):

    if position == 'UTG':
        selector = {
            'name': 'UTG_player_name',
            'cards': 'UTG_cards'
        }
    elif position == 'SB':
        selector = {
            'name': 'SB_player_name',
            'cards': 'SB_cards'
        }

    query = '''
        SELECT 
            {0} 
        FROM 
            hands 
        WHERE
            {0} != 'None'
    '''.format(selector['cards'], selector['name'], player_name, nb_seated)

    data = run_sql_command(
        query=query,
        unique_items=True,
        database_file_path=database_file_path
    )

    return data


# from GLOBAL_VARIABLES import DATABASE_LOCATION
# print(player_range_heatmap(
#     database_file_path=DATABASE_LOCATION,
#     player_name='DmexicanPooh',
#     position='SB',
#     nb_seated=9
# ))


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

freq_each = {"AA": 128, "KK": 66, "AKs": 45}
freq_each_raised = {
    "AA": 178, "KK": 69,  "AKs": 46
}


cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


matrix___ = [[0 for i in range(13)] for j in range(13)]


idx = 0
for idx_c1, c1 in enumerate(cards):
    for idx_c2, c2 in enumerate(cards):

        findMax = max(idx_c1, idx_c2)
        findMin = min(idx_c1, idx_c2)
        egg_max = [findMax, findMax]
        egg_min = [findMin, findMin]
        loc = [idx_c1, idx_c2]

        print(c1, c2)
        print('egg', egg_min)
        print('egg', egg_max)
        print(loc)
        print()

        if loc == egg_max:
            cardsss = c1 + c2

        if (loc[0] < egg_max[0]) and (loc[1] > egg_min[1]):
            cardsss = c1 + c2 + 's'

        if (loc[0] > egg_min[0]) and (loc[1] < egg_max[1]):
            cardsss = c1 + c2 + 'o'

        matrix___[idx_c1][idx_c2] = cardsss

# for r in matrix:
#     print(r)
#
#
# quit()

freq_percentage = dict()
for i in freq_each:
    if(i in freq_each_raised):
        freq_percentage[i] = freq_each_raised[i]/freq_each[i]

matrix = [[0 for i in range(13)] for j in range(13)]

for i in freq_percentage:
    for m in range(13):
        b = 0
        for n in range(13):
            if(matrix___[m][n] == i):
                matrix[m][n] = round(freq_percentage[i], 2)
                b = 1
                break
        if(b):
            break

hands_percentage1 = pd.DataFrame(matrix)

hands_percentage2 = pd.DataFrame(matrix)



# Here we create a figure instance, and two subplots
fig = plt.figure(figsize=(19,15))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
# ax2 = fig.add_subplot(212)

# We use ax parameter to tell seaborn which subplot to use for this plot
sns.heatmap(hands_percentage1, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False, ax=ax1)

sns.heatmap(hands_percentage2, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False, ax=ax2)



#
# fig, axs = plt.subplots(2)
# fig.suptitle('Vertically stacked subplots')
#
#
# fig.add_subplot(
#     sns.heatmap(hands_percentage, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False))
# fig.add_subplot(
# sns.heatmap(hands_percentage, cmap="YlGnBu", square=True, annot = matrix___, fmt = '', xticklabels=False, yticklabels=False))

plt.savefig('./nowhitespace.png', bbox_inches='tight', pad_inches=0.5)
plt.show()
