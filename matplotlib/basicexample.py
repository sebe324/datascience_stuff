import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure(figsize=(4, 2), facecolor="lightskyblue", layout="constrained")

fig.suptitle("A nice Matplotlib Fugre")

ax = fig.add_subplot()
ax.set_title("Axes", loc="left", fontstyle="oblique", fontsize="medium")
plt.show()
