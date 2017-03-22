from .utils import DIRECTIONS, concatenate
from .hexpoints import HexPoints


def create_ring(radius, center=None, orientation=None):
    if center is None:
        orientation = orientation or 'pointy_top'
        center = HexPoints(0, 0, 0, orientation=orientation)
    else:
        orientation = center.orientation

    if radius == 0:
        return center

    current_point = center + radius * DIRECTIONS[orientation][4]
    points = []
    for direction in DIRECTIONS[orientation]:
        for i in range(radius):
            points.append(current_point)
            current_point = current_point + direction

    return concatenate(*points)


def create_spiral(max_radius, center=None, orientation=None):

    if center is None:
        orientation = orientation or 'pointy_top'
        center = HexPoints(0, 0, 0, orientation=orientation)
    else:
        orientation = center.orientation

    return concatenate(*[
        create_ring(radius, center=center) for radius in range(max_radius)
    ])
