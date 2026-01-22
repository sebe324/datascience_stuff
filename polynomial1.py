from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Slider


def f(x, a, b, c):
    return a * x**2 + b * x + c


a = 1
b = 1
c = 1
t = np.linspace(-50, 50, 1000)

fig = plt.figure(figsize=(10, 6))

axs = fig.subplots(ncols=1, nrows=4, gridspec_kw={"height_ratios": [3, 1, 1, 1]})

line = axs[0].plot(t, f(t, 1, 1, 1))
a_slider = Slider(ax=axs[1], valmin=-15, valmax=15, valinit=a, label="a")
b_slider = Slider(ax=axs[2], valmin=-150, valmax=150, valinit=b, label="b")
c_slider = Slider(ax=axs[3], valmin=-1500, valmax=1500, valinit=c, label="c")
axs[0].set_ylim((-5000, 5000))


def update(val):
    print((a_slider.val))
    y = f(t, a_slider.val, b_slider.val, c_slider.val)
    line[0].set_ydata(y)
    fig.canvas.draw_idle()


a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)


plt.show()
