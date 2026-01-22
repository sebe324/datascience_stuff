import matplotlib.pyplot as plt

fig, axs = plt.subplot_mosaic(
    [["A", "right", "E"], ["B", "right", "E"], ["B", "C", "E"], ["D", "C", "E"]],
    figsize=(10, 10),
    layout="constrained",
)

for ax_name, ax in axs.items():
    ax.text(0.5, 0.5, ax_name, ha="center", va="center")

plt.show()
