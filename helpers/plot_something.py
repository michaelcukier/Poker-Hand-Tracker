import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
from scipy.ndimage.filters import gaussian_filter1d


def plot_something(list_of_data_points, xlabel, ylabel, title, add_avg_line=False, sigma=0):

    if add_avg_line:
        x = range(1, len(list_of_data_points) + 1)
        y = gaussian_filter1d(list_of_data_points, sigma=sigma)
        plt.plot(x, y, '--')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    x2 = range(1, len(list_of_data_points) + 1)
    y2 = list_of_data_points

    plt.plot(x2, y2)
    plt.show()
