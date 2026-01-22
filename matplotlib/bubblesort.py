import copy
from matplotlib import animation
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np

actions = []


def bubble_sort(vals):
    for i in range(len(vals)):
        for j in range(0, len(vals) - i - 1):
            actions.append((j, j + 1, "COMPARE"))
            if vals[j] > vals[j + 1]:
                actions.append((j, j + 1, "SWAP"))
                vals[j], vals[j + 1] = vals[j + 1], vals[j]

    return vals


x = np.arange(1, 50, 1)
values = np.arange(1, 50, 1)
np.random.shuffle(values)

fig = plt.figure()
ax = plt.subplot()
bc = ax.bar(x, values, width=1, color="#00aaaa")

copied_values = copy.deepcopy(values)

bubble_sort(values)
print(values)


def animate(frame):
    if frame > 5:
        a, b = actions[frame - 4][0], actions[frame - 4][1]
        rect: Rectangle
        rect = bc[a]
        rect.set_color("#00aaaa")
        rect = bc[b]
        rect.set_color("#00aaaa")

    if actions[frame][2] == "COMPARE":
        pass
    elif actions[frame][2] == "SWAP":
        a, b = actions[frame][0], actions[frame][1]
        copied_values[a], copied_values[b] = copied_values[b], copied_values[a]
        bc[a].set_height(copied_values[a])
        bc[b].set_height(copied_values[b])
        rect: Rectangle
        rect = bc[a]
        rect.set_color("#00ffff")
        rect = bc[b]
        rect.set_color("#00ffff")
    return bc


ani = animation.FuncAnimation(
    fig=fig, func=animate, frames=len(actions), interval=3, blit=True, repeat=False
)
plt.show()
