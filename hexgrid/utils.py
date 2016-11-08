import numpy as np

from .hexpoints import HexPoints


DIRECTIONS = HexPoints.from_points([
    (1, -1, 0),
    (1, 0, -1),
    (0, 1, -1),
    (-1, 1, 0),
    (-1, 0, 1),
    (0, -1, 1)
])


def get_neighbors(hexpoints):
    return [h + DIRECTIONS for h in hexpoints]


def cube_round(hexpoints):
    ''' Round cube coordinates to nearest hexagon center '''
    x = hexpoints.x
    y = hexpoints.y
    z = hexpoints.z

    rx = np.round(x)
    ry = np.round(y)
    rz = np.round(z)

    x_diff = np.abs(x - rx)
    y_diff = np.abs(y - ry)
    z_diff = np.abs(z - rz)

    mask1 = np.logical_and(x_diff > y_diff, x_diff > z_diff)
    rx[mask1] = -ry[mask1] - rz[mask1]

    mask2 = np.logical_and(np.logical_not(mask1), y_diff > z_diff)
    ry[mask2] = -rx[mask2] - rz[mask2]

    mask3 = np.logical_not(mask2)
    rz[mask3] = -rx[mask3] - ry[mask3]

    return HexPoints(rx, ry, rz)


def append(hexpoints1, hexpoints2):
    points = np.append(hexpoints1.cube, hexpoints2.cube, axis=0)
    return HexPoints.from_points(points)


def concatenate(*args):
    points = np.concatenate([hexpoints.cube for hexpoints in args], axis=0)
    return HexPoints.from_points(points)
