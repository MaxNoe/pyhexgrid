import numpy as np
from pytest import approx


def test_rotation_x():
    from hexgrid.conversions import rotate

    x = 1
    y = 0

    rot_x, rot_y = rotate(x, y, np.pi/2)
    assert rot_x == approx(0)
    assert rot_y == approx(1)


def test_rotation_y():
    from hexgrid.conversions import rotate
    x = 0
    y = 1
    rot_x, rot_y = rotate(x, y, np.pi/2)
    assert rot_x == approx(-1)
    assert rot_y == approx(0)


def test_cube2cartesian_pointy_top():
    from hexgrid.conversions import cube2cartesian_pointy_top, outer2inner_radius

    x, y = cube2cartesian_pointy_top(0, 0, 0)
    assert x == approx(0)
    assert y == approx(0)

    x, y = cube2cartesian_pointy_top(0, 0, 1)
    assert x == approx(0)
    assert y == approx(-1)

    x, y = cube2cartesian_pointy_top(1, 1, -2)
    assert x == approx(0)
    assert y == approx(3)

    x, y = cube2cartesian_pointy_top(-2, 2, 0)
    assert x == approx(- 4 * outer2inner_radius(1))
    assert y == approx(0)


def test_cube_odd_col():
    from hexgrid.conversions import cube2odd_col_offset, odd_col_offset2cube
    x, y, z = 1, -2, 1

    row, col = cube2odd_col_offset(x, y, z)
    res_x, res_y, res_z = odd_col_offset2cube(row, col)

    assert res_x == x
    assert res_y == y
    assert res_z == z


def test_cube_event_q():
    from hexgrid.conversions import cube2even_col_offset, even_col_offset2cube
    x, y, z = 1, -2, 1

    row, col = cube2even_col_offset(x, y, z)
    res_x, res_y, res_z = even_col_offset2cube(row, col)

    assert res_x == x
    assert res_y == y
    assert res_z == z
