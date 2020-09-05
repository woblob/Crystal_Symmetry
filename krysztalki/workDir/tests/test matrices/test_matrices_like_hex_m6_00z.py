import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_m6_00z:

    def test_matrix_hex_m6_00z(self):
        expected = Point([ -x+y, -x, -z, 1])
        calculated = Point.calculate(mne._matrix_hex_m6_00z)
        assert calculated == expected
