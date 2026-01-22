import matplotlib.pyplot as plt
import matplotlib.artist as martist
import numpy as np
import matplotlib

fig = plt.figure(figsize=(4, 2.5))

ax = fig.subplots(1, 1)

x = np.arange(0, 13, 0.2)
y = np.sin(x)

lines = ax.plot(x, y, "-", linewidth=0.2, label="example", color="blue")


print(lines)

print(ax.get_lines())
print(ax.get_lines()[0])

lines[0].set(color="green", linewidth=2)

print(matplotlib.artist.getp(lines[0]))
plt.show()
