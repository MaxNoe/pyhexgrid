# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from hexgrid.plotting import (
    plot_hexagons_odd_row_offset,
    plot_hexagons_even_row_offset,
    plot_hexagons_odd_col_offset,
    plot_hexagons_even_col_offset,
)
from hexgrid.conversions import (
    odd_row_offset2cube,
    even_row_offset2cube,
    odd_col_offset2cube,
    even_col_offset2cube,
    cube2cartesian_pointy_top,
    cube2cartesian_flat_top,
)

col, row = np.array([
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2],
]).T


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.set_title('odd row')
p = plot_hexagons_odd_row_offset(col, row, ax=ax1)
p.set_facecolors('lightgray')
p.set_linewidth(2)
for c, r in zip(col, row):
    x, y, z = odd_row_offset2cube(c, r)
    x, y = cube2cartesian_pointy_top(x, y, z)
    ax1.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')

ax2.set_title('even row')
p = plot_hexagons_even_row_offset(col, row, ax=ax2)
p.set_facecolors('lightgray')
p.set_linewidth(2)
for c, r in zip(col, row):
    x, y, z = even_row_offset2cube(c, r)
    x, y = cube2cartesian_pointy_top(x, y, z)
    ax2.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')

ax3.set_title('odd col')
p = plot_hexagons_odd_col_offset(col, row, ax=ax3)
p.set_facecolors('lightgray')
p.set_linewidth(2)
for c, r in zip(col, row):
    x, y, z = odd_col_offset2cube(c, r)
    x, y = cube2cartesian_flat_top(x, y, z)
    ax3.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')

ax4.set_title('even col')
p = plot_hexagons_even_col_offset(col, row, ax=ax4)
p.set_facecolors('lightgray')
p.set_linewidth(2)
for c, r in zip(col, row):
    x, y, z = even_col_offset2cube(c, r)
    x, y = cube2cartesian_flat_top(x, y, z)
    ax4.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')

plt.show()
