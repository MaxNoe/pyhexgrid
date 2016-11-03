# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from hexgrid.plotting import plot_hexagons_cube

x, y, z = np.array([
    [0, 0, 0],
    [0, 1, -1],
    [0, -1, 1],
    [-1, 0, 1],
    [-1, 1, 0],
    [1, -1, 0],
    [1, 0, -1],
]).T

plot_hexagons_cube(x, y, z, pointy=False)
plt.show()
