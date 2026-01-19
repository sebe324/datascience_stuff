from typing import Tuple
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


"""
Pairwise data 

- plot
- scatter
- bar
- step 

Array objects

- pcolormesh
- contour
- quiver
- streamplot
- imshow

Statistical distributions

- hist
- errorbar
- hist2d
- pie
- boxplot
- violinplot

Irregularly gridded data

- tricontour
- tripcolor

"""
fig = plt.figure(figsize=(20, 20))


fig_pairwise: Figure
fig_array: Figure
fig_stat: Figure
fig_irreg: Figure

fig_pairwise, fig_array, fig_stat, fig_irreg = fig.subfigures(ncols=4, nrows=1)


fig_pairwise.set_facecolor("#ffc9c9")
fig_array.set_facecolor("#d8f999")
fig_stat.set_facecolor("#a2f4fd")
fig_irreg.set_facecolor("#fff085")

fig_pairwise.suptitle("Pairwise plot types")
fig_array.suptitle("Array plot types")
fig_stat.suptitle("Statistical plot types")
fig_irreg.suptitle("Irregular plot types")


axs_pairwise = fig_pairwise.subplots(ncols=1, nrows=4)

x = np.arange(100)
y = np.cumsum(np.random.randn(100))

axs_pairwise[0].plot(x, y)
axs_pairwise[0].set_title("Plot")

axs_pairwise[1].scatter(x, y)
axs_pairwise[1].set_title("Scatter")

axs_pairwise[2].bar(x, y)
axs_pairwise[2].set_title("Bar")

axs_pairwise[3].step(x, y)
axs_pairwise[3].set_title("Step")


axs_array = fig_array.subplots(ncols=1, nrows=5)

test = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]

pcm = axs_array[0].pcolormesh(test)
fig_array.colorbar(pcm, ax=axs_array[0])

axs_array[1].contour(test)


x = np.linspace(0, 2, 5)  # 5 points along x
y = np.linspace(0, 2, 5)  # 5 points along y
X, Y = np.meshgrid(x, y)

print("LOL")
print(x)
# Generate vector components (U, V)
U = np.cos(X)  # horizontal component
V = np.sin(Y)  # vertical component

# Plot the quiver
ax_quiver: Axes
ax_quiver = axs_array[2]
ax_quiver.quiver(X, Y, U, V)


ax_streamplot: Axes
ax_streamplot = axs_array[3]
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)
print(x, y)
# Define a rotational vector field
U = -Y  # x-component
V = X  # y-component
ax_streamplot.streamplot(
    X, Y, U, V, color=np.sqrt(U**2 + V**2), linewidth=2, cmap="viridis"
)

test_color = [
    [[255, 0, 0], [255, 255, 0], [255, 0, 255]],
    [[0, 255, 0], [0, 255, 225], [255, 255, 0]],
    [[0, 0, 255], [255, 0, 255], [0, 255, 255]],
]
axs_array[4].imshow(test_color)
plt.show()
