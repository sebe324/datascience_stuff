import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
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


fig = plt.figure(figsize=(6, 3))

ax = fig.subplots(ncols=1, nrows=2, gridspec_kw={"height_ratios": [3, 1]})

ax[0].scatter(vec_x, vec_y)
ax[0].set_xlim(-2, 12)
ax[0].set_ylim(-2, 12)

cost = calculate_cost(vec_x, vec_y, 1, 1)
print(cost)

a = 1
b = 1

next_btn = Button(ax=ax[1], label="next step")


def deriv_cost_a(vec_x, vec_y, a, b):
    sum = 0
    for x, y in zip(vec_x, vec_y):
        sum += (f(x, a, b) - y) * 2 * x
    return sum / len(vec_x)


def deriv_cost_b(vec_x, vec_y, a, b):
    sum = 0
    for x, y in zip(vec_x, vec_y):
        sum += (f(x, a, b) - y) * 2 * 1
    return sum / len(vec_x)


x_vals = np.linspace(-2, 12, 100)
line = ax[0].plot(x_vals, f(x_vals, a, b))
ax[0].set_title("cost: " + str(cost))


def next(val):
    global a
    global b
    hmm1 = deriv_cost_a(vec_x, vec_y, a, b)
    hmm2 = deriv_cost_b(vec_x, vec_y, a, b)
    a -= hmm1 * 0.01
    b -= hmm2 * 0.01
    line[0].set_ydata(f(x_vals, a, b))
    cost = calculate_cost(vec_x, vec_y, a, b)
    ax[0].set_title("cost: " + str(cost))

    print(hmm1)
    print(hmm2)
    fig.canvas.draw_idle()


next_btn.on_clicked(next)
plt.show()
