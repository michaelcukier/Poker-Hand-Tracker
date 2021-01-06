import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def make_scatter_plot(x_coordinates: list, y_coordinates: list, x_label, y_label, title):
    figure(num=None, figsize=(10, 6), dpi=300, facecolor='w', edgecolor=None)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)
    plt.scatter(x_coordinates, y_coordinates, alpha=0.15, s=6500, edgecolors='none')

    # plt.xlim([1, 30])

    x2 = range(1, 41, 1)
    plt.xticks(x2)
    plt.grid()
    plt.show()
    # plt.savefig('./plots_jpgs/' + str(title + '.jpg').replace(' ', '_'), dpi=300, facecolor='w', edgecolor='w',
    #         orientation='portrait', papertype=None, format=None,
    #         transparent=False, bbox_inches='tight', pad_inches=0, metadata=None)
    return title + '.jpg'
