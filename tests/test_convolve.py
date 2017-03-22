import hexgrid
from hexgrid.convolution import convolve7
import numpy as np


def test_conv7():
    p = hexgrid.create_spiral(3)

    p.data['a'] = np.zeros(len(p))
    p.data.loc[(0, 0), 'a'] = 1

    p.data['conv1'] = convolve7(p, key='a', kernel=np.ones(7))

    assert p.data.loc[(0, 0), 'conv1'] == 1.0
    assert p.data.loc[(0, 1), 'conv1'] == 1.0
