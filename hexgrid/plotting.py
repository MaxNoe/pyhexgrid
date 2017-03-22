import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import RegularPolygon


def plot_hexagons(
        hexpoints,
        ax=None,
        facecolor=None,
        edgecolor=None,
        linewidth=None,
        key=None,
        cmap=None,
        ):

    ax = ax or plt.gca()
    x, y = hexpoints.cartesian

    if hexpoints.orientation == 'pointy_top':
        orientation = 0
    else:
        orientation = np.pi / 6

    hexagons = [
        RegularPolygon(xy, 6, radius=1, orientation=orientation)
        for xy in zip(x, y)
    ]

    collection = PatchCollection(hexagons)

    if facecolor is not None:
        collection.set_facecolor(facecolor)
    if edgecolor is not None:
        collection.set_edgecolor(edgecolor)
    if linewidth is not None:
        collection.set_linewidth(linewidth)

    if key is not None:
        collection.set_array(hexpoints.data[key])
        collection.set_cmap(plt.get_cmap(cmap))

    ax.add_collection(collection)
    ax.set_xlim(np.min(x) - 1, np.max(x) + 1)
    ax.set_ylim(np.min(y) - 1, np.max(y) + 1)
    ax.set_aspect(1)

    plt.draw_if_interactive()
    return collection
