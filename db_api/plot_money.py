
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


from scipy.ndimage.filters import gaussian_filter1d

x = range(len(starting))
y = gaussian_filter1d(intz, sigma=10)
plt.plot(x,y)
plt.xlabel("# of game")
plt.ylabel("Money ($)")
plt.title("Money made over time in the $0.55's")
x2 = range(len(starting))
y2 = intz

plt.plot(x2, y2)

plt.show()