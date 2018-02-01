from hexgrid import HexPoints, create_spiral
from hexgrid.plotting import plot_hexagons
import matplotlib.pyplot as plt
import numpy as np


points = create_spiral(max_radius=4, center=HexPoints(0, 0, 0))

plot_hexagons(points, edgecolor='k', linewidth=4, facecolor='lightgray')

phis = np.arange(0, 2 * np.pi, np.pi * 2/3)


for i, p in enumerate(points):
    x, y = p.cartesian

    for axis, phi, coord, color in zip('xyz', phis, p.points[0], ['C0', 'C1', 'C2']):
        label_x = x + 0.4 * np.cos(phi + np.pi / 6)
        label_y = y + 0.4 * np.sin(phi + np.pi / 6)

        if i == 0:
            label = axis
        else:
            label = '{:-2d}'.format(coord)

        plt.text(
            label_x, label_y, label,
            va='center', ha='center', color=color, weight='bold',
        )

plt.gca().set_axis_off()
plt.tight_layout()
plt.show()
