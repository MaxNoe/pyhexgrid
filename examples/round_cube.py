# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from hexgrid.plotting import plot_hexagons_cube
from hexgrid.utils import cube_round
from hexgrid.conversions import cartesian2cube_pointy_top
from matplotlib import colors


CUBE2ID = {
    (0, 0, 0): 0,
    (0, 1, -1): 1,
    (0, -1, 1): 2,
    (-1, 0, 1): 3,
    (-1, 1, 0): 4,
    (1, -1, 0): 5,
    (1, 0, -1): 6,
}

hx, hy, hz = np.array([
    [0, 0, 0],
    [0, 1, -1],
    [0, -1, 1],
    [-1, 0, 1],
    [-1, 1, 0],
    [1, -1, 0],
    [1, 0, -1],
]).T


cmap = plt.get_cmap('inferno')
cmap = colors.ListedColormap([cmap(i) for i in np.linspace(0, 1, len(hx) + 1)])


@np.vectorize
def cube2id(x, y, z):
    return CUBE2ID.get((x, y, z), -1)

px, py = np.meshgrid(np.linspace(-3, 3, 1000), np.linspace(-3, 3, 1000))

cxs, cys, czs = cartesian2cube_pointy_top(px, py)
cxs, cys, czs = cube_round(cxs, cys, czs)

counts = np.zeros_like(hx)
ids = cube2id(cxs, cys, czs)

counts_hit = np.bincount(ids[ids >= 0])
counts[:len(counts_hit)] = counts_hit

plt.scatter(px, py, c=ids, linewidth=0, cmap=cmap, norm=colors.BoundaryNorm(np.arange(len(hx) + 2) -1.5, cmap.N), s=3)
plt.colorbar()
p = plot_hexagons_cube(hx, hy, hz, pointy=True)
p.set_facecolor('none')
p.set_edgecolor('r')
plt.show()
