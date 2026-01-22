import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib.animation as animation

fig = plt.figure()

ax = fig.subplots(ncols=1, nrows=1)


x = np.linspace(0, 50, 50)
y = np.random.random(50) * 100

pc = ax.scatter(x=x, y=y)

directionsY = np.random.random(50)
directionsX = np.random.random(50)


def on_press(event):
    sys.stdout.flush()
    if event.key == " ":
        global y
        global directionsY
        global directionsX
        directionsY = np.random.random(50)
        directionsX = np.random.random(50)
        y = np.random.random(50) * 100
        ax.clear()
        ax.scatter(x, y)
        fig.canvas.draw_idle()


ax.set_ylim((-200, 200))

fig.canvas.mpl_connect("key_press_event", on_press)


def update(frame, x, y):
    ax.clear()
    ax.set_ylim((-200, 200))
    y += directionsY
    x += directionsX
    ax.scatter(x, y)


ani = animation.FuncAnimation(
    fig=fig, func=lambda myfun: update(None, x, y), frames=40, interval=30
)
plt.show()
