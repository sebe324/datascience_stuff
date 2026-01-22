import matplotlib.pyplot as plt


class DataContainer:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def plot(self, ax=None, **kwargs):
        if ax is None:
            ax = plt.gca()

        ax.plot(self._x, self._y, **kwargs)
        ax.set_title("Plotted from DataContainer class!")
        return ax


if __name__ == "__main__":
    data = DataContainer([0, 1, 2, 3], [0, 0.2, 0.5, 0.3])
    data.plot()
    plt.show()
