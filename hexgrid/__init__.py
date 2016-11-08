import numpy as np

from .conversions import (
    cube2even_row_offset, cube2odd_row_offset,
    even_row_offset2cube, odd_row_offset2cube,
    cube2cartesian_pointy_top, cube2cartesian_flat_top
)


class HexPoints:
    def __init__(self, x, y, z, orientation='pointy_top'):
        if orientation not in ('pointy_top', 'flat_top'):
            raise ValueError('orientation must be "pointy_top" or "flat_top"')
        self.orientation = orientation

        self.cube = np.array([x, y, z])
        if self.cube.ndim == 1:
            self.cube.shape = (1, 3)
        else:
            self.cube = self.cube.T

        if not np.isclose(np.sum(self.cube), 0):
            raise ValueError('Cube coordinates do not add up to 0')

    def __add__(self, other):
        if self.orientation != other.orientation:
            raise ValueError('HexPoints have different orientations')
        cube = self.cube + other.cube
        return self.__class__.from_array(cube)

    def __sub__(self, other):
        if self.orientation != other.orientation:
            raise ValueError('HexPoints have different orientations')
        cube = self.cube - other.cube
        return self.__class__.from_array(cube)

    @classmethod
    def from_array(cls, cube, orientation='pointy_top'):
        return cls(cube[:, 0], cube[:, 1], cube[:, 2], orientation=orientation)

    @classmethod
    def from_even_row_offset(cls, row, col):
        x, y, z = even_row_offset2cube(row, col)
        return cls(x, y, z, orientation='pointy_top')

    @classmethod
    def from_odd_row_offset(cls, row, col):
        x, y, z = odd_row_offset2cube(row, col)
        return cls(x, y, z, orientation='pointy_top')

    @classmethod
    def from_axial(cls, x, z, orientation='pointy_top'):
        return cls(x, -x - z, z, orientation=orientation)

    @property
    def x(self):
        if len(self) > 0:
            return self.cube[:, 0]
        else:
            return np.array([])

    @property
    def y(self):
        if len(self) > 0:
            return self.cube[:, 1]
        else:
            return np.array([])

    @property
    def z(self):
        if len(self) > 0:
            return self.cube[:, 2]
        else:
            return np.array([])

    @property
    def even_row_offset(self):
        if self.orientation == 'flat_top':
            raise NotImplemented(
                'Even row offset coordinates not valid for flat_top orientation'
            )
        return cube2even_row_offset(self.x, self.y, self.z)

    @property
    def odd_row_offset(self):
        if self.orientation == 'flat_top':
            raise NotImplemented(
                'Even row offset coordinates not valid for flat_top orientation'
            )
        return cube2odd_row_offset(self.x, self.y, self.z)

    @property
    def axial(self):
        return self.array[0], self.array[2]

    @property
    def cartesian(self):
        if self.orientation == 'pointy_top':
            return cube2cartesian_pointy_top(self.x, self.y, self.z)
        return cube2cartesian_flat_top(self.x, self.y, self.z)

    def __len__(self):
        return self.cube.shape[0]

    def __repr__(self):
        np.set_printoptions(threshold=5)
        if len(self.cube.shape) == 1:
            s = self.__class__.__name__ + '({}, x={}, y={}, z={})'.format(
                self.orientation, self.x, self.y, self.z
            )
        else:
            s = self.__class__.__name__ + '({},\n  x={},\n  y={},\n  z={}\n)'.format(
                self.orientation, self.x, self.y, self.z
            )
        np.set_printoptions()
        return s

    def __getitem__(self, sl):
        other = self.__class__([], [], [])
        cube = self.cube[sl]
        if cube.ndim == 1:
            cube.shape = (1, 3)
        other.cube = cube
        return other

    def __eq__(self, other):
        return np.all(self.cube == other.cube, axis=1)


DIRECTIONS = HexPoints.from_array(np.array([
    (1, -1, 0),
    (1, 0, -1),
    (0, 1, -1),
    (-1, 1, 0),
    (-1, 0, 1),
    (0, -1, 1)
]))


def get_neighbors(hexpoints):
    return [h + DIRECTIONS for h in hexpoints]
