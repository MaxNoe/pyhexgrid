import matplotlib.pyplot as plt
import hexgrid
from hexgrid.plotting import plot_hexagons

spiral = hexgrid.create_spiral(hexgrid.HexPoints(0, 0, 0), 5)

plot_hexagons(spiral, facecolor='lightgray')

for i, (x, y) in enumerate(zip(*spiral.cartesian)):
    plt.text(x, y, str(i), va='center', ha='center')

plt.show()
