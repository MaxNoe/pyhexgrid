import hexgrid
import numpy as np
import matplotlib.pyplot as plt


points = hexgrid.create_spiral(hexgrid.HexPoints(0, 0, 0), 4)

points.data['id'] = np.arange(len(points))
points.data['random'] = np.random.normal(size=len(points))


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_size_inches(9, 3)

for ax in (ax1, ax2):
    ax.set_axis_off()
    ax.set_xlabel('')
    ax.set_ylabel('')


p1 = hexgrid.plot_hexagons(points, key='id', ax=ax1)
fig.colorbar(p1, ax=ax1)

p2 = hexgrid.plot_hexagons(points, key='random', ax=ax2)
fig.colorbar(p2, ax=ax2)

fig.tight_layout()
plt.show()
