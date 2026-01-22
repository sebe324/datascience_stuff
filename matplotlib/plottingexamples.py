from typing import Tuple
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as tri
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


axs_stat = fig_stat.subplots(ncols=1, nrows=5)

stat_data = [5, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 2, 1, 1]

axs_stat[0].hist(stat_data)
axs_stat[0].set_title("hist")
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

# example error bar values that vary with x-position
error = 0.1 + 0.2 * x


axs_stat[1].errorbar(x, y, yerr=error, fmt="-o")
axs_stat[1].set_title("errorbar")

size = 100000
x = np.random.normal(size=size)
y = np.random.normal(size=size)
axs_stat[2].hist2d(x=x, y=y, bins=(50, 50))
axs_stat[2].set_title("hist2d")

x = [25, 40, 10, 15, 10]
explode = [
    0,
] * len(x)

explode[1] = 0.2

axs_stat[3].pie(
    x=x,
    explode=explode,
    autopct="%1.1f%%",
)
axs_stat[3].set_title("pie")

spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
axs_stat[4].boxplot(data)
axs_stat[4].set_title("boxplot")


axs_irreg = fig_irreg.subplots(ncols=1, nrows=2)

n_angles = 48
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.cos(radii) * np.cos(3 * angles)).flatten()

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(
    np.hypot(x[triang.triangles].mean(axis=1), y[triang.triangles].mean(axis=1))
    < min_radius
)
axs_irreg[0].set_aspect("equal")
tcf = axs_irreg[0].tricontourf(triang, z)
fig_irreg.colorbar(tcf, ax=axs_irreg[0])
axs_irreg[0].tricontour(triang, z, colors="k")
axs_irreg[0].set_title("tricounter")

axs_irreg[1].set_aspect("equal")
tpc = axs_irreg[1].tripcolor(triang, z, shading="flat")
fig_irreg.colorbar(tpc, ax=axs_irreg[1])
axs_irreg[1].set_title("tripcolor")
plt.show()
