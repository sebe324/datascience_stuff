import matplotlib.pyplot as plt

import numpy as np


fig = plt.figure(figsize=(12, 2))

axs = fig.subplots(nrows=1, ncols=4)


def f1(mg):
    return mg[0] * mg[1]


def f2(mg):
    return np.sin(mg[0]) * np.cos(mg[1])


def f3(mg):
    # return mg[0] ** 2 / mg[1] ** 2
    x, y = mg
    return np.sin(x + y)


def f4(mg):
    x = mg[0]
    y = mg[1]

    return np.cos(x**2 + y**2 - x - y)


x = np.arange(-2.5, 2.5, 0.1)
y = np.arange(-2.5, 2.5, 0.1)
mg = np.meshgrid(x, y)
result = f1(mg)
print(result[0])
# z = np.random.rand(6, 10)
# print(z)
axs[0].pcolormesh(x, y, result)

result = f2(mg)
axs[1].pcolormesh(x, y, result)

result = f3(mg)
axs[2].pcolormesh(x, y, result)
result = f4(mg)
axs[3].pcolormesh(x, y, result)
plt.show()
