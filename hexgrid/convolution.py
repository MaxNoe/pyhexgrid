from .utils import DIRECTIONS


def convolve7(hexpoints, key, kernel, fill_value=0):

    convolved = kernel[0] * hexpoints.data[key]

    for value, d in zip(kernel, DIRECTIONS[hexpoints.orientation]):
        neighbors = hexpoints + d
        resp = hexpoints.data.loc[neighbors._data_index, key].fillna(0).values

        convolved += value * resp

    return convolved
