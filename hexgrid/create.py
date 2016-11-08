from .utils import DIRECTIONS, concatenate


def create_ring(center, radius):

    if radius == 0:
        return center

    current_point = center + radius * DIRECTIONS[4]
    points = []
    for direction in DIRECTIONS:
        for i in range(radius):
            points.append(current_point)
            current_point = current_point + direction

    return concatenate(*points)


def create_spiral(center, max_radius):
    return concatenate(*[
        create_ring(center, radius) for radius in range(max_radius)
    ])
