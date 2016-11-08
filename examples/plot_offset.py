# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from hexgrid.plotting import plot_hexagons
from hexgrid import HexPoints


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
], dtype=int).T


hexpoints_even_row = HexPoints.from_even_row_offset(col, row)
hexpoints_even_col = HexPoints.from_even_col_offset(col, row)
hexpoints_odd_row = HexPoints.from_odd_row_offset(col, row)
hexpoints_odd_col = HexPoints.from_odd_col_offset(col, row)


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.set_title('odd row')
p = plot_hexagons(hexpoints_odd_row, ax=ax1)
p.set_facecolors('lightgray')
p.set_linewidth(2)
xs, ys = hexpoints_odd_row.cartesian
cs, rs = hexpoints_odd_row.odd_row_offset
for x, y, c, r in zip(xs, ys, cs, rs):
    ax1.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')


ax2.set_title('even row')
p = plot_hexagons(hexpoints_even_row, ax=ax2)
p.set_facecolors('lightgray')
p.set_linewidth(2)
xs, ys = hexpoints_even_row.cartesian
cs, rs = hexpoints_even_row.odd_row_offset
for x, y, c, r in zip(xs, ys, cs, rs):
    ax2.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')

ax3.set_title('odd col')
p = plot_hexagons(hexpoints_odd_col, ax=ax3)
p.set_facecolors('lightgray')
p.set_linewidth(2)
xs, ys = hexpoints_odd_col.cartesian
cs, rs = hexpoints_odd_col.odd_col_offset
for x, y, c, r in zip(xs, ys, cs, rs):
    ax3.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')


ax4.set_title('even col')
p = plot_hexagons(hexpoints_even_col, ax=ax4)
p.set_facecolors('lightgray')
p.set_linewidth(2)
xs, ys = hexpoints_even_col.cartesian
cs, rs = hexpoints_even_col.odd_col_offset
for x, y, c, r in zip(xs, ys, cs, rs):
    ax4.text(x, y, '{}, {}'.format(c, r), size=12, va='center', ha='center')

plt.show()
