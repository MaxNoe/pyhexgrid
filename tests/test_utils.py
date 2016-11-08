import numpy as np


def test_append():
    from hexgrid import HexPoints, append
    h1 = HexPoints(1, 0, -1)
    h2 = HexPoints(-1, 0, 1)

    h = append(h1, h2)
    assert len(h) == 2
    assert h.points.shape == (2, 3)
    assert np.all(h.points == np.array([[1, 0, -1], [-1, 0, 1]]))


def test_concatenate():
    from hexgrid import HexPoints, concatenate
    h1 = HexPoints(1, 0, -1)
    h2 = HexPoints(-1, 0, 1)
    h3 = HexPoints(-1, 2, -1)

    h = concatenate(h1, h2, h3)
    assert len(h) == 3
    assert h.points.shape == (3, 3)
    assert np.all(h.points == np.array([[1, 0, -1], [-1, 0, 1], [-1, 2, -1]]))
