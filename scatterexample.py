import matplotlib.pyplot as plt
import numpy as np
import sys

fig = plt.figure()

ax = fig.subplots(ncols=1, nrows=1)


x = np.linspace(0, 50, 50)
y = np.random.randint(0, 50, 50)

pc = ax.scatter(x=x, y=y)


def on_press(event):
    sys.stdout.flush()
    if event.key == " ":
        y = np.random.randint(0, 50, 50)
        ax.clear()
        ax.scatter(x, y)
        fig.canvas.draw_idle()


fig.canvas.mpl_connect("key_press_event", on_press)

plt.show()
