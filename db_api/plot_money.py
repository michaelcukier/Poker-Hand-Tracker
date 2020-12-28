
from helpers.run_sql_command import run_sql_command

prizes = run_sql_command('SELECT prize FROM tournaments ORDER BY finished_time', unique_items=True)

starting = ['0']

for prize in prizes:
    starting.append(
        float(starting[-1]) + (prize - 0.55)
    )

intz = []
for x in starting:
    intz.append(float(x))

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

from scipy.ndimage.filters import gaussian_filter1d

x = range(1, len(starting) + 1)
y = gaussian_filter1d(intz, sigma=10)
plt.plot(x,y, '--')
plt.xlabel("Game #")
plt.ylabel("Money ($)")
plt.title("Tournament: On-Demand $0.55")
x2 = range(1, len(starting) + 1)
y2 = intz

plt.plot(x2, y2)

plt.show()