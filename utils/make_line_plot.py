import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
from matplotlib.pyplot import figure


def make_line_plot(list_of_data_points, xlabel, ylabel, title, add_avg_line=False, sigma=0, all_xticks=False, custom_width=False, width=0):
    if custom_width:
        figure(num=None, figsize=(width, 6), dpi=300, facecolor='w', edgecolor='k')
    else:
        figure(num=None, figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
    if add_avg_line:
        x = range(1, len(list_of_data_points) + 1)
        y = gaussian_filter1d(list_of_data_points, sigma=sigma)
        plt.plot(x, y, '--')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    x2 = range(1, len(list_of_data_points) + 1)
    y2 = list_of_data_points
    if all_xticks:
        plt.xticks(x2)
    plt.plot(x2, y2)
    plt.grid()
    plt.savefig(str(title + '.jpg').replace(' ', '_'), dpi=300, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, pad_inches=1, metadata=None)
    return title + '.jpg'
