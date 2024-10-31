
import matplotlib.pyplot as _plot
import numpy as np


def get_points(g, q, n):
    x = []
    y = []
    
    for p in range(1, n):
        x.append(p)
        y.append(g**p % q)

    return {"x": x, "y": y}

def plot_fourier(x, y, n, period):
    _plot.plot(x, y)

    _plot.xlabel('Frequency')
    _plot.ylabel('Amplitude')
    _plot.xticks(np.arange(0, n, period))

    _plot.show()

def main():
    n = 100
    coordinates = get_points(7, 15, n)
    plot_fourier(
        coordinates["x"],
        coordinates["y"],
        n,
        4
    )

if __name__ == "__main__":
    main()