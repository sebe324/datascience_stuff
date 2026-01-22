from matplotlib.axes import Axes
from matplotlib.figure import SubFigure
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider
import numpy as np


def f1(x, a, b):
    return a * x + b


def f2(x, a, b, c):
    return a * x**2 + b * x + c


def f3(x, a, b):
    return np.log(x**b) / np.log(a)


def f4(x, a):
    return a / x


fig = plt.figure(figsize=(10, 8))

subfig_linear: SubFigure
subfig_polynomial: SubFigure
subfig_logistic: SubFigure
subfig_hyperbolean: SubFigure
subfig_linear, subfig_polynomial, subfig_logistic, subfig_hyperbolean = fig.subfigures(
    nrows=1, ncols=4
)

x = np.arange(-100, 100)

axs_linear = subfig_linear.subplots(
    nrows=4, ncols=1, gridspec_kw={"height_ratios": [12, 2, 2, 2]}
)
line_linear = axs_linear[0].plot(x, f1(x, 1, 1))
a_linear_slider = Slider(ax=axs_linear[1], valmin=-2, valmax=2, valinit=1, label="a")
b_linear_slider = Slider(ax=axs_linear[2], valmin=-15, valmax=15, valinit=1, label="b")


def update_linear(val):
    y = f1(x, a_linear_slider.val, b_linear_slider.val)
    line_linear[0].set_ydata(y)
    fig.canvas.draw_idle()


a_linear_slider.on_changed(update_linear)
b_linear_slider.on_changed(update_linear)

stuff: Axes
stuff = axs_linear[3]
stuff.axis("off")

axs_polynomial = subfig_polynomial.subplots(
    nrows=4, ncols=1, gridspec_kw={"height_ratios": [12, 2, 2, 2]}
)

line_polynomial = axs_polynomial[0].plot(x, f2(x, 1, 1, 1))
a_polynomial_slider = Slider(
    ax=axs_polynomial[1], valmin=-2, valmax=2, valinit=1, label="a"
)
b_polynomial_slider = Slider(
    ax=axs_polynomial[2], valmin=-15, valmax=15, valinit=1, label="b"
)
c_polynomial_slider = Slider(
    ax=axs_polynomial[3], valmin=-15, valmax=15, valinit=1, label="c"
)


def update_polynomial(val):
    y = f2(x, a_polynomial_slider.val, b_polynomial_slider.val, c_polynomial_slider.val)
    line_polynomial[0].set_ydata(y)
    fig.canvas.draw_idle()


a_polynomial_slider.on_changed(update_polynomial)
b_polynomial_slider.on_changed(update_polynomial)
c_polynomial_slider.on_changed(update_polynomial)


axs_logistic = subfig_logistic.subplots(
    nrows=4, ncols=1, gridspec_kw={"height_ratios": [12, 2, 2, 2]}
)

line_logistic = axs_logistic[0].plot(x, f3(x, 2, 1))

a_logistic_slider = Slider(
    ax=axs_logistic[1], valmin=-10, valmax=10, valinit=1, label="a"
)
b_logistic_slider = Slider(
    ax=axs_logistic[2], valmin=-15, valmax=15, valinit=1, label="b"
)

axs_logistic[3].axis("off")


def update_logistic(val):
    y = f3(x, a_logistic_slider.val, b_logistic_slider.val)
    line_logistic[0].set_ydata(y)
    fig.canvas.draw_idle()


a_logistic_slider.on_changed(update_logistic)
b_logistic_slider.on_changed(update_logistic)

axs_hyperbolean = subfig_hyperbolean.subplots(
    nrows=4, ncols=1, gridspec_kw={"height_ratios": [12, 2, 2, 2]}
)

line_hyperbolean = axs_hyperbolean[0].plot(x, f4(x, 1))

a_hyperbolean_slider = Slider(
    ax=axs_hyperbolean[1], valmin=-10, valmax=10, valinit=1, label="a"
)


def update_hyperbolean(val):
    y = f4(x, a_hyperbolean_slider.val)
    line_hyperbolean[0].set_ydata(y)
    fig.canvas.draw_idle()


a_hyperbolean_slider.on_changed(update_hyperbolean)
axs_hyperbolean[2].axis("off")
axs_hyperbolean[3].axis("off")
plt.show()
