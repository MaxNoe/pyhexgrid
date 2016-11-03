import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import RegularPolygon

from .conversions import (
    cube2cartesian_pointy_top, cube2cartesian_flat_top,
    odd_col_offset2cube, even_col_offset2cube,
    odd_row_offset2cube, even_row_offset2cube
)


def plot_hexagons_cube(cube_x, cube_y, cube_z, ax=None, pointy=True):

    ax = ax or plt.gca()

    if pointy:
        x, y = cube2cartesian_pointy_top(cube_x, cube_y, cube_z)
        orientation = 0
    else:
        x, y = cube2cartesian_flat_top(cube_x, cube_y, cube_z)
        orientation = np.pi / 6

    hexagons = [
        RegularPolygon(xy, 6, radius=1, orientation=orientation)
        for xy in zip(x, y)
    ]

    collection = PatchCollection(hexagons)

    ax.add_collection(collection)
    ax.set_xlim(np.min(x) - 1, np.max(x) + 1)
    ax.set_ylim(np.min(y) - 1, np.max(y) + 1)
    ax.set_aspect(1)

    plt.draw_if_interactive()
    return collection


def plot_hexagons_odd_col_offset(col, row, ax=None):

    x, y, z = odd_col_offset2cube(col, row)

    return plot_hexagons_cube(x, y, z, ax=ax, pointy=False)


def plot_hexagons_even_col_offset(col, row, ax=None):

    x, y, z = even_col_offset2cube(col, row)

    return plot_hexagons_cube(x, y, z, ax=ax, pointy=False)


def plot_hexagons_odd_row_offset(col, row, ax=None):

    x, y, z = odd_row_offset2cube(col, row)

    return plot_hexagons_cube(x, y, z, ax=ax, pointy=True)


def plot_hexagons_even_row_offset(col, row, ax=None):

    x, y, z = even_row_offset2cube(col, row)

    return plot_hexagons_cube(x, y, z, ax=ax, pointy=True)
