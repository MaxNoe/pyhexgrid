import numpy as np


def cube_round(x, y, z):
    ''' Round cube coordinates to nearest hexagon center '''
    for a in (x, y, z):
        a = np.asanyarray(a)

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

    return rx, ry, rz
