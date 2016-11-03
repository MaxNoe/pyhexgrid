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


def outer2inner_radius(outer_radius):
    return 0.5 * np.sqrt(3) * outer_radius
