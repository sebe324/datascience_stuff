import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


vec_x = np.arange(1, 10 + 1, 1)
vec_y = np.random.randint(5, 10, (10))


print(vec_x)
print(vec_y)


def f(x, a, b):
    return a * x + b


def calculate_cost(vec_x, vec_y, a, b):
    sum = 0
    for x, y in zip(vec_x, vec_y):
        sum += (f(x, a, b) - y) ** 2
    return sum / len(vec_x)


fig = plt.figure(figsize=(10, 8))
ax = fig.subplots(ncols=1, nrows=3, gridspec_kw={"height_ratios": [3, 1, 1]})

ax[0].scatter(vec_x, vec_y)
ax[0].set_xlim(-2, 12)
ax[0].set_ylim(-2, 12)

cost = calculate_cost(vec_x, vec_y, 1, 1)
print(cost)

a = 1
b = 1
slider_a = Slider(ax=ax[1], valmin=-5, valmax=5, valinit=1, label="a")
slider_b = Slider(ax=ax[2], valmin=-10, valmax=10, valinit=1, label="b")
x_vals = np.linspace(-2, 12, 100)
line = ax[0].plot(x_vals, f(x_vals, a, b))
ax[0].set_title("cost: " + str(cost))
fig.tight_layout()


def update_cost(val):
    cost = calculate_cost(vec_x, vec_y, slider_a.val, slider_b.val)
    line[0].set_ydata(f(x_vals, slider_a.val, slider_b.val))
    ax[0].set_title("cost: " + str(cost))


slider_a.on_changed(update_cost)
slider_b.on_changed(update_cost)
plt.show()
