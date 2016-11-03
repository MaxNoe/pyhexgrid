import numpy as np


COS30 = np.cos(np.pi/6)
SIN30 = np.sin(np.pi/6)


def rotate(x, y, angle):
    x_prime = np.cos(angle) * x - np.sin(angle) * y
    y_prime = np.sin(angle) * x + np.cos(angle) * y
    return x_prime, y_prime


def cube2cartesian_pointy_top(cube_x, cube_y, cube_z):
    cartesian_x = COS30 * (cube_x - cube_y)
    cartesian_y = SIN30 * (cube_x + cube_y) - cube_z
    return cartesian_x, cartesian_y


def cube2cartesian_flat_top(cube_x, cube_y, cube_z):
    cartesian_x = cube_x - SIN30 * (cube_y + cube_z)
    cartesian_y = COS30 * (cube_y - cube_z)
    return cartesian_x, cartesian_y


def cartesian2cube_pointy_top(cartesian_x, cartesian_y):
    cube_x = cartesian_x / np.sqrt(3) + cartesian_y / 3
    cube_z = - 2 / 3 * cartesian_y

    return cube_x, -cube_x - cube_z, cube_z


def outer2inner_radius(outer_radius):
    return 0.5 * np.sqrt(3) * outer_radius


def cube2axial(x, y, z):
    return x, z


def axial2cube(x, y, z):
    return x, -x - z, z


def cube2even_col_offset(x, y, z):
    col = x
    row = z + (x + (x & 1)) / 2

    return col, row


def even_col_offset2cube(col, row):
    x = col
    z = row - (col + (col & 1)) / 2
    y = -x - z
    return x, y, z


def cube2odd_col_offset(x, y, z):
    col = x
    row = z + (x - (x & 1)) / 2

    return col, row


def odd_col_offset2cube(col, row):
    x = col
    z = row - (col - (col & 1)) / 2
    y = -x - z
    return x, y, z


def cube2even_row_offset(x, y, z):
    col = x + (z + (z & 1)) / 2
    row = z

    return col, row


def even_row_offset2cube(col, row):
    x = col - (row + (row & 1)) / 2
    z = row
    y = -x - z
    return x, y, z


def cube2odd_row_offset(x, y, z):
    col = x + (z - (z & 1)) / 2
    row = z

    return col, row


def odd_row_offset2cube(col, row):
    x = col - (row - (row & 1)) / 2
    z = row
    y = -x - z
    return x, y, z
