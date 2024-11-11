
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

    for i_x, i_y in zip(x, y):
        _plot.text(i_x, i_y, f"({i_x}, {i_y})")

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
    collapsed_coordinates = {"x": [], "y": []}
    arbritary_y = coordinates["y"][0]
    for index, y in enumerate(coordinates["y"]):
        if y == arbritary_y:
            collapsed_coordinates["x"].append(coordinates["x"][index])
            collapsed_coordinates["y"].append(coordinates["y"][index])

    plot_fourier(
        collapsed_coordinates["x"],
        collapsed_coordinates["y"],
        n,
        4
    )

if __name__ == "__main__":
    main()