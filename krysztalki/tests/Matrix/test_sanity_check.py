import numpy as np
import sympy as sp

from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])

matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


class TestIdentity:

    def test_identity(self):
        assert Point([x, y, z, 1]).is_got_by(matrix)
