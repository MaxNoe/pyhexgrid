import numpy as np

from .conversions import (
    cube2even_row_offset, cube2odd_row_offset,
    even_row_offset2cube, odd_row_offset2cube,
)


class PointyTopHex:
    def __init__(self, x, y, z):
        self.cube = np.array([x, y, z])
        if self.cube.ndim == 1:
            self.cube.shape = (1, 3)
        else:
            self.cube = self.cube.T
        assert np.sum(self.cube) == 0, 'Cube coordinates do not add up to 0'

    def __add__(self, other):
        cube = self.cube + other.cube
        return self.__class__.from_array(cube)

    def __sub__(self, other):
        cube = self.cube - other.cube
        return self.__class__.from_array(cube)

    @classmethod
    def from_array(cls, cube):
        return cls(cube[:, 0], cube[:, 1], cube[:, 2])

    @classmethod
    def from_even_row_offset(cls, row, col):
        x, y, z = even_row_offset2cube(row, col)
        return cls(x, y, z)

    @classmethod
    def from_odd_row_offset(cls, row, col):
        x, y, z = odd_row_offset2cube(row, col)
        return cls(x, y, z)

    @classmethod
    def from_axial(cls, x, z):
        return cls(x, -x - z, z)

    @property
    def x(self):
        return self.cube[:, 0]

    @property
    def y(self):
        return self.cube[:, 1]

    @property
    def z(self):
        return self.cube[:, 2]

    @property
    def even_row_offset(self):
        return cube2even_row_offset(self.x, self.y, self.z)

    @property
    def odd_row_offset(self):
        return cube2odd_row_offset(self.x, self.y, self.z)

    @property
    def axial(self):
        return self.array[0], self.array[2]

    def __len__(self):
        return self.cube.shape[0]

    def __repr__(self):
        np.set_printoptions(threshold=5)
        if len(self.cube.shape) == 1:
            s = self.__class__.__name__ + '(x={}, y={}, z={})'.format(
                self.x, self.y, self.z
            )
        else:
            s = self.__class__.__name__ + '(\n  x={},\n  y={},\n  z={}\n)'.format(
                self.x, self.y, self.z
            )
        np.set_printoptions()
        return s
