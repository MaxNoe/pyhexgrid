import numpy as np
import pandas as pd

from .hexpoints import HexPoints

DIRECTIONS = {
    orientation: HexPoints.from_points([
        (1, -1, 0),
        (1, 0, -1),
        (0, 1, -1),
        (-1, 1, 0),
        (-1, 0, 1),
        (0, -1, 1)
    ], orientation=orientation)
    for orientation in ('flat_top', 'pointy_top')
}


def get_neighbors(hexpoints):
    return [h + DIRECTIONS[h.orientation] for h in hexpoints]


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

    return HexPoints(
        rx, ry, rz,
        data=hexpoints.data,
        orientation=hexpoints.orientation,
    )


def append(hexpoints1, hexpoints2):
    assert hexpoints1.orientation == hexpoints2.orientation
    points = np.append(hexpoints1.points, hexpoints2.points, axis=0)

    new = HexPoints.from_points(points, orientation=hexpoints1.orientation)
    new.data = hexpoints1.data.append(hexpoints2.data)

    return new


def concatenate(*args):
    assert all(args[0].orientation == p.orientation for p in args)

    points = np.concatenate([hexpoints.points for hexpoints in args], axis=0)
    data = pd.concat([hexpoints.data for hexpoints in args])
    return HexPoints.from_points(points, orientation=args[0].orientation)
