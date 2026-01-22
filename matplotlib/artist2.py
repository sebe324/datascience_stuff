import matplotlib.pyplot as plt
import matplotlib.artist as martist
import numpy as np
import matplotlib

import matplotlib.patches as mpatches

fig = plt.figure(figsize=(4, 2.5))
ax = fig.subplots(1, 1)

circle = mpatches.Circle((0.5, 0.5), 0.25, ec="none")

ax.add_artist(circle)

clipped_circle = mpatches.Circle((1, 0.5), 0.125, ec="none", facecolor="C1")

ax.add_artist(clipped_circle)
ax.set_aspect(1)

# circle.remove()
plt.show()
