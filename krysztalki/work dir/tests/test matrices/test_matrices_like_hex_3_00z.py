import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.base_point = np.array([x, y, z, 1])


class Test_Axis_hex_3_00z:

    def test_matrix_hex_3_00z(self):
        expected = Point([ -y, x-y, z, 1])
        calculated = Point.calculate(mne._matrix_hex_3_00z)
        assert calculated == expected

    def test_matrix_hex_3_1_00z_00t(self):
        expected = Point([ -y, x-y, 2/3+z, 1])
        calculated = Point.calculate(mne._matrix_hex_3_1_00z_00t)
        assert calculated == expected

    def test_matrix_hex_3_2_00z_002t(self):
        expected = Point([ -y, x-y, 4/3+z, 1])
        calculated = Point.calculate(mne._matrix_hex_3_2_00z_002t)
        assert calculated == expected
