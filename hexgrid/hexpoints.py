import numpy as np
import pandas as pd

from .conversions import (
    cube2even_row_offset, cube2odd_row_offset,
    cube2even_col_offset, cube2odd_col_offset,
    even_row_offset2cube, odd_row_offset2cube,
    even_col_offset2cube, odd_col_offset2cube,
    cube2cartesian_pointy_top, cube2cartesian_flat_top
)


class HexPoints:
    def __init__(self, x=(), y=(), z=(), data=None, orientation='pointy_top'):
        if orientation not in ('pointy_top', 'flat_top'):
            raise ValueError('orientation must be "pointy_top" or "flat_top"')
        self.orientation = orientation

        self.points = np.array([x, y, z])
        if self.points.ndim == 1:
            self.points.shape = (1, 3)
        else:
            self.points = self.points.T

        if not np.isclose(np.sum(self.points), 0):
            raise ValueError('Cube coordinates do not add up to 0')

        self.data = data

    def __add__(self, other):
        if self.orientation != other.orientation:
            raise ValueError('HexPoints have different orientations')
        cube = self.points + other.points
        return self.__class__.from_points(cube, orientation=self.orientation)

    def __sub__(self, other):
        if self.orientation != other.orientation:
            raise ValueError('HexPoints have different orientations')
        cube = self.points - other.points
        return self.__class__.from_points(cube, orientation=self.orientation)

    def __mul__(self, number):
        if not np.isscalar(number):
            raise TypeError('HexPoints coordinates can only be multiplied by scalars')
        points = self.points * number
        return self.__class__.from_points(points, orientation=self.orientation)

    def __rmul__(self, number):
        return self.__mul__(number)

    def __radd__(self, other):
        return self.__add__(other)

    @classmethod
    def from_points(cls, points, orientation='pointy_top', data=None):
        cube = np.array(points)
        return cls(
            cube[:, 0], cube[:, 1], cube[:, 2],
            orientation=orientation,
            data=data,
        )

    @classmethod
    def from_even_row_offset(cls, col, row, data=None):
        x, y, z = even_row_offset2cube(col, row)
        return cls(x, y, z, orientation='pointy_top', data=data)

    @classmethod
    def from_odd_row_offset(cls, col, row, data=None):
        x, y, z = odd_row_offset2cube(col, row)
        return cls(x, y, z, orientation='pointy_top', data=data)

    @classmethod
    def from_even_col_offset(cls, col, row, data=None):
        x, y, z = even_col_offset2cube(col, row)
        return cls(x, y, z, orientation='flat_top', data=data)

    @classmethod
    def from_odd_col_offset(cls, col, row, data=None):
        x, y, z = odd_col_offset2cube(col, row)
        return cls(x, y, z, orientation='flat_top', data=data)

    @classmethod
    def from_axial(cls, x, z, orientation='pointy_top', data=None):
        return cls(x, -x - z, z, orientation=orientation, data=data)

    @property
    def x(self):
        if len(self) > 0:
            return self.points[:, 0]
        else:
            return np.array([])

    @property
    def y(self):
        if len(self) > 0:
            return self.points[:, 1]
        else:
            return np.array([])

    @property
    def z(self):
        if len(self) > 0:
            return self.points[:, 2]
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
    def even_col_offset(self):
        if self.orientation == 'pointy_top':
            raise NotImplemented(
                'Even row offset coordinates not valid for pointy_top orientation'
            )
        return cube2even_col_offset(self.x, self.y, self.z)

    @property
    def odd_col_offset(self):
        if self.orientation == 'pointy_top':
            raise NotImplemented(
                'Even row offset coordinates not valid for pointy_top orientation'
            )
        return cube2odd_col_offset(self.x, self.y, self.z)

    @property
    def axial(self):
        return self.points[:, 0], self.points[:, 2]

    @property
    def cartesian(self):
        if self.orientation == 'pointy_top':
            return cube2cartesian_pointy_top(self.x, self.y, self.z)
        return cube2cartesian_flat_top(self.x, self.y, self.z)

    def __len__(self):
        return self.points.shape[0]

    def __repr__(self):
        np.set_printoptions(threshold=5)
        s = self.__class__.__name__
        s += '({}'.format(self.orientation)

        if len(self) == 0:
            return s + ')'

        s += ',\n  '
        if len(self) > 6:
            with pd.option_context('display.max_rows', 6):
                s += '\n  '.join(str(self.data.reset_index()).splitlines()[:-2])
        else:
            s += '\n  '.join(str(self.data.reset_index()).splitlines())

        s += '\n)'
        return s

    def __getitem__(self, sl):
        other = self.__class__([], [], [], orientation=self.orientation)
        cube = self.points[sl]
        if cube.ndim == 1:
            cube.shape = (1, 3)
        other.points = cube
        other.data = self.data.loc[other._data_index]
        return other

    def __eq__(self, other):
        return np.all(self.points == other.points, axis=1)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, df):
        if isinstance(df, pd.DataFrame):
            self._data = df.set_index(self._data_index)
        else:
            df = pd.DataFrame(df, index=self._data_index)
            self._data = df

    @property
    def _data_index(self):
        return pd.MultiIndex.from_arrays([self.x, self.z], names=['x', 'z'])
