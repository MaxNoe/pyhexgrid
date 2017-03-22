from .utils import DIRECTIONS, concatenate
from .hexpoints import HexPoints


def create_ring(radius, center=None):
    center = center or HexPoints(0, 0, 0)

    if radius == 0:
        return center

    current_point = center + radius * DIRECTIONS[4]
    points = []
    for direction in DIRECTIONS:
        for i in range(radius):
            points.append(current_point)
            current_point = current_point + direction

    return concatenate(*points)


def create_spiral(max_radius, center=None):
    center = center or HexPoints(0, 0, 0)
    return concatenate(*[
        create_ring(center, radius) for radius in range(max_radius)
    ])
