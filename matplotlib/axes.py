from matplotlib.axes import Axes
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure(figsize=(10, 8))

COLS_AMOUNT = 3
ROWS_AMOUNT = 3
axs = fig.subplots(ncols=COLS_AMOUNT, nrows=ROWS_AMOUNT)


for row in range(ROWS_AMOUNT):
    for col in range(COLS_AMOUNT):
        current_axes: Axes = axs[row, col]
        x = np.arange(100)
        y = np.cumsum(np.random.randn(100))
        lines = current_axes.plot(x, y, "r")
        maxY = y.max()
        minY = y.min()
        print(minY, maxY)
        middleY = (maxY + minY) / 2

        maxX = x.max()
        minX = x.min()
        middleX = (maxX + minX) / 2
        # current_axes.annotate(
        #     f"axs[{row},{col}]",
        #     (middleX, middleY),
        #     transform=current_axes.transAxes,
        #     ha="center",
        #     va="center",
        #     fontsize=18,
        #     color="darkgrey",
        # )
        current_axes.set_title(f"axs[{row},{col}]")
fig.suptitle("plt.subplots()")
plt.show()
