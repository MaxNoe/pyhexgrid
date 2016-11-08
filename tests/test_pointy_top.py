import numpy as np
from hexgrid import PointyTopHex


def test_len():

    n = 10
    x, z = np.random.randint(0, 5, (2, n))
    p = PointyTopHex(x, -x - z, z)
    assert len(p) == n

    p = PointyTopHex(-1, 0, 1)
    assert len(p) == 1


def test_add():
    p1 = PointyTopHex(-1, 0, 1)
    p2 = PointyTopHex(1, 0, -1)

    p = p1 + p2
    assert p.x == 0
    assert p.y == 0
    assert p.z == 0

    p1 = PointyTopHex(-1, 0, 1)
    p2 = PointyTopHex([1, 0], [-1, 1], [0, -1])

    p = p1 + p2
    assert np.all(p.x == np.array([0, -1]))
    assert np.all(p.y == np.array([-1, 1]))
    assert np.all(p.z == np.array([1, 0]))


def test_sub():
    p1 = PointyTopHex(-1, 0, 1)
    p2 = PointyTopHex(2, 0, -2)

    p = p1 - p2
    assert p.x == -3
    assert p.y == 0
    assert p.z == 3

    p1 = PointyTopHex(-1, 0, 1)
    p2 = PointyTopHex([1, 0], [-1, 1], [0, -1])

    p = p1 - p2
    assert np.all(p.x == np.array([-2, -1]))
    assert np.all(p.y == np.array([1, -1]))
    assert np.all(p.z == np.array([1, 2]))
